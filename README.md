repository for the new paleopy library and the associated notebooks, allowing to run 'PICT' (Past Interpretation of Climate Tool") standalone in
a dedicated conda environment

## installation instructions:

1) clone the repository with git, or download the zip file (green `clone or download` button on the upper right of this repository), if downloading the ZIP file rename the folder created from `PICT_notebooks-master` to `PICT_notebooks`.
2) install the Anaconda python distribution from [https://www.anaconda.com/distribution/](https://www.anaconda.com/distribution/), choose the **Python 3.7** version, not the Python 2.7 version. 
3) in the `PICT_notebooks` directory, run at the command line (on a Mac, go to `Applications / Utilities / Terminal`):
	+ `conda env create -f MAC_PICT_environment.yml` on a Mac
	or
	+ `conda env create -f LINUX_PICT_environment.yml` on Linux
4) activate the `PICT_notebooks` environment by runnning `conda activate PICT_notebooks` at the command line, then run `jupyter notebook` or `jupyter lab`
5) navigate to the `notebooks` directory

### Notes (PICT refactoring, September 2022):

@TODO: 

#### circulation regimes: 

- K2K (Kidson 2000)
- Southwest Pacific Regimes (Lorrey and Fauchereau, 2017)
- 9 AP NZ circulation regimews (Rampal, Lorrey and Fauchereau, 2022) 
- Ross Sea Types (see CPP/indices/notebooks/Ross_Sea_WRs/notebooks)
- SH circulation 
- SSTa (ERSST v5b)

#### datasets and variables for composites 

- VCSN, all daily variables (except wind)

  - Rain_bc instead of Rain 
  - Tmean (Norton) instead of regular Tmean 

- AWAP (http://www.bom.gov.au/metadata/catalogue/19115/ANZCW0503900567) 

Note: not available yet, update in progress

- GPCP precipitation

sourced from https://psl.noaa.gov/thredds/dodsC/Datasets/gpcp/precip.mon.mean.nc.html 

- NCEP:

sourced from https://downloads.psl.noaa.gov/Datasets/ncep.reanalysis.derived/

  - MSLP: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived/surface/slp.mon.mean.nc.html 
  - u-wind: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived/pressure/uwnd.mon.mean.nc.html 
  - vector wind: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived/surface/slp.mon.mean.nc.html and https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived/pressure/vwnd.mon.mean.nc.html 
  - HGT ? if so: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived/pressure/hgt.mon.mean.nc.html 

#### Climate Indices

- SAM
- SOI
- CEI 
- Nino 3.4 
- ZW3 * 
- PSA 
- IOD 

#### Features

- Analog Selection, equal and inverse distance weighting
- Heatmaps for all CRs / synoptic types
- Histogram outputs for all CRs / synoptic types
- Ensemble Generation 
- Climatology Periods
- Detrended vs un-detrended
- version control and tracking of the proxy files

#### A maybe 

- widgets ?





