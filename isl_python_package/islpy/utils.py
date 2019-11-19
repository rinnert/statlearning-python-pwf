import re
import numpy as np
import pandas as pd
import patsy
import statsmodels.api as sm
from statsmodels.nonparametric import smoothers_lowess
from sklearn.base import BaseEstimator, RegressorMixin
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


class SMWrapper(BaseEstimator, RegressorMixin):
    """ A universal sklearn-style wrapper for statsmodels regressors.
    
        Credit: 
        
            https://stackoverflow.com/users/6498293/david-dale
    """
    def __init__(self, model_class, fit_intercept=True):
        self.model_class = model_class
        self.fit_intercept = fit_intercept

    def fit(self, X, y):
        if self.fit_intercept:
            X = sm.add_constant(X)
        self.model_ = self.model_class(y, X)
        self.results_ = self.model_.fit()
    
    def predict(self, X):
        if self.fit_intercept:
            X = sm.add_constant(X)
       
        return self.results_.predict(X)


def marginalised_range(columns, data, points=100, others=None):
    """Return data frame with range in column column and 
        the other variables marginalised out.
    """

    names = data.columns

    xs = pd.DataFrame()
    for name in names:
        if name == columns or name in columns:
            xs[name] = np.linspace(data[name].min(), data[name].max(), points)
        elif others is not None and (name == others or name in others):
            xs[name] = np.full(points, data[name].mean())
        elif others is None:
            xs[name] = np.full(points, data[name].mean())
        else:
            xs[name] = data[name]

    return xs


def lowess(x, y):
    """Compute y versus x LOWESS estimate."""

    lfit = smoothers_lowess.lowess(y, x)
    
    return lfit[:, 0], lfit[:, 1]


def encode_categories(data, formula=None):
    """Return new data frame with category encoding and flattened names."""

    if formula is None:
        formula = '+'.join(data.columns)

    r_cat = re.compile(r'(?P<name>.+)\[(?P<trans>[TSDH]?)\.(?P<category>.+)\]') 
    r_cexp = re.compile(r'C\((?P<name>.+), .+\)') 
    r_poly = re.compile(r'C\((?P<name>.+), Poly.*\)\.(?P<category>.+)')

    df = patsy.dmatrix(formula, data, return_type='dataframe')
    
    new_names = {}
    for name in df.columns:
        m_cat = r_cat.match(name)
        m_poly = r_poly.match(name)
        if m_cat:
            new_name = m_cat['name']
            m_cexp = r_cexp.match(new_name)
            if m_cexp:
                new_name = m_cexp['name']
            category = m_cat['category']
            trans = m_cat['trans']
            if trans:
                new_name += '_' + trans
            new_name += '_' + category
            new_names[name] = new_name
        elif m_poly:
            new_name = m_poly['name'] + '_' + m_poly['category']
            new_names[name] = new_name

    df.rename(new_names, axis=1, inplace=True)
    try:
        df.drop('Intercept', axis=1, inplace=True)
    except KeyError:
        pass

    return df


def plot_corr(corr, figsize=(12, 10), cmap=None, labels=None):
    """Plot annotated correlation matrix for given data frame."""

    mask = np.full_like(corr, False, dtype=bool)
    mask[np.triu_indices_from(mask)] = True
    corr.iloc[mask] = 0

    if cmap is None:
        cmap = sns.diverging_palette(220, 10, as_cmap=True)

    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(corr, 
                mask=mask, 
                xticklabels=False, 
                yticklabels=False, 
                cmap=cmap, 
                center=0, 
                square=True,
                annot=True, 
                fmt=".2f")

    if labels is None:
        try:
            plt.xticks(range(len(corr.columns)), corr.columns, rotation=45);
        except AttributeError:
            pass
    else:
        plt.xticks(range(len(lables)), labels, rotation=45);

    # yticks only if supported by matplotlib version (there is
    # a bug in 3.1.1 that distorts the plot otherwise).
    if matplotlib.__version__ != '3.1.1':
        if labels is None:
            try:
                plt.yticks(range(len(corr.index)), corr.index)
            except AttributeError:
                pass
        else:
            plt.yticks(range(len(lables)), labels);

    return fig, ax


def meshgrid_map(x1, x2, func, npoints=100):
    """Create a meshgrid and map a function on it.

    Create meshgrid of size npoints x npoints from ranges
    of the x and y input arrays.

    Then map the callable func on the grid, resulting in an array
    z with the same shape as the grid.

    Return x, y, z of the grid
    """
    x1s = np.linspace(min(x1), max(x1), npoints)
    x2s = np.linspace(min(x2), max(x2), npoints)
    X, Y = np.meshgrid(x1s, x2s)
    try:
        z = func(X.ravel(), Y.ravel())
    except (TypeError, ValueError):
        z = func(np.c_[X.ravel(), Y.ravel()])

    return X, Y, z.reshape((*X.shape, -1))


def plot_decision_contour(x1, x2, predprob, npoints=100, category=0, ax=None, labels=True,
        colors='black', levels=[0.5], alpha=0.7, fmt='%.2f'):
    """Plot decision contours.

    Plot descision contours based on the predictors x1, x2 and the probabilities returned by
    the callable predprob. By default the contours for the first category are plotted.

    If ax is None the plot goes onto the current default axis.

    If labels is True (default) the contour lines are labeled inline.

    The other keyword arguments are passed to matplotlib's contour() function.

    Return the axis the plot was drawn on.
    """
    xs, ys, zs = meshgrid_map(x1, x2, predprob, npoints)
    try:
        z = zs[:, :, category]
    except IndexError:
        z = zs

    if ax is None:
        ax = plt

    cs = ax.contour(xs, ys, z, colors=colors, alpha=alpha, levels=levels)

    if labels:
        _ = cs.ax.clabel(cs, cs.levels, fmt=fmt)

    return cs.ax


def plot_decision_boundaries(x1, x2, predprob, npoints=100, ax=None, cmap='Paired', alpha=0.1):
    """Plot decision boundaries.

    Plot descision contours based on the predictors x1, x2 and the probabilities returned by
    the callable predprob.

    If ax is None the plot goes onto the current default axis.

    The other keyword arguments are passed to matplotlib's pcolormesh() function.

    Return the axis the plot was drawn on.
    """
    xs, ys, zs = meshgrid_map(x1, x2, predprob, npoints)

    z = zs.argmax(axis=2)

    if ax is None:
        ax = plt

    _ = ax.pcolormesh(xs, ys, z, cmap=cmap, alpha=alpha)

    return ax







