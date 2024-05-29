import pandas as pd

import Py_Mods.postgres_actions as pgapi


def read_data_only(file_path):
    """
    Function that only reads the link
    this will be adapted to format the sheets for curl use.
    :return: dfs which is a variable that might involve columns at a later stage.
    """
    dfs = pd.read_excel(file_path, sheet_name=None)
    return dfs


dfs = read_data_only("Lawa_ground_water-2024-04-21.xlsx")

for sheet_name, df in dfs.items():  # dfs is a dictionary of workbook:pandas.df pairs
    if sheet_name == "GWQMonitoringResults2004-22":
        # year conversion from Julian

        df["Year"] = df["Date"].dt.year
        print(f"Working on Sheet name: {sheet_name}")
        df = df.sort_values(by="Year")
        curl_data = pd.DataFrame(
            {"Year": df.loc[:, "Year"], "measurement_unit": df.loc[:, "Indicator"], "Units": df.loc[:, "Units"],
             "obs_value": df.loc[:, "RawValue"]})


def prepare_data(dataset, data_fields):
    """
    Commit data to the dataset
    function takes a dictionary and inserts the appropriate variables for
    requests to post the data to the table called data under schema db_access
    :param dataset: the dataset to work on
    :param data_fields: the fields to use in this dataset
    :return:
    """

    # drop fields with detect
    dataset['obs_value'] = pd.to_numeric(dataset['obs_value'], errors='coerce')
    # Drop rows where 'obs_value' is NaN (i.e., rows with non-numeric values)
    dataset = dataset.dropna(subset=['obs_value'])
    # some tables have their own field name so this converts the name to the target name the api expects
    # see db_data_fields below this function.
    payload_data_dict = {}
    for db_field in data_fields:
        payload_data_dict[db_field[0]] = dataset[db_field[-1]]

    payload_data = pd.DataFrame(payload_data_dict).to_csv(index=False)
    pgapi.db_commit(payload_data)


# first row in each array is field name, second is the dataset field name incase the two are different.
db_data_fields = [['Year'], ['obs_value'], ['Units'], ['measure_unit', 'measurement_unit']]
prepare_data(curl_data, db_data_fields)
