import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_fitted_model(fitted_model, var_name, data=None,
                      ax=None, points=100, scolor='C0', fcolor='C1', alpha=0.3):
    """Make a scatter plot and overlay fit result."""

    model = fitted_model.model

    if data is None:
        data = pd.DataFrame(model.exog, columns=model.exog_names)
        data[model.endog_names] = model.endog

    xs = pd.DataFrame()
    for name in model.exog_names:
        try:
            xs[name] = np.linspace(data[name].min(), data[name].max(), points)
        except KeyError:
            xs[name] = np.ones(points)  # presumably the intercept

    pred = fitted_model.get_prediction(xs).summary_frame()
    x = xs[var_name]
    y = pred['mean']
    cil = pred['mean_ci_lower']
    ciu = pred['mean_ci_upper']

    ax = sns.scatterplot(x=var_name, y=model.endog_names,
                         data=data, ax=ax, color=scolor)
    ax.plot(x, y, color=fcolor, lw=2)
    ax.fill_between(x, cil, ciu, color=fcolor, alpha=alpha)

    return ax