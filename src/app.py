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
import os
import sys

# Get the full path of the current file
file_path = sys.argv[0]

# Get the base name of the file (i.e., file name with extension)
base_name = os.path.basename(file_path)

# Remove the file extension
file_name = os.path.splitext(base_name)[0]

from log_parser.log_settings import *
# call outside so function does not call gain this sets the date for the actual file.
f_date = get_frozen_datetime()

# set up the logging info and date, you only need to do this once!
send_to_log(f_date, file_name)

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
        logging.info(code)
        get_into_dataframe.get_main_data(well_code=code)
