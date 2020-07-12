# anhost Configuration TEMPLATE
# Dataset list structure:
#   (YEAR, DEADLINE, [(section, filename)])
original_dir = "original_dataset"
original_datasets = [(2020, "2020-05-15 00:00:00",
                [("section_1", "dataset_2020_section_1.txt"),
                 ("section_2", "dataset_2020_section_2.txt")]),
                   (2019, "2019-05-14 18:00:00",
                [("section_1", "dataset_2019_section_1.txt"),
                 ("section_2", "dataset_2019_section_2.txt" )])
                ]

proc_dir = "dataset"
proc_dataset = "_processed.csv"

indexed_dir = "dataset"
indexed_dataset = "_indexed.csv"
