import numpy as np
import pandas as pd

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
