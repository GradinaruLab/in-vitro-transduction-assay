## Quantification Pipeline of Fluorescent Cells within in vitro images
This pipeline can be used to perform analysis and quantification on images of in vitro images to determine how many fluorescent cells are present as a fraction of the total number of cells stained with DAPI. The median brightness of those cells can subsequently be determined.

## Motivation
Quantification of in vitro transduction requires robust and reproducible pipelines. Due to significant variability in the DAPI signal in our images, a workflow to 
convert brightfield and signal images into masks was created. 

## Notebooks
There are three notebooks for this pipeline:
1. analysis_pipelien.ipynb runs the whole pipeline on a single image to allow examination of the results.
2. in_vitro_cell_segmentation.ipynb is where an image directory is run at scale, returning a dataframe and csv of the results.
3. figure_plotting.ipynb generates the plots for the figures, provided that the data files are provided. 

## Installation
To operate this code, first git and Anaconda should be installed to allow download of the repository and simple examination of the python notebooks. 

For Anaconda, go to the Anaconda distribution homepage and download Anaconda for Python 3.9 for the appropriate operating system. 

Enter the following into the command line:
conda update conda
conda update --all
conda install -c bokeh jupyter_bokeh opencv-python

The remaining dependencies should be installed with conda, but they are: pandas, numpy, json, scipy, scikit-image, glob2, tqdm, imagecodecs.

Next, download the package using the the clone function 

Then, setup the package by running `pip install -e .` in the directory containing `setup.py`. This will allow you to have an editable version of the code.

## Credits
David Goertsen wrote all of the code for this repository.

## License
GNU GENERAL PUBLIC LICENSE
