import pandas as pd

# Load the positive and negative CSV files
path_to_positive = r"C:\Users\user\Desktop\work\mirna\mirna for web\data\data_human\darnell_human.csv"
path_to_negative = r"C:\Users\user\Desktop\work\mirna\mirna for web\data\data_human\non_overlapping_sites_darnell_human_ViennaDuplex_negative_features.csv"

# Load the data types from the second row of each file
positive_dtypes = pd.read_csv(path_to_positive, nrows=1).iloc[0]
negative_dtypes = pd.read_csv(path_to_negative, nrows=1).iloc[0]

# Load the CSV files with the specified data types
positive_df = pd.read_csv(path_to_positive)
negative_df = pd.read_csv(path_to_negative, skiprows=[1])

# Find common columns in both DataFrames
common_columns = list(set(positive_df.columns).intersection(negative_df.columns))

# Remove any columns that are not in both DataFrames
positive_df = positive_df[common_columns]
negative_df = negative_df[common_columns]

# Ensure equal number of positive and negative samples
num_rows = min(positive_df.shape[0], negative_df.shape[0])
positive_df = positive_df.head(num_rows)
negative_df = negative_df.head(num_rows)

# Add a new column named "target" with 1 for positive and 0 for negative
positive_df["target"] = 1
negative_df["target"] = 0

# Concatenate the DataFrames
concatenated_df = pd.concat([positive_df, negative_df], ignore_index=True)
