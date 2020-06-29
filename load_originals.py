# anhost pre-processing module
# About privacy:
# - This tool receives input with personally identifying information (PII), but
#   it is removed at the earliest opportunity possible. It is not used for any
#   purpose except to ensure that each student has only one record.
# - This module is used for data conversion and PII scrambling. It is NOT used
#   for actual data analysis. Input data for this module is NOT AVAILABLE to the
#   general public, but the output is.
# - This module produces an intermediate file suitable for later use.

import os #used for file path joining
import pandas as pd
import numpy as np

# We use a configuration script to set it all up. Refer to
# load_originals_config_template.py for template.
import load_originals_config as config

# Column name definitions

cn = {
        "userid": "<User ID>",
        "date": "<Tested on>",
        "time": "<Taken Time>",
        "score": "<Score>"
        }

import_cns = [cn["userid"], cn["date"], cn["time"], cn["score"]]
export_sec_cns = ["year", "sec", "index.year", "index.sec", "timestamp", "deadline"]


# Final dataframe to be exported (will contain no user ID and only minimum data
# necessary for further processing)

df_dtypes = np.dtype([
    ("year", int),
    ("sec", str),
    ("index.year", int),
    ("index.sec", int),
    ("timestamp", np.datetime64),
    ("deadline", np.datetime64),
    ])

df = pd.DataFrame(np.empty(0, dtype=df_dtypes))

# Actual import

for (year, deadline, sections) in config.import_datasets:
    for (section, filename) in sections:
        df_sub = pd.read_csv(os.path.join(config.import_dir, filename), usecols=import_cns,
                converters={cn["userid"]: str, cn["date"]: str, cn["time"]: str, cn["score"]: int})
        new_timestamp = pd.to_datetime(df_sub[cn["date"]] + " " + df_sub[cn["time"]])
        df_sub["timestamp"] = pd.to_datetime(df_sub[cn["date"]] + " " + df_sub[cn["time"]])
        df_sub["deadline"] = pd.to_datetime(deadline)
        df_sub["year"] = int(year)
        df_sub["sec"] = str(section)
        df_sub["index.year"] = 0
        df_sub = df_sub.sort_values(by="timestamp", ascending="true")
        df_sub["index.sec"] = np.arange(len(df_sub))+1
        df_sub = df_sub.drop_duplicates(subset=[cn["userid"]], keep="first")
        df_sub = df_sub.drop(import_cns, axis=1)
        df_sub = df_sub[export_sec_cns]
        df = df.append(df_sub)

#print(df)

export_path = os.path.join(config.export_dir, config.export_filename)
with open(export_path, 'w') as export_file:
    export_file.write(df.to_csv(index=False))


