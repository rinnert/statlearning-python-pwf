import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import seaborn as sns
from islpy import utils


def plot_fit(fitted_model, column, data=None,
             ax=None, points=100, scolor='C0', fcolor='C1', pcolor='C2', 
             cialpha=0.3, pialpha=0.2, 
             show_ci=True, show_pi=False):
    """Make a scatter plot and overlay fit result.
    
    Make a scatter plot of the response versus a specified predictor and
    overlay the fit result.  The distributions of the other predictors are
    marginalised out, ie. they are set to the mean values of their respective
    distributions.

    Returns the matplot lib axis object the plot was drawn on.
    """

    model = fitted_model.model

    if data is None:
        data = pd.DataFrame(model.exog, columns=model.exog_names)

    xs = utils.marginalised_range(column, data, points=points)

    pred = fitted_model.get_prediction(xs).summary_frame()
    x = xs[column]
    y = pred['mean']
    cil = pred['mean_ci_lower']
    ciu = pred['mean_ci_upper']
    pil = pred['obs_ci_lower']
    piu = pred['obs_ci_upper']
    
    ax = sns.scatterplot(x=column, y=model.endog,
                         data=data, ax=ax, color=scolor)
    ax.set_ylabel(model.endog_names)
    ax.plot(x, y, color=fcolor, lw=2)
    if show_ci:
        ax.fill_between(x, cil, ciu, color=fcolor, alpha=cialpha)
    if show_pi:
        ax.fill_between(x, pil, piu, color=pcolor, alpha=pialpha)

    return ax


def plot_fit_3D(fitted_model, column1, column2, 
                data=None, points=100, 
                scolor='C0', fcolor='C0', cicolor='C1', 
                salpha=0.4, cialpha=0.2, cmap='Oranges', 
                figsize=(12,9), show_ci=True):
    """Produce 3D scatter plot and overlay fitted model surface.
    
    
    Make a 3D scatter plot of the response versus two specified predictors and
    overlay the fit result surface.  The distributions of the other predictors
    are marginalised out, ie. they are set to the mean values of their
    respective distributions.

    NOTE: This resets matplotlib graphics options to the defaults. 

    Returns the matplotlib figure and Axes3D objects.
    """

    model = fitted_model.model
    
    if data is None:
        data = pd.DataFrame(model.exog, columns=model.exog_names)

    marg = utils.marginalised_range((column1, column2), data, points=points)
    
    sns.reset_defaults()

    fig = plt.figure(figsize=figsize)
    ax = axes3d.Axes3D(fig)

    # prepare point grids from the ranges of the scatter plot
    xs = marg[column1] 
    ys = marg[column2]
    xv, yv = np.meshgrid(xs, ys)
    zv = np.zeros((ys.size, xs.size))
    lv = np.zeros((ys.size, xs.size))
    uv = np.zeros((ys.size, xs.size))

    # compute predictions and CI bounds for the rows in the point grids
    for idx, y in enumerate(yv):
        marg[column2] = y
        pred = fitted_model.get_prediction(marg).summary_frame()
        zv[idx] = pred['mean']
        lv[idx] = pred['mean_ci_lower']
        uv[idx] = pred['mean_ci_upper']

    # 3D scatter plot of the raw data
    ax.scatter(data[column1], data[column2], model.endog, color=scolor)

    # plot the prediction & CI boundary surfaces
    ax.plot_surface(xv, yv, zv, alpha=salpha, color=fcolor)
    if show_ci:
        ax.plot_surface(xv, yv, lv, alpha=cialpha, color=cicolor)
        ax.plot_surface(xv, yv, uv, alpha=cialpha, color=cicolor)
    
        # add contour plot of the CI width to the bottom of the figure   
        ax.contourf(xv, yv, uv-lv,
                    zdir='z',
                    offset=ax.get_zlim()[0],
                    levels=50,
                    antialiased=True,
                    alpha=cialpha*2,
                    cmap=cmap)
    
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.set_zlabel(model.endog_names)
    
    return fig, ax
