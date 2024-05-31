import sys
import os

# current_dir = os.path.dirname(os.path.abspath(__file__))
# script_dir = os.path.join(current_dir, "..")
# sys.path.append(script_dir)

import get_into_dataframe
import create_well_metadata_table
import connect_to_db as connect
import insert_into_well_metadata as insert_into_well
import pandas as pd

if __name__ == "__main__":
    connection = connect.connect_to_database()
    create_well_metadata_table.create_well_metadata_table(connection=connection)
    all_ecan_df = pd.read_csv('/app/src/ecan_data.csv')
    all_ecan_df.apply(
        lambda row: insert_into_well.insert_into_well_metadata(connection, row), axis=1
    )
    directory = "/app/src/well_data/"
    well_code_list = os.listdir(directory)
    code_list = [x.split(".")[0] for x in well_code_list]
    for code in code_list:
        print(code)
        get_into_dataframe.get_main_data(well_code=code)
