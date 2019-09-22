#!/usr/bin/env python
import pandas as pd
import os

hdf_file = 'isldata.h5'
try:
    os.remove(hdf_file)
except FileNotFoundError:
    pass

with pd.HDFStore(hdf_file, complevel=9, complib='blosc') as store:
    for fname in os.listdir('./'):
        if fname.endswith('.csv'):
            print(fname)
            df = pd.read_csv(fname)
            dfname = os.path.splitext(fname)[0]
            store[dfname] = df
        if fname.endswith('.dat'):
            print(fname)
            df = pd.read_csv(fname, header=None, sep='\s+')
            dfname = os.path.splitext(fname)[0]
            store[dfname] = df
