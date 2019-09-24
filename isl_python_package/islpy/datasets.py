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

    Description:
    
         The data contains 5822 real customer records. Each record consists
         of 86 variables, containing sociodemographic data (variables 1-43)
         and product ownership (variables 44-86). The sociodemographic data
         is derived from zip codes. All customers living in areas with the
         same zip code have the same sociodemographic attributes. Variable
         86 (‘Purchase’) indicates whether the customer purchased a caravan
         insurance policy. Further information on the individual variables
         can be obtained at
         http://www.liacs.nl/~putten/library/cc2000/data.html
    
    Format:
    
         A data frame with 5822 observations on 86 variables.
    
    Source:
    
         The data was originally supplied by Sentient Machine Research and
         was used in the CoIL Challenge 2000.
    
    References:
    
         P. van der Putten and M. van Someren (eds) . CoIL Challenge 2000:
         The Insurance Company Case.  Published by Sentient Machine
         Research, Amsterdam. Also a Leiden Institute of Advanced Computer
         Science Technical Report 2000-09. June 22, 2000. See
         http://www.liacs.nl/~putten/library/cc2000/
         P. van der Putten and M. van Someren. A Bias-Variance Analysis of
         a Real World Learning Problem: The CoIL Challenge 2000. Machine
         Learning, October 2004, vol. 57, iss. 1-2, pp. 177-195, Kluwer
         Academic Publishers
         James, G., Witten, D., Hastie, T., and Tibshirani, R. (2013) _An
         Introduction to Statistical Learning with applications in R_,
         <URL: www.StatLearning.com>, Springer-Verlag, New York
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

    Description:
    
         A simulated data set containing sales of child car seats at 400
         different stores.
    
    Format:
    
         A data frame with 400 observations on the following 11 variables.
    
         ‘Sales’ Unit sales (in thousands) at each location
    
         ‘CompPrice’ Price charged by competitor at each location
    
         ‘Income’ Community income level (in thousands of dollars)
    
         ‘Advertising’ Local advertising budget for company at each
              location (in thousands of dollars)
    
         ‘Population’ Population size in region (in thousands)
    
         ‘Price’ Price company charges for car seats at each site
    
         ‘ShelveLoc’ A factor with levels ‘Bad’, ‘Good’ and ‘Medium’
              indicating the quality of the shelving location for the car
              seats at each site
    
         ‘Age’ Average age of the local population
    
         ‘Education’ Education level at each location
    
         ‘Urban’ A factor with levels ‘No’ and ‘Yes’ to indicate whether
              the store is in an urban or rural location
    
         ‘US’ A factor with levels ‘No’ and ‘Yes’ to indicate whether the
              store is in the US or not
    
    Source:
    
         Simulated data
    
    Rferences:
    
         James, G., Witten, D., Hastie, T., and Tibshirani, R. (2013) _An
         Introduction to Statistical Learning with applications in R_,
         <URL: www.StatLearning.com>, Springer-Verlag, New York
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

    Description:
    
         Statistics for a large number of US Colleges from the 1995 issue
         of US News and World Report.
    
    Format:
    
         A data frame with 777 observations on the following 18 variables.
    
         ‘Private’ A factor with levels ‘No’ and ‘Yes’ indicating private
              or public university
    
         ‘Apps’ Number of applications received
    
         ‘Accept’ Number of applications accepted
    
         ‘Enroll’ Number of new students enrolled
    
         ‘Top10perc’ Pct. new students from top 10% of H.S. class
    
         ‘Top25perc’ Pct. new students from top 25% of H.S. class
    
         ‘F.Undergrad’ Number of fulltime undergraduates
    
         ‘P.Undergrad’ Number of parttime undergraduates
    
         ‘Outstate’ Out-of-state tuition
    
         ‘Room.Board’ Room and board costs
    
         ‘Books’ Estimated book costs
    
         ‘Personal’ Estimated personal spending
    
         ‘PhD’ Pct. of faculty with Ph.D.'s
    
         ‘Terminal’ Pct. of faculty with terminal degree
    
         ‘S.F.Ratio’ Student/faculty ratio
    
         ‘perc.alumni’ Pct. alumni who donate
    
         ‘Expend’ Instructional expenditure per student
    
         ‘Grad.Rate’ Graduation rate
    
    Source:
    
         This dataset was taken from the StatLib library which is
         maintained at Carnegie Mellon University. The dataset was used in
         the ASA Statistical Graphics Section's 1995 Data Analysis
         Exposition.
    
    References:
    
         James, G., Witten, D., Hastie, T., and Tibshirani, R. (2013) _An
         Introduction to Statistical Learning with applications in R_,
         <URL: www.StatLearning.com>, Springer-Verlag, New York
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

    Description:
    
         A simulated data set containing information on ten thousand
         customers. The aim here is to predict which customers will default
         on their credit card debt.
    
    Format:
    
         A data frame with 10000 observations on the following 4 variables.
    
         ‘default’ A factor with levels ‘No’ and ‘Yes’ indicating whether
              the customer defaulted on their debt
    
         ‘student’ A factor with levels ‘No’ and ‘Yes’ indicating whether
              the customer is a student
    
         ‘balance’ The average balance that the customer has remaining on
              their credit card after making their monthly payment
    
         ‘income’ Income of customer
    
    Source:
    
         Simulated data
    
    References:
    
         James, G., Witten, D., Hastie, T., and Tibshirani, R. (2013) _An
         Introduction to Statistical Learning with applications in R_,
         <URL: www.StatLearning.com>, Springer-Verlag, New York
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

    Description:
    
         Major League Baseball Data from the 1986 and 1987 seasons.
    
    Format:
    
         A data frame with 322 observations of major league players on the
         following 20 variables.
    
         ‘AtBat’ Number of times at bat in 1986
    
         ‘Hits’ Number of hits in 1986
    
         ‘HmRun’ Number of home runs in 1986
    
         ‘Runs’ Number of runs in 1986
    
         ‘RBI’ Number of runs batted in in 1986
    
         ‘Walks’ Number of walks in 1986
    
         ‘Years’ Number of years in the major leagues
    
         ‘CAtBat’ Number of times at bat during his career
    
         ‘CHits’ Number of hits during his career
    
         ‘CHmRun’ Number of home runs during his career
    
         ‘CRuns’ Number of runs during his career
    
         ‘CRBI’ Number of runs batted in during his career
    
         ‘CWalks’ Number of walks during his career
    
         ‘League’ A factor with levels ‘A’ and ‘N’ indicating player's
              league at the end of 1986
    
         ‘Division’ A factor with levels ‘E’ and ‘W’ indicating player's
              division at the end of 1986
    
         ‘PutOuts’ Number of put outs in 1986
    
         ‘Assists’ Number of assists in 1986
    
         ‘Errors’ Number of errors in 1986
    
         ‘Salary’ 1987 annual salary on opening day in thousands of dollars
    
         ‘NewLeague’ A factor with levels ‘A’ and ‘N’ indicating player's
              league at the beginning of 1987
    
    Source:
    
         This dataset was taken from the StatLib library which is
         maintained at Carnegie Mellon University. This is part of the data
         that was used in the 1988 ASA Graphics Section Poster Session. The
         salary data were originally from Sports Illustrated, April 20,
         1987. The 1986 and career statistics were obtained from The 1987
         Baseball Encyclopedia Update published by Collier Books, Macmillan
         Publishing Company, New York.
    
    References:
    
         James, G., Witten, D., Hastie, T., and Tibshirani, R. (2013) _An
         Introduction to Statistical Learning with applications in R_,
         <URL: www.StatLearning.com>, Springer-Verlag, New York
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

    Description:
    
         The data contains 1070 purchases where the customer either
         purchased Citrus Hill or Minute Maid Orange Juice. A number of
         characteristics of the customer and product are recorded.
    
    Format:
    
         A data frame with 1070 observations on the following 18 variables.
    
         ‘Purchase’ A factor with levels ‘CH’ and ‘MM’ indicating whether
              the customer purchased Citrus Hill or Minute Maid Orange
              Juice
    
         ‘WeekofPurchase’ Week of purchase
    
         ‘StoreID’ Store ID
    
         ‘PriceCH’ Price charged for CH
    
         ‘PriceMM’ Price charged for MM
    
         ‘DiscCH’ Discount offered for CH
    
         ‘DiscMM’ Discount offered for MM
    
         ‘SpecialCH’ Indicator of special on CH
    
         ‘SpecialMM’ Indicator of special on MM
    
         ‘LoyalCH’ Customer brand loyalty for CH
    
         ‘SalePriceMM’ Sale price for MM
    
         ‘SalePriceCH’ Sale price for CH
    
         ‘PriceDiff’ Sale price of MM less sale price of CH
    
         ‘Store7’ A factor with levels ‘No’ and ‘Yes’ indicating whether
              the sale is at Store 7
    
         ‘PctDiscMM’ Percentage discount for MM
    
         ‘PctDiscCH’ Percentage discount for CH
    
         ‘ListPriceDiff’ List price of MM less list price of CH
    
         ‘STORE’ Which of 5 possible stores the sale occured at
    
    Source:
    
         Stine, Robert A., Foster, Dean P., Waterman, Richard P. Business
         Analysis Using Regression (1998). Published by Springer.
    
    References:
    
         James, G., Witten, D., Hastie, T., and Tibshirani, R. (2013) _An
         Introduction to Statistical Learning with applications in R_,
         <URL: www.StatLearning.com>, Springer-Verlag, New York
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

    Description:
    
         A simple simulated data set containing 100 returns for each of two
         assets, X and Y. The data is used to estimate the optimal fraction
         to invest in each asset to minimize investment risk of the
         combined portfolio. One can then use the Bootstrap to estimate the
         standard error of this estimate.
    
    Usage:
    
         Portfolio
         
    Format:
    
         A data frame with 100 observations on the following 2 variables.
    
         ‘X’ Returns for Asset X
    
         ‘Y’ Returns for Asset Y
    
    Source:
    
         Simulated data
    
    References:
    
         James, G., Witten, D., Hastie, T., and Tibshirani, R. (2013) _An
         Introduction to Statistical Learning with applications in R_,
         <URL: www.StatLearning.com>, Springer-Verlag, New York
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

    Description:
    
        Daily percentage returns for the S&P 500 stock index between 2001
        and 2005.
    
    Format:
    
         A data frame with 1250 observations on the following 9 variables.
    
         ‘Year’ The year that the observation was recorded
    
         ‘Lag1’ Percentage return for previous day
    
         ‘Lag2’ Percentage return for 2 days previous
    
         ‘Lag3’ Percentage return for 3 days previous
    
         ‘Lag4’ Percentage return for 4 days previous
    
         ‘Lag5’ Percentage return for 5 days previous
    
         ‘Volume’ Volume of shares traded (number of daily shares traded in
              billions)
    
         ‘Today’ Percentage return for today
    
         ‘Direction’ A factor with levels ‘Down’ and ‘Up’ indicating
              whether the market had a positive or negative return on a
              given day
    
    Source:
    
         Raw values of the S&P 500 were obtained from Yahoo Finance and
         then converted to percentages and lagged.
    
    References:
    
         James, G., Witten, D., Hastie, T., and Tibshirani, R. (2013) _An
         Introduction to Statistical Learning with applications in R_,
         <URL: www.StatLearning.com>, Springer-Verlag, New York
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

    Description:
    
         This data set contains statistics, in arrests per 100,000
         residents for assault, murder, and rape in each of the 50 US
         states in 1973.  Also given is the percent of the population
         living in urban areas.
    
    Format:
    
         A data frame with 50 observations on 4 variables.
    
           [,1]  Murder    numeric  Murder arrests (per 100,000)  
           [,2]  Assault   numeric  Assault arrests (per 100,000) 
           [,3]  UrbanPop  numeric  Percent urban population      
           [,4]  Rape      numeric  Rape arrests (per 100,000)    
          
    Source:
    
         World Almanac and Book of facts 1975.  (Crime rates).
    
         Statistical Abstracts of the United States 1975.  (Urban rates).
    
    References:
    
         McNeil, D. R. (1977) _Interactive Data Analysis_.  New York:
         Wiley.
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

    Description:
    
         Wage and other data for a group of 3000 male workers in the
         Mid-Atlantic region.
    
    Format:
    
         A data frame with 3000 observations on the following 11 variables.
    
         ‘year’ Year that wage information was recorded
    
         ‘age’ Age of worker
    
         ‘maritl’ A factor with levels ‘1. Never Married’ ‘2. Married’ ‘3.
              Widowed’ ‘4. Divorced’ and ‘5. Separated’ indicating marital
              status
    
         ‘race’ A factor with levels ‘1. White’ ‘2. Black’ ‘3. Asian’ and
              ‘4. Other’ indicating race
    
         ‘education’ A factor with levels ‘1. < HS Grad’ ‘2. HS Grad’ ‘3.
              Some College’ ‘4. College Grad’ and ‘5. Advanced Degree’
              indicating education level
    
         ‘region’ Region of the country (mid-atlantic only)
    
         ‘jobclass’ A factor with levels ‘1. Industrial’ and ‘2.
              Information’ indicating type of job
    
         ‘health’ A factor with levels ‘1. <=Good’ and ‘2. >=Very Good’
              indicating health level of worker
    
         ‘health_ins’ A factor with levels ‘1. Yes’ and ‘2. No’ indicating
              whether worker has health insurance
    
         ‘logwage’ Log of workers wage
    
         ‘wage’ Workers raw wage
    
    Source:
    
         Data was manually assembled by Steve Miller, of Open BI
         (www.openbi.com), from the March 2011 Supplement to Current
         Population Survey data.
    
         <URL: http://thedataweb.rm.census.gov/TheDataWeb>
    
    References:
    
         James, G., Witten, D., Hastie, T., and Tibshirani, R. (2013) _An
         Introduction to Statistical Learning with applications in R_,
         <URL: www.StatLearning.com>, Springer-Verlag, New York
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

    Description:
    
         Weekly percentage returns for the S&P 500 stock index between 1990
         and 2010.
    
    Format:
    
         A data frame with 1089 observations on the following 9 variables.
    
         ‘Year’ The year that the observation was recorded
    
         ‘Lag1’ Percentage return for previous week
    
         ‘Lag2’ Percentage return for 2 weeks previous
    
         ‘Lag3’ Percentage return for 3 weeks previous
    
         ‘Lag4’ Percentage return for 4 weeks previous
    
         ‘Lag5’ Percentage return for 5 weeks previous
    
         ‘Volume’ Volume of shares traded (average number of daily shares
              traded in billions)
    
         ‘Today’ Percentage return for this week
    
         ‘Direction’ A factor with levels ‘Down’ and ‘Up’ indicating
              whether the market had a positive or negative return on a
              given week
    
    Source:
    
         Raw values of the S&P 500 were obtained from Yahoo Finance and
         then converted to percentages and lagged.
    
    References:
    
         James, G., Witten, D., Hastie, T., and Tibshirani, R. (2013) _An
         Introduction to Statistical Learning with applications in R_,
         <URL: www.StatLearning.com>, Springer-Verlag, New York
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

