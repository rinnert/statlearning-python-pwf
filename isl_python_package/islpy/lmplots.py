import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import seaborn as sns
from statsmodels.nonparametric import smoothers_lowess
from statsmodels.graphics.gofplots import ProbPlot
from islpy import utils


def plot_fit(fitted_model, column, data=None,
             ax=None, points=100, scolor='C0', fcolor='C1', pcolor='C2', lcolor='C7',
             cialpha=0.3, pialpha=0.2, lalpha=0.8, lw=2,
             show_ci=True, show_pi=False, lowess=False, legend=False):
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
    
    slabel = None
    if legend:
        slabel = 'data'
    ax = sns.scatterplot(x=column, y=model.endog,
                         data=data, ax=ax, color=scolor, label=slabel)
    ax.set_title(f'Fit vs {column}')
    ax.set_ylabel(model.endog_names)
    ax.plot(x, y, color=fcolor, lw=lw, label='fit')
    
    if show_ci:
        ax.fill_between(x, cil, ciu, color=fcolor, alpha=cialpha, label='conf. int.')

    if show_pi:
        ax.fill_between(x, pil, piu, color=pcolor, alpha=pialpha, label='pred. int.')

    if lowess:
        ax.plot(*utils.lowess(data[column], model.endog), color=lcolor, lw=lw, alpha=lalpha, label='lowess')

    if legend:
        ax.legend()

    return ax


