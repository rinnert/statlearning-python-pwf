import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def marginalised_range(var_name, data, points=100, others=None):
    """Return data frame with range in column var_name and the other variables marginalised out."""
    
    if others is None:
        names = list(data.columns).remove(var_name)
    else:
        names = list(others)
        
    xs = pd.DataFrame()
    for name in names:
        xs[name] = np.full(points, data[name].mean())
    xs[var_name] = np.linspace(data[var_name].min(), data[var_name].max(), points)
    
    return xs
    

def plot_linear_model(fitted_model, var_name, data=None,
                      ax=None, points=100, scolor='C0', fcolor='C1', alpha=0.3):
    """Make a scatter plot and overlay fit result."""

    model = fitted_model.model

    if data is None:
        data = pd.DataFrame(model.exog, columns=model.exog_names)

    xs = marginalised_range(var_name, data, points=points)

    pred = fitted_model.get_prediction(xs).summary_frame()
    x = xs[var_name]
    y = pred['mean']
    cil = pred['mean_ci_lower']
    ciu = pred['mean_ci_upper']

    ax = sns.scatterplot(x=var_name, y=model.endog,
                         data=data, ax=ax, color=scolor)
    ax.plot(x, y, color=fcolor, lw=2)
    ax.fill_between(x, cil, ciu, color=fcolor, alpha=alpha)

    return ax