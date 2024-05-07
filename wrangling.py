"""
Some wrangling for Hadoop Hooligans
jjm148 81456731

I just grouped the raw file to by year and indicator
Then the output will be saved into downloads folder
Need to automate somehow - will update

Analysis script will follow
"""

import pandas as pd

# Read the file from LAWA
file_path = r"C:/Users/julia/OneDrive/Desktop/DATA472 Data Engineering/DATA472_Hadoop_Hooligans/Lawa_ground_water-2024-04-12.xlsx"

# There are four tabs in this excel file
# The first tab is irrelevant
# Read the second tab (index 1)
df_GWQ_Monitoring_Results = pd.read_excel(file_path, sheet_name=1)

# Read the third tab (index 2)
df_State_Results = pd.read_excel(file_path, sheet_name=2)

# Read the fourth tab (index 3)
df_Trend_Results = pd.read_excel(file_path, sheet_name=3)

# Explore GWQ Monitoring Results
# print(df_GWQ_Monitoring_Results.head())

# Check the completeness of each column
completeness = df_GWQ_Monitoring_Results.isnull().mean() * 100
# print(completeness)

# Filter Canterbury region only
df_GWQ_Monitoring_Results = df_GWQ_Monitoring_Results[df_GWQ_Monitoring_Results["Region"] == "Canterbury"]

# Convert 'Date' column to datetime format
df_GWQ_Monitoring_Results["Date"] = pd.to_datetime(df_GWQ_Monitoring_Results["Date"], dayfirst=True)

# Extract the 'Year' component
df_GWQ_Monitoring_Results["Year"] = df_GWQ_Monitoring_Results["Date"].dt.year

# Make a copy of the DataFrame to avoid SettingWithCopyWarning
canterbury_GWQ = df_GWQ_Monitoring_Results.copy()

# Create new df with Year, Indicator, Units, Raw Values, CenType, and Value
indicator_df = canterbury_GWQ[["Year", "Indicator", "Units", "RawValue", "CenType", "Value"]].copy()

# Sort by year
indicator_year = indicator_df.sort_values(by="Year")

# Display the first few rows of the new DataFrame
print(indicator_year.head())

# Save the DataFrame to a CSV file
indicator_year.to_csv('indicator_year_df.csv', index=False)

# Move the saved file to the Downloads folder
import shutil
import os

# Path to the Downloads folder
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

# Move the file to the Downloads folder
shutil.move('indicator_year_df.csv', downloads_folder)

