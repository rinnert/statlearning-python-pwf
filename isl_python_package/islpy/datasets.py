#    Datasets and helper functions for Introduction to Statistical Learning.
#
#    Copyright (C) 2019  Kurt Rinnert <kurt.rinnert@liverpool.ac.uk>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
import pandas as pd
import os

_datafile = os.path.join(os.path.dirname(__file__), 'isldata.h5')

def HDFFilePath():
    """
    Return path to HDF file containing all datasets.
    """
    return _datafile

_auto_ds = None
def Auto(force_reload=False):
    """
    Return data frame for Auto dataset.

	Description:
	
	     Gas mileage, horsepower and other information for cars.
	
	Format:
	
	     A data frame with 392 observations on the following 9 variables.
	
	     ‘mpg’ miles per gallon
	
	     ‘cylinders’ Number of cylinders between 4 and 8
	
	     ‘displacement’ Engine displacement (cu. inches)
	
	     ‘horsepower’ Engine horsepower
	
	     ‘weight’ Vehicle weight (lbs.)
	
	     ‘acceleration’ Time to accelerate from 0 to 60 mph (sec.)
	
	     ‘year’ Model year (modulo 100)
	
	     ‘origin’ Origin of car (1. American, 2. European, 3. Japanese)
	
	     ‘name’ Vehicle name
	
	     The orginal data contained 408 observations but 16 observations
	     with missing values were removed.
	
	Source:
	
	     This dataset was taken from the StatLib library which is
	     maintained at Carnegie Mellon University. The dataset was used in
	     the 1983 American Statistical Association Exposition.
	
	References:
	
	     James, G., Witten, D., Hastie, T., and Tibshirani, R. (2013) _An
	     Introduction to Statistical Learning with applications in R_,
	     <URL: www.StatLearning.com>, Springer-Verlag, New York
    """
    global _auto_ds
    if force_reload or _auto_ds is None:
        with pd.HDFStore(_datafile, 'r') as store:
            _auto_ds = store['Auto']
    return _auto_ds

_boston_ds = None
def Boston(force_reload=False):
    """
    Return data frame for Boston dataset.

	Description:
	
	     Housing values and other information about Boston suburbs.
	
	Format:
	
	     This data frame contains the following columns:
	
	     ‘crim’ per capita crime rate by town.
	
	     ‘zn’ proportion of residential land zoned for lots over 25,000
	          sq.ft.
	
	     ‘indus’ proportion of non-retail business acres per town.
	
	     ‘chas’ Charles River dummy variable (= 1 if tract bounds river; 0
	          otherwise).
	
	     ‘nox’ nitrogen oxides concentration (parts per 10 million).
	
	     ‘rm’ average number of rooms per dwelling.
	
	     ‘age’ proportion of owner-occupied units built prior to 1940.
	
	     ‘dis’ weighted mean of distances to five Boston employment
	          centres.
	
	     ‘rad’ index of accessibility to radial highways.
	
	     ‘tax’ full-value property-tax rate per \$10,000.
	
	     ‘ptratio’ pupil-teacher ratio by town.
	
	     ‘black’ 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by
	          town.
	
	     ‘lstat’ lower status of the population (percent).
	
	     ‘medv’ median value of owner-occupied homes in \$1000s.
	
	Source:
	
	     Harrison, D. and Rubinfeld, D.L. (1978) Hedonic prices and the
	     demand for clean air.  _J. Environ. Economics and Management_ *5*,
	     81-102.
	
	     Belsley D.A., Kuh, E.  and Welsch, R.E. (1980) _Regression
	     Diagnostics. Identifying Influential Data and Sources of
	     Collinearity._ New York: Wiley.
    """
    global _boston_ds
    if force_reload or _boston_ds is None:
        with pd.HDFStore(_datafile, 'r') as store:
            _boston_ds = store['Boston']
    return _boston_ds

_caravan_ds = None
def Caravan(force_reload=False):
    """
    Return data frame for Caravan dataset.

    Information about individuals offered caravan insurance.
    """
    global _caravan_ds
    if force_reload or _caravan_ds is None:
        with pd.HDFStore(_datafile, 'r') as store:
            _caravan_ds = store['Caravan']
    return _caravan_ds

_carseats_ds = None
def Carseats(force_reload=False):
    """
    Return data frame for Carseats dataset.

    Information about carseat sales in 400 stores.
    """
    global _carseats_ds
    if force_reload or _carseats_ds is None:
        with pd.HDFStore(_datafile, 'r') as store:
            _carseats_ds = store['Carseats']
    return _carseats_ds

_college_ds = None
def College(force_reload=False):
    """
    Return data frame for College dataset.

    Demographic characteristics, tuition, and more for USA colleges.
    """
    global _college_ds
    if force_reload or _college_ds is None:
        with pd.HDFStore(_datafile, 'r') as store:
            _college_ds = store['College']
    return _college_ds

_default_ds = None
def Default(force_reload=False):
    """
    Return data frame for Default dataset.

    Customer default records for a credit card company.
    """
    global _default_ds
    if force_reload or _default_ds is None:
        with pd.HDFStore(_datafile, 'r') as store:
            _default_ds = store['Default']
    return _default_ds

