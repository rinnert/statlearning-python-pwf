import re
import numpy as np
import pandas as pd
import patsy


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


def encode_categories(data, formula=None):
    """Return new data frame with category encoding and flattened names."""

    if formula is None:
        formula = '+'.join(data.columns)

    r_cat = re.compile(r'(?P<name>.+)\[(?P<trans>[TSDH]?)\.(?P<category>.+)\]') 
    r_cexp = re.compile(r'C\((?P<name>.+), .+\)') 
    r_poly = re.compile(r'C\((?P<name>.+), Poly\)\.(?P<category>.+)')

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
