# Introduction to Statistical Learning 

## (With Applications in Python)

### *For ICTP Physics Without Frontiers*

## Description

This repository provides resources for a course based on ["Introduction to Statistical Learning with applications in R"](http://faculty.marshall.usc.edu/gareth-james/ISL/).

<center><img src="lectures/figs/intro/isl_cover.jpg" alt="ISLR" width="320"/></center>

The R labs and exercises are replaced by Python labs and exercises.

The course is designed for the [ICTP Physics Without Frontiers](https://www.ictp.it/physics-without-frontiers.aspx) programme. 

<center><img src="lectures/figs/common/ICTP-logo-full-trans.png" alt="ISLR" width="320"/></center>

## Project Structure

  - `lectures/slides/` contains the lecture slides in PDF format.
  - `lectures/latex/` contains the LaTeX/Beamer sources for the slides.
  - `islpy_python_package/` provides a Python library needed for the labs and exercises (provides data sets and utilities).
  - `themes/` contains some CSS/JS hacks for consistent look & feel in jupyter notebooks.
  - `notebooks/` contains jupyter notebooks for labs and exercises
  - `datasets/` contains the data sets in CSV format (also available via the islpy Python library).


## Requirements

The jupyter notebooks for the labs and exercises require a Python >= 3.6 installation with the usual suspects for statistical/machine learning.

  - `numpy`
  - `pandas`, `hdf5`, `pytables`
  - `matplotplib`
  - `seaborn`
  - `statsmodels`
  - `patsy`
  - `scikit-learn`
  - `torch`
  - `jupyter`

We highly recommend an [`conda`](https://conda.io/en/latest/) or [`miniconda`](https://docs.conda.io/en/latest/miniconda.html) installation for this.

In addition, the `islpy` library provided by this project is required (see `islpy_python_package/` sub-directory).

The exercises require some jupyter extensions to behave properly, in particular the *exercise2* and *freeze* extensions. These are provided by the `jupyter_contrib_nbextensions` package:

```bash
conda install -c conda-forge jupyter_contrib_nbextensions

```

Then restart your jupyter server and activate the relevant extensions from the extensions tab of the launch page (you might have to untick the "check compatibility" check box).

We recommend to install the extensions in your user space and then install the CSS/JS patches from the `themes/` sub-directory of this project:

```bash
jupyter contrib nbextension install --user
```

If you get warnings about duplicate files when starting jupyter, you might have to do:
```bash
jupyter contrib nbextension uninstall --sys-prefix
```

Then follow the instructions in the README files under `themes/` and restart your jupyter server (the instructions assume you are running a modern Linux distribution).