_hitters_ds = None
def Hitters(force_reload=False):
    """
    Return data frame for Hitters dataset.

    Records and salaries for baseball players.
    """
    global _hitters_ds
    if force_reload or _hitters_ds is None:
        with pd.HDFStore(_datafile, 'r') as store:
            _hitters_ds = store['Hitters']
    return _hitters_ds

_khan_ds = None
def Khan(force_reload=False):
    """
    Return data frame for Khan dataset.

    Gene expression measurements for four cancer types.
    """
    global _khan_ds
    if force_reload or _khan_ds is None:
        with pd.HDFStore(_datafile, 'r') as store:
            _khan_ds = store['Khan']
    return _khan_ds

_nci60_ds = None
def NCI60(force_reload=False):
    """
    Return data frame for NCI60 dataset.

    Gene expression measurements for 64 cancer types.
    """
    global _nci60_ds
    if force_reload or _nci60_ds is None:
        with pd.HDFStore(_datafile, 'r') as store:
            _nci60_ds = store['NCI60']
    return _nci60_ds

_oj_ds = None
def OJ(force_reload=False):
    """
    Return data frame for OJ dataset.

    Sales information for Citrus Hill and Minute Maid orange juice.
    """
    global _oj_ds
    if force_reload or _oj_ds is None:
        with pd.HDFStore(_datafile, 'r') as store:
            _oj_ds = store['OJ']
    return _oj_ds

_portfolio_ds = None
def Portfolio(force_reload=False):
    """
    Return data frame for Portfolio dataset.

    Past values of finacial assets, for use in porfolio allocation.
    """
    global _portfolio_ds
    if force_reload or _portfolio_ds is None:
        with pd.HDFStore(_datafile, 'r') as store:
            _portfolio_ds = store['Portfolio']
    return _portfolio_ds

_smarket_ds = None
def Smarket(force_reload=False):
    """
    Return data frame for Smarket dataset.

    Daily percentage returns for S&P 500 over a 5-year period.
    """
    global _smarket_ds
    if force_reload or _smarket_ds is None:
        with pd.HDFStore(_datafile, 'r') as store:
            _smarket_ds = store['Smarket']
    return _smarket_ds

_usarrests_ds = None
def USArrests(force_reload=False):
    """
    Return data frame for USArrests dataset.

    Crime statistics per 100,000 residents in 50 states of the USA.
    """
    global _usarrests_ds
    if force_reload or _usarrests_ds is None:
        with pd.HDFStore(_datafile, 'r') as store:
            _usarrests_ds = store['USArrests']
    return _usarrests_ds

_wage_ds = None
def Wage(force_reload=False):
    """
    Return data frame for Wage dataset.

    Income survey data for males in the central Atlantic region of the USA.
    """
    global _wage_ds
    if force_reload or _wage_ds is None:
        with pd.HDFStore(_datafile, 'r') as store:
            _wage_ds = store['Wage']
    return _wage_ds

_weekly_ds = None
def Weekly(force_reload=False):
    """
    Return data frame for Weekly dataset.

    1,089 weekly stock market returns for a period of 21 years.
    """
    global _weekly_ds
    if force_reload or _weekly_ds is None:
        with pd.HDFStore(_datafile, 'r') as store:
            _weekly_ds = store['Weekly']
    return _weekly_ds

_digit_train_ds, _digit_test_ds = None, None
def Digits(force_reload=False):
    """
    Return tuple of training and test data frames for Digits dataset.

    Normalized handwritten digits, automatically scanned from envelopes by the
    U.S. Postal Service. The original scanned digits are binary and of
    different sizes and orientations; the images  here have been deslanted and
    size normalized, resulting in 16 x 16 grayscale images (Le Cun et al.,
    1990).
    
    The data are returnd as two data frames and each row consists of the digit
    id (0-9) followed by the 256 grayscale values.
    
    There are 7291 training observations and 2007 test observations,
    distributed as follows:
             0    1   2   3   4   5   6   7   8   9 Total
    Train 1194 1005 731 658 652 556 664 645 542 644 7291
     Test  359  264 198 166 200 160 170 147 166 177 2007
    
    or as proportions:
             0    1   2    3    4    5    6    7    8    9 
    Train 0.16 0.14 0.1 0.09 0.09 0.08 0.09 0.09 0.07 0.09
     Test 0.18 0.13 0.1 0.08 0.10 0.08 0.08 0.07 0.08 0.09

    The test set is notoriously "difficult", and a 2.5% error rate is
    excellent. These data were kindly made available by the neural network
    group at AT&T research labs (thanks to Yann Le Cunn).

    """
    global _digit_train_ds, _digit_test_ds
    if force_reload or _digit_train_ds is None:
        with pd.HDFStore(_datafile, 'r') as store:
            _digit_train_ds, _digit_test_ds = store['DigitsTrain'], store['DigitsTest']
    return _digit_train_ds, _digit_test_ds

