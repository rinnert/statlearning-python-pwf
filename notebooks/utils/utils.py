import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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


def plot_fit(fitted_model, column, data=None,
             ax=None, points=100, scolor='C0', fcolor='C1', alpha=0.3):
    """Make a scatter plot and overlay fit result."""

    model = fitted_model.model

    if data is None:
        data = pd.DataFrame(model.exog, columns=model.exog_names)

    xs = marginalised_range(column, data, points=points)

    pred = fitted_model.get_prediction(xs).summary_frame()
    x = xs[column]
    y = pred['mean']
    cil = pred['mean_ci_lower']
    ciu = pred['mean_ci_upper']
    
    ax = sns.scatterplot(x=column, y=model.endog,
                         data=data, ax=ax, color=scolor)
    ax.set_ylabel(model.endog_names)
    ax.plot(x, y, color=fcolor, lw=2)
    ax.fill_between(x, cil, ciu, color=fcolor, alpha=alpha)

    return ax

