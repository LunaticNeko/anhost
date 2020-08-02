# anhost basic plotting module

import os #used for file path joining
import pandas as pd
import numpy as np
import scipy
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# Configuration file template is available at config_template.py
import config

indexed_converter = {
    "year": int,
    "sec": str,
    "timestamp": pd.to_datetime,
    "deadline": pd.to_datetime,
    "index.sec": int,
    "index.year": int,
    }

df = pd.read_csv(os.path.join(config.indexed_dir, config.indexed_dataset),
                    converters=indexed_converter)

df['timeleft'] = df['deadline'] - df['timestamp']
df['timeleft'] = df['timeleft'].clip(lower=pd.Timedelta(0))
# SO::54535619
df['timeleft'] = df['timeleft']/pd.to_timedelta(1, unit='D')

years = [2019, 2020]

timeleft_series = [df.loc[df['year']==year]['timeleft'] for year in years]
scipy.stats.ttest_ind(timeleft_series[0], timeleft_series[1], equal_var=False)