def plot_fit_3D(fitted_model, column1, column2, 
                data=None, points=100, 
                scolor='C3', fcolor='C0', cicolor='C1', 
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
    try:
        fig.suptitle(f'Fit vs {column1} & {column2}\n{model.formula}')
    except AttributeError:
        ax.suptitle(f'Fit vs {column1} & {column2}')
    
    return fig, ax


def plot_resid(fitted_model, ax=None, scolor='C0', lcolor='C1', lw=2, lowess=True,
               annotations=3):
    """Plot residuals versus fitted values."""

    values = fitted_model.fittedvalues
    resids = fitted_model.resid

    ax = sns.scatterplot(values, resids, color=scolor, ax=ax)
    ax.axhline(0, color=scolor, alpha=0.5)

    if lowess:
        ax.plot(*utils.lowess(values, resids), color=lcolor, lw=lw)

    if  annotations:
        idxs = resids.abs().nlargest(annotations).index
        for idx in idxs:
            value = values[idx].max()
            resid = resids[idx].max()
            ax.annotate(idx, (value, resid))

    ax.set_title('Residuals vs Fitted')
    ax.set_xlabel('Fitted Values')
    ax.set_ylabel('Residuals')

    return ax


def plot_qq(fitted_model, ax=None, scolor='C0', lcolor='C1', lw=2, line=True,
            annotations=3):
    """Produce standard Q-Q plot."""
    
    resids = fitted_model.get_influence().resid_studentized_internal
    pp = ProbPlot(resids)
    
    ax = sns.scatterplot(pp.theoretical_quantiles, pp.sorted_data, 
                         ax=ax, color=scolor, linewidth=0, alpha=0.7)
    if line:
        ax.plot(pp.theoretical_quantiles[[0, -1]], pp.theoretical_quantiles[[0, -1]], color=lcolor, lw=lw)

    if  annotations:
        idxs = pd.Series(resids).abs().nlargest(annotations).index
        jdxs = pd.Series(pp.sorted_data).abs().nlargest(annotations).index
        for idx, jdx in zip(idxs, jdxs):
            qq = pp.theoretical_quantiles[jdx]
            resid = pp.sorted_data[jdx]
            ax.annotate(fitted_model.resid.index[idx], (qq, resid))

    ax.set_title('Normal Q-Q')
    ax.set_xlabel('Theoretical Quantiles')
    ax.set_ylabel('Standardised Residuals')

    return ax


def plot_scaleloc(fitted_model, ax=None, scolor='C0', lcolor='C1', lw=2, lowess=True,
                  annotations=3):
    """Produce scale-location plot."""
    
    resids = np.sqrt(np.abs(fitted_model.get_influence().resid_studentized_internal))
    values = fitted_model.fittedvalues
    
    ax = sns.scatterplot(values, resids, ax=ax, color=scolor)

    if lowess:
        ax.plot(*utils.lowess(values, resids), color=lcolor, lw=lw)

    if  annotations:
        idxs = pd.Series(resids).nlargest(annotations).index
        for idx in idxs:
            value = values[idx]
            resid = resids[idx]
            ax.annotate(values.index[idx], (value, resid))

    ax.set_title('Scale-Location')
    ax.set_xlabel('Fitted Values')
    ax.set_ylabel('$\sqrt{|\mathrm{Standardised}\; \mathrm{Residuals}|}$')

    return ax


def plot_leverage(fitted_model, ax=None, scolor='C0', lcolor='C1', ccolor='C2', lw=2, 
                  lowess=True, cook=True, legend=True, annotations=3):
    """Produce leverage plot."""
    
    influence = fitted_model.get_influence()
    resids = influence.resid_studentized_internal
    values = influence.hat_matrix_diag
    cooks = influence.cooks_distance[0]
    
    ax = sns.scatterplot(values, resids, ax=ax, color=scolor)
    ax.set

    if lowess:
        ax.plot(*utils.lowess(values, resids), color=lcolor, lw=lw)

    if  annotations:
        idxs = pd.Series(cooks).nlargest(annotations).index
        for idx in idxs:
            value = values[idx]
            resid = resids[idx]
            ax.annotate(fitted_model.fittedvalues.index[idx], (value, resid))

    if cook:
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        p = fitted_model.params.size
        x = np.linspace(*xlim, 100)
        y = np.sqrt((0.5 * p * (1 - x)) / x) 
        ax.plot(x, y, color=ccolor, lw=lw, alpha=0.8, label="Cook's Distance")
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        if legend:
            ax.legend()

    ax.set_title('Residuals vs Leverage')
    ax.set_xlabel('Leverage')
    ax.set_ylabel('Standardised Residuals')

    return ax


def plot_hat(fitted_model, ax=None, scolor='C0', annotations=3):
    """Make scatter plot of leverage vs index."""

    influence = fitted_model.get_influence()
    ys = influence.hat_matrix_diag
    xs = np.arange(fitted_model.fittedvalues.index.size)

    ax = sns.scatterplot(xs, ys, ax=ax, color=scolor)

    if  annotations:
        idxs = pd.Series(ys).nlargest(annotations).index
        for idx in idxs:
            x = xs[idx]
            y = ys[idx]
            ax.annotate(fitted_model.fittedvalues.index[idx], (x, y))

    ax.set_title('Leverage vs Index')
    ax.set_xlabel('Index')
    ax.set_ylabel('Leverage')

    return ax


def plot(fitted_model, scolor='C0', lcolor='C1', auxcolor='C2', annotations=3, figsize=(12, 9), title=None):
    """Produce R-style control plots for linear model."""
    fig, axs = plt.subplots(2, 2, figsize=figsize)

    plot_resid(fitted_model, ax=axs[0][0], scolor=scolor, lcolor=lcolor, annotations=annotations)
    plot_qq(fitted_model, ax=axs[0][1], scolor=scolor, lcolor=lcolor, annotations=annotations)
    plot_scaleloc(fitted_model, ax=axs[1][0], scolor=scolor, lcolor=lcolor, annotations=annotations)
    plot_leverage(fitted_model, ax=axs[1][1], scolor=scolor, lcolor=lcolor, ccolor=auxcolor, annotations=annotations)
    
    if title is None:
        try:
            fig.suptitle(fitted_model.model.formula, y=1.02, weight='bold')
        except AttributeError:
            pass
    else:
        fig.suptitle(title, y=1.02, weight='bold')

    fig.tight_layout()
    
    return fig



