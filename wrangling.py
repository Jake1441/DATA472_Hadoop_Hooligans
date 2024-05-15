import pandas as pd
import os
import shutil
import uuid

def process_ground_water_data(file_path, region):
    # Read the file
    df = pd.read_excel(file_path, sheet_name=None)

    # Read the relevant tab
    df_GWQ_Monitoring_Results = df[list(df.keys())[1]]

    # Filter by region
    df_GWQ_Monitoring_Results = df_GWQ_Monitoring_Results[df_GWQ_Monitoring_Results["Region"] == region]

    # Convert 'Date' column to datetime format
    df_GWQ_Monitoring_Results["Date"] = pd.to_datetime(df_GWQ_Monitoring_Results["Date"], dayfirst=True)

    # Extract the 'Year' component
    df_GWQ_Monitoring_Results["Year"] = df_GWQ_Monitoring_Results["Date"].dt.year

    # Create new DataFrame with relevant columns
    indicator_df = df_GWQ_Monitoring_Results[["Year", "Indicator", "Units", "RawValue", "CenType", "Value"]].copy()

    # Sort by year
    indicator_year = indicator_df.sort_values(by="Year")

    # Generate a unique filename
    unique_filename = 'indicator_year_df_' + str(uuid.uuid4())[:8] + '.csv'
    csv_file_path = os.path.join(os.path.expanduser('~'), 'Downloads', unique_filename)

    # Save the DataFrame to a CSV file
    indicator_year.to_csv(csv_file_path, index=False)

    return indicator_year

# Example usage:
file_path = r"C:/Users/julia/OneDrive/Desktop/DATA472 Data Engineering/DATA472_Hadoop_Hooligans/Lawa_ground_water-2024-04-12.xlsx"
region = "Canterbury"
processed_data = process_ground_water_data(file_path, region)
print(processed_data.head())
