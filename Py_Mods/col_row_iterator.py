"""
Function to read a basic row by column object
Could this be a class?
"""


def list_iter(data):
    for row_info in data:
        for col_data in row_info:
            print(col_data)


def dataframe_iter(data):
    for row_info in data.iterrows():
        for col_data in row_info:
            print(col_data)


def by_row(data):
    for row_info in data:
        print(row_info)


def dic_iterator(dict_data):
    for key, value in dict_data.items():
        print(f"{key} : {value}")