# anhost Configuration TEMPLATE
# Dataset list structure:
#   (YEAR, DEADLINE, [(section, filename)])
original_dir = "dataset/original"
original_datasets = [(2020, "2020-05-15 00:00:00",
                [("section_1", "sample_dataset_2020.txt"),
                ]),
                   (2019, "2019-05-17 00:00:00",
                [("section_1", "sample_dataset_2019.txt"),
                ])
                ]

proc_dir = "dataset"
proc_dataset = "_processed.csv"

indexed_dir = "dataset"
indexed_dataset = "_indexed.csv"
