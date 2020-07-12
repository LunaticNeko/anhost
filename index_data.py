# anhost indexing module
#
# This file is separate from the pre-processing module because that one is
# meant ONLY to remove sensitive and duplicate data.

import os #used for file path joining
import pandas as pd
import numpy as np

# Configuration file template is available at config_template.py
import config

proc_cns = ["year", "sec", "timestamp", "deadline"]
proc_dtypes = np.dtype([
    ("year", int),
    ("sec", str),
    ("timestamp", np.datetime64),
    ("deadline", np.datetime64),
    ])
proc_converter = {
    "year": int,
    "sec": str,
    "timestamp": pd.to_datetime,
    "deadline": pd.to_datetime,
    }

def index_data(df):
    '''
    Given a data frame, perform indexing on it.
    '''
    # if index, index.year, and index.sec are not present, add them.
    # select each year
    #   select each sec
    #       sort by time ascending
    #     index students in sec
    #   sort by time ascending
    #   index students in year
    # sort by time ascending
    # index students (globally)
    pass

# main

proc_df = pd.read_csv(os.path.join(config.proc_dir, config.proc_dataset), converters=proc_converter)

'''
the following lines HGT'd from load_originals.py
        df_sub["index.year"] = 0
        df_sub = df_sub.sort_values(by="timestamp", ascending="true")
        df_sub["index.sec"] = np.arange(len(df_sub))+1
        df_sub = df_sub.drop_duplicates(subset=[cn["userid"]], keep="first")
'''
