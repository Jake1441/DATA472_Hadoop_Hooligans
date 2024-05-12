import pandas as pd
"""
Notes:
Sample ID might be unique
Site ID should also be unique

Can use a loop to get all the csv files under well_data.
"""
# well data metadata

well_data_metadata = pd.read_csv("./dataset/BV22-0001.csv", nrows=3)

# read the well data
well_data_values = pd.read_csv("./dataset/BV22-0001.csv", skiprows=4)
print("Well metadata")
print(well_data_metadata.head())
print("Well Data")
print(well_data_values.head())

