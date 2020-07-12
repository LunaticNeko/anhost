# anhost indexing module
#
# This file is separate from the pre-processing module because that one is
# meant ONLY to remove sensitive and duplicate data.

import os #used for file path joining
import pandas as pd
import numpy as np

# Configuration file template is available at config_template.py
import config

proc_converter = {
    "year": int,
    "sec": str,
    "timestamp": pd.to_datetime,
    "deadline": pd.to_datetime,
    }

df = pd.read_csv(os.path.join(config.proc_dir, config.proc_dataset),
                      converters=proc_converter)

df = df.sort_values(by=["year","timestamp"], ascending="true")
df['index.sec'] = df.groupby(["year","sec"]).cumcount()
df['index.year'] = df.groupby("year").cumcount()

indexed_path = os.path.join(config.indexed_dir, config.indexed_dataset)
with open(indexed_path, 'w') as indexed_file:
    indexed_file.write(df.to_csv(index=False))
