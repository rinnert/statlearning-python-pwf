# ISLPy Library

## Introduction

This library provides the datasets and some helper functions for 
a Python version of the labs and exercises of "Introduction to Statistical Learning with applications in R" (ISLR). Some of the datasets are downloaded from the [book's website](www.statlearning.com), others are extracted
from the default `R` distribution and the `R` `MASS` and `ISLR` libraries.

## Installation

Build the wheel with `make` and then

```bash
pip install dist/islpy-0.3-py3-none-any.whl
```

Note: the version number might be different.

## Data Set Access

To access the datasets you will need to `import` the `dataset` module:

```python
from islpy import datasets
```

Use the `help` function to get documentation about the available datasets:

```python
help(datasets)
```

To retrieve a pandas data frame for a dataset simply call the corresponding function, for example:

```python
df = datasets.Boston()
```

Behind the scenes all datasets are stored in a single HDF file. Datasets are only loaded into memory when the corresponding functions are called. By default the `datasets` module caches the data frames. That is, a second call to a dataset retrieval function returns the same object as the first call (which you might have modified!). You can override this behaviour with the `force_reload` parameter:

```python
df = datasets.Khan(force_reload=True)
```

## R-style Plots for Linear Models

The `lmplots` module provides R-style summary plots for linear models from the `statsmodels` library, for example:

```python
import statsmodels.formula.api as smf
from islpy import datasets, lmplots

auto = datasets.Auto()
lm = smf.ols('mpg~horsepower+acceleration', auto).fit()
lmplots.plot(lm)
```

## Utilities
Some useful wrapper functions and utilities are provided by the `utils` module:

```python
from islpy import utils

help(utils)
```
