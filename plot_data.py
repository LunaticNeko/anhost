# anhost basic plotting module

import os #used for file path joining
import pandas as pd
import numpy as np
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

#plotdata = df[["year","timeleft","index.year"]]

# SO::14887119
#fig = sns.FacetGrid(data=df, hue="year")
fig = sns.scatterplot(data=df, x="timeleft", y="index.year", hue="year", legend="full")
fig.invert_xaxis()
#fig.set(xlim=(30,0))
mpl.pyplot.show()

