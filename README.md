repository for the new paleopy library and the associated notebooks, allowing to run 'PICT' (Past Interpretation of Climate Tool") standalone in
a dedicated conda environment

## installation instructions:

1) clone the repository with git, or download the zip file (green `clone or download` button on the upper right of this repository), if downloading the ZIP file rename the folder created from `PICT_notebooks-master` to `PICT_notebooks`.
2) install the mamnaforge python distribution from [https://github.com/conda-forge/miniforge#mambaforge](https://github.com/conda-forge/miniforge#mambaforge)
3) in the `PICT_notebooks` directory, run at the command line (on a Mac, go to `Applications / Utilities / Terminal`):
	+ `conda env create -f PICT.yml` on a Mac
4) activate the `PICT_notebooks` environment by runnning `conda activate PICT` at the command line, then run `jupyter notebook` or `jupyter lab` (the ;latter preferred)
5) navigate to `src` and type `python -m pip install -e .` to install the *paleopy* library
6) navigate to the `notebooks` directory

### Notes (PICT refactoring, September 2022):

@TODO: 

#### circulation regimes: 

- [x] K2K (Kidson 2000)
- [x] Southwest Pacific Regimes (Lorrey and Fauchereau, 2017)
- [x] 9 AP NZ circulation regimes (Rampal, Lorrey and Fauchereau, 2022) 
- [/] Ross Sea Types (see CPP/indices/notebooks/Ross_Sea_WRs/notebooks)


#### datasets and variables for composites 

- [x] SSTa (ERSST v5b)

- [x] Berkeley Earth Temperatures (http://berkeleyearth.lbl.gov/auto/Global/Gridded/Land_and_Ocean_LatLong1.nc) 

- [x] VCSN, all daily variables (except wind)

  - [x] Rain_bc instead of Rain 
  - [x] Tmean (Norton) instead of regular Tmean 

- [x] AWAP (http://www.bom.gov.au/metadata/catalogue/19115/ANZCW0503900567) 

Note: not available yet, update in progress, but the *Australian Gridded Climate Data (AGCD) v1/ Australian Water Availability Project (AWAP)* dataset is available to 2019 at https://dapds00.nci.org.au/thredds/catalog/zv2/agcd/v1/catalog.html. It includes *tmin*, *tmax* and *precip*. 

- [x] GPCP precipitation

sourced from https://psl.noaa.gov/thredds/dodsC/Datasets/gpcp/precip.mon.mean.nc.html 

- [x] Monthly NCEP:

sourced from https://psl.noaa.gov/thredds/catalog/Datasets/catalog.html 

  - [x] MSLP: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived/surface/slp.mon.mean.nc.html 
  
  - [x] u-wind: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived/pressure/uwnd.mon.mean.nc.html 
  
  - [x] vector wind: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived/surface/slp.mon.mean.nc.html and https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived/pressure/vwnd.mon.mean.nc.html 

    in one dataset (NCEP1_monthly_wind_1948_2021.nc), levels 1000, 850, 200 

  - [x] HGT: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived/pressure/hgt.mon.mean.nc.html 

    levels: 1000, 850, 200 

  - [x] Omega: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived/pressure/omega.mon.mean.nc.html

    levels: 500 (variable name: 'omega_500')

  - [x] Mean Temperature (Tmean): https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived/surface/air.mon.mean.nc.html 
  
  - [x] Precipitable water: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived/surface/pr_wtr.eatm.mon.mean.nc.html
  
#### Climate Indices

- SAM
- SOI
- CEI 
- Nino 3.4 
- ZW3 * 
- PSA 
- IOD 

#### Features

- [x] Analog Selection, equal and inverse distance weighting
- [ ] Heatmaps for all CRs / synoptic types
- [x] Histogram outputs for all CRs / synoptic types
- [x] Ensemble Generation 
- [x] Climatology Periods
- [x] Detrended vs un-detrended
- [ ] version control and tracking of the proxy files

#### A maybe 

- widgets ?