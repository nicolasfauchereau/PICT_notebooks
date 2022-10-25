import numpy as np
from numpy import ma
from matplotlib import pyplot as plt
import xarray as xr
from cartopy import crs as ccrs
from cartopy.util import add_cyclic_point
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import palettable
import cmocean

class scalar_plot:
    """
    scalar plot accepts a `analogs` object and implements
    methods to plot a scalar plot on a map
    """
    def __init__(self, analogs, center=None, robust=True, robust_percentile=1.0, \
              vmin=None, vmax=None, cmap=None, grid=True, domain=None, proj=None, res='c', test=0.05, border=True, proxies_loc=False):

        self.analogs = analogs
        self.domain = domain
        self.center = center
        self.robust = robust
        self.robust_percentile = robust_percentile
        self.vmin = vmin
        self.vmax = vmax
        self.cmap = cmap
        self.grid = grid
        self.domain = domain
        self.proj = proj
        self.res = res
        self.test = test
        self.border = border
        self.proxies_loc = proxies_loc

    def _get_domain(self):

        if self.domain is not None:
            domain_dset = self.analogs.dset_dict['domain']
            if ( (self.domain[0] < domain_dset[0]) | (self.domain[1] > domain_dset[1])  \
                | (self.domain[2] < domain_dset[2]) | (self.domain[3] > domain_dset[3]) ):
                print("""ERROR! the domain for the analog site is partly outside the limits of the dataset""")
                raise Exception("DOMAIN ERROR")

            else:
                # checks whether the first latitude is the northermost or southermost latitude
                latstart = self.analogs.dset['latitudes'].data[0]
                latend  = self.analogs.dset['latitudes'].data[-1]
                # if first latitude northermost, reverse the order of the domain selection
                if latstart > latend:
                    dset_domain = self.analogs.dset.sortby('latitudes')
                # if not, go ahead with the domain limits as they are provided
                else:
                    dset_domain = self.analogs.dset.sel(latitudes=slice(self.domain[2], self.domain[3]), \
                                                   longitudes=slice(self.domain[0], self.domain[1]))
            self.dset_domain = dset_domain
        else:
            self.dset_domain = self.analogs.dset
            self.domain = [self.analogs.dset['longitudes'].data.min(), \
                self.analogs.dset['longitudes'].data.max(), \
                    self.analogs.dset['latitudes'].data.min(), \
                        self.analogs.dset['latitudes'].data.max()]
        return self

    def _get_plots_params(self, data):
        """
        data can be either the data array attached to:

        + self.analogs.dset['composite_anomalies']

        or one of the data arrays attached to

        + self.analogs.dset['composite_sample']
        """

        # ravel and removes nans for calculation of intervals etc
        calc_data = np.ravel(data[np.isfinite(data)])

        # the following is borrowed from xr
        # see: plot.py in xr/xr/plot
        if self.vmin is None:
            self.vmin = np.percentile(calc_data, self.robust_percentile) if self.robust else calc_data.min()
        if self.vmax is None:
            self.vmax = np.percentile(calc_data, 100 - self.robust_percentile) if self.robust else calc_data.max()

        del(calc_data)

        # Simple heuristics for whether these data should  have a divergent map
        divergent = ((self.vmin < 0) and (self.vmax > 0)) or self.center is not None

        # Now set center to 0 so math below makes sense
        if self.center is None:
            self.center = 0

        # A divergent map should be symmetric around the center value
        if divergent:
            vlim = max(abs(self.vmin - self.center), abs(self.vmax - self.center))
            self.vmin, self.vmax = -vlim, vlim

        # Now add in the centering value and set the limits
        self.vmin += self.center
        self.vmax += self.center

        # Choose default colormaps if not provided
        if self.cmap is None:
            if divergent:
                # get the colormap defined in the dset_dict
                self.cmap = eval(self.analogs.dset_dict['plot']['cmap'])
            else:
                # get the default matplotlib colormap
                self.cmap = plt.get_cmap()

        return self

    def _get_ccrs(self):
            """
            given the projection and the domain, returns
            the cartopy projection of the map (the data projection, i.e.
            the 'transform' argument, is always assumed to be
            ccrs.PlateCarree(central_longitude=0))
            """

            if not(self.proj):
                self.proj = 'cyl'
                self.crs = ccrs.PlateCarree(central_longitude=0)

            if self.proj in ['cyl', 'merc']:
                self.crs = ccrs.PlateCarree(central_longitude=180)

            if self.proj == 'moll':
                self.crs = ccrs.Mollweide(central_longitude=180)

            if self.proj == 'spstere':
                self.crs = ccrs.SouthPolarStereo(central_longitude=180)

            if self.proj == 'npstere':
                self.crs = ccrs.NorthPolarStereo(central_longitude=180)

            return self

    def _wrap_longitudes(self, data_array):

        lat = data_array.coords['latitudes']
        lon = data_array.coords['longitudes']

        data = data_array.data

        wrap_data, wrap_lon = add_cyclic_point(data, coord=lon)

        data_array = xr.DataArray(wrap_data, dims=('latitudes','longitudes'), coords=[lat, wrap_lon])

        return data_array

    def plot(self, subplots=False, domain=None, wrap_longitudes=False, res='low'):
        """
        cartopy plot of a scalar quantity
        """

        if not hasattr(self, 'crs'):
            self._get_ccrs()

        if not hasattr(self, 'dset_domain'):
            self._get_domain()

        mat = self.dset_domain['composite_anomalies']
        pvalues = self.dset_domain['pvalues']

        # get the plot params from the composite anomalies data
        self._get_plots_params(mat.data)

        cmap = eval(self.analogs.dset_dict['plot']['cmap'])
        units = self.analogs.dset_dict['units']

        # if the domain is global, we wrap the longitudes
        if wrap_longitudes:
            mat = self._wrap_longitudes(mat)
            pvalues = self._wrap_longitudes(pvalues)

        r, c = mat.shape

        f, ax = plt.subplots(figsize=(5*(c/r), 5), dpi=200, subplot_kw={'projection':self.crs})

        if self.proj == 'spstere':
            mat = mat.sel(latitudes=slice(-90, 0))
            pvalues = pvalues.sel(latitudes=slice(-90, 0))
        elif self.proj == 'npstere':
            mat = mat.sel(latitudes=slice(0, 90))
            pvalues = pvalues.sel(latitudes=slice(0, 90))

        mat.plot.contourf(ax=ax, levels=20, cmap=cmap, transform=ccrs.PlateCarree(), \
            cbar_kwargs={'shrink':0.7, 'label':units})

        # if test is defined, one contours the p-values for that level
        if self.test:
            pvalues_mask = pvalues.where(pvalues <= self.test)
            pvalues_mask.plot.contourf(transform=ccrs.PlateCarree(), levels=2, colors="None", hatches=["..."], add_colorbar=False)
            # pvalues.plot.contour(levels = [self.test], colors='#8C001A', linewidths=1.5, transform=ccrs.PlateCarree())

        # draw the coastlines, if the domain is global we use the 50 minutes resolution coastlines
        # dataset, and if not (res = 'high') we use the 10 minutes resolution (slower)

        # we also adjust the gridlines according to the resolution
        if res in ['low','l']:

            ax.coastlines(resolution='50m', linewidth=0.5)

            if self.proj not in ['spstere','npstere']:

                xticks = np.arange(0, 400., 40)

                yticks = np.arange(-80., 100., 20.)

                gl = ax.gridlines(draw_labels=False, linewidth=0.5, linestyle='--', xlocs=xticks, ylocs=yticks, crs=ccrs.PlateCarree())

                ax.set_xticks(xticks, crs=ccrs.PlateCarree())

                ax.set_yticks(yticks, crs=ccrs.PlateCarree())

                lon_formatter = LongitudeFormatter(zero_direction_label=True, dateline_direction_label=True)

                lat_formatter = LatitudeFormatter()

                ax.xaxis.set_major_formatter(lon_formatter)

                ax.yaxis.set_major_formatter(lat_formatter)

                gl.top_labels = False
                gl.right_labels = False

                ax.set_ylabel('latitudes (degrees north)')
                ax.set_xlabel('longitudes (degrees east)')

        elif res in ['high','h']:

            ax.coastlines(resolution='10m', linewidth=0.5)

            if self.proj not in ['spstere','npstere']:

                xticks = np.arange(0, 365., 5)

                yticks = np.arange(-80., 85., 5.)

                gl = ax.gridlines(draw_labels=False, linewidth=0.5, linestyle='--', xlocs=xticks, ylocs=yticks, crs=ccrs.PlateCarree())

                ax.set_xticks(xticks, crs=ccrs.PlateCarree())

                ax.set_yticks(yticks, crs=ccrs.PlateCarree())

                lon_formatter = LongitudeFormatter(zero_direction_label=True, dateline_direction_label=True)

                lat_formatter = LatitudeFormatter()

                ax.xaxis.set_major_formatter(lon_formatter)

                ax.yaxis.set_major_formatter(lat_formatter)

                gl.top_labels = False
                gl.right_labels = False

                ax.set_ylabel('latitudes (degrees north)')
                ax.set_xlabel('longitudes (degrees east)')

        elif res in ['full', 'f']:

            ax.coastlines(resolution='10m', linewidth=0.5)

            if self.proj not in ['spstere','npstere']:

                xticks = np.arange(self.domain[0], self.domain[1] + 3, 3)

                yticks = np.arange(self.domain[2], self.domain[3] + 3, 3)

                gl = ax.gridlines(draw_labels=False, linewidth=0.5, linestyle='--', xlocs=xticks, ylocs=yticks, crs=ccrs.PlateCarree())

                ax.set_xticks(xticks, crs=ccrs.PlateCarree())

                ax.set_yticks(yticks, crs=ccrs.PlateCarree())

                lon_formatter = LongitudeFormatter(zero_direction_label=True, dateline_direction_label=True)

                lat_formatter = LatitudeFormatter()

                ax.xaxis.set_major_formatter(lon_formatter)

                ax.yaxis.set_major_formatter(lat_formatter)

                gl.top_labels = False
                gl.right_labels = False

                ax.set_ylabel('latitudes (degrees north)')
                ax.set_xlabel('longitudes (degrees east)')

        else:

            print('resolution invalid, got {}, expect `low, l, high, h or full, f`'.format(res))

        # set the title from the description in the dataset + variable JSON entry
        ax.set_title(self.analogs.dset_dict['description'], fontsize=14)

        if self.proj not in ['spstere', 'npstere']:
            ax.set_extent(self.domain, crs=ccrs.PlateCarree(central_longitude=0))

        if self.proj in ['spstere', 'npstere']:
            import matplotlib.path as mpath
            # Compute a circle in axes coordinates, which we can use as a boundary
            # for the map. We can pan/zoom as much as we like - the boundary will be
            # permanently circular.
            theta = np.linspace(0, 2*np.pi, 100)
            center, radius = [0.5, 0.5], 0.5
            verts = np.vstack([np.sin(theta), np.cos(theta)]).T
            circle = mpath.Path(verts * radius + center)

            ax.set_boundary(circle, transform=ax.transAxes)

        # proxies_loc is True, we plot the proxies locations on the map
        if self.proxies_loc:
            locs = self.analogs.locations
            for k in locs.keys():
                lon, lat = locs[k]
                ax.plot(lon, lat, marker='o', color='w', markersize=7, transform=ccrs.PlateCarree())
                ax.plot(lon, lat, marker='*', color='k', markersize=6, transform=ccrs.PlateCarree())

        return f, ax

        self.dset_domain.close()

        plt.close(f)
