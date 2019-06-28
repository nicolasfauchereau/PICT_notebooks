repository for the new paleopy library and the associated notebooks, allowing to run 'PICT' (Past Interpretation of Climate Tool") standalone in
a dedicated conda environment

## installation instructions:

1) clone the repository with git, or download the zip file
2) install the Anaconda python distribution from [https://www.anaconda.com/distribution/](https://www.anaconda.com/distribution/), choose the **Python 3.7** version, not the Python 2.7 version. 
3) in the repository directory, run at the command line (on a Mac, go to `Applications/Utilities/Terminal`):
	+ `conda env create -f MAC_PICT_environment.yml` on a Mac
	or
	+ `conda env create -f LINUX_PICT_environment.yml` on Linux
4) activate the `PICT_notebooks` environment by runnning `conda activate PICT_notebooks` at the command line, then run `jupyter notebook` or `jupyter lab`
5) navigate to the `notebooks` directory
