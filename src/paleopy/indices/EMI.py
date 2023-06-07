def calculate_EMI(dset_anoms, lon_name='longitudes', lat_name='latitudes', clim_start=1981, clim_end=2010, name='EMI'): 
    """ 
    calculate the EMI (El Nino Modoki Index) 
    from a dataset of monthly SST anomalies (does not calculate the anomalies, they need to 
    be pre-calculated), typically ERSST version 5 

    The index is standardized WRT to average and standard deviation calculated over `clim_start` to `clim_end`
    (1981 - 2010 by default)
    """

    import numpy as np 
    import pandas as pd 
    import xarray as xr 

    dom_A = dset_anoms.sel(latitudes=slice(-10., 10.), longitudes=slice(165., 220.)).mean(dim='latitudes').mean(dim='longitudes')
    dom_B = dset_anoms.sel(latitudes=slice(-15., 5.), longitudes=slice(250., 290.)).mean(dim='latitudes').mean(dim='longitudes')
    dom_C = dset_anoms.sel(latitudes=slice(-10., 20.), longitudes=slice(125., 145.)).mean(dim='latitudes').mean(dim='longitudes')

    EMI = dom_A-0.5*dom_B-0.5*dom_C

    ave = EMI.sel(time=slice(str(clim_start), str(clim_end))).mean('time')
    std = EMI.sel(time=slice(str(clim_start), str(clim_end))).std('time')

    EMI_std = (EMI - ave) / std
    EMI_std = EMI_std.to_dataframe()
    EMI_std.columns = ['EMI']

    return EMI_std