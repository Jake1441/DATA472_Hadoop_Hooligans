import os
from datetime import date

import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import Py_Mods.read_postgrest_conf as pg_conf

"""Important Notes:
You will need to have the Microsoft edge Webdriver installed (and added to PATH) before this will work.
I'm hoping that this will be easy to do on the virtual machine as well.
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH
"""

""" Notes 08042024
Adapated the curl requests to use text/csv and used panadas to.csv
used pandas to cooerce fields to numeric to drop strings.
found was using measurement_unit when field name in postgres is measure_unit
the csv importer appeared to import all non-string obs_values into the dataset successfully.


"""
download_dir = os.path.dirname(os.path.realpath(__file__))
lawa_url = "https://www.lawa.org.nz/download-data/"


def lawa_download_link_groundwater():
    """This Function goes to the lawa downloads page, clicks download, then graps the download link of the 
    confirm button (this makes sure we have the latest dataset). It returns a string url"""
    # Currently this is hardcoded to look for the Groundwater quality dataset on the lawa downloads page
    driver = webdriver.Edge()
    driver.get(lawa_url)
    ground_water_xpath = """//*[@id="body"]/div[2]/div/div/div[4]/div[1]/div/a"""
    driver.find_element(By.XPATH, ground_water_xpath).click()
    confirm_xpath = """//*[@id="download-data-gwquality-dataset"]/div[1]/div/a"""
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, confirm_xpath)))
    # element.find_element(By.XPATH, confirm_xpath).click()
    exel_file_download_link = element.get_attribute('href')
    # print(exel_file_download_link)

    driver.quit()
    return exel_file_download_link


def download_excel_workbook(url):
    """Function that takes the url download link of a file, and then returns a dictionary of worksheet:pandas df pairs"""
    print(f"Downloading content from {url}")
    response = requests.get(url)
    content_type = response.headers.get('Content-Type')
    assert 'excel' in content_type or url.endswith(('.xls', '.xlsx'))
    file_path = "Lawa_ground_water-" + str(date.today()) + ".xlsx"
    with open(file_path, 'wb') as f:  # Its safer to write the dataset to disk first, then read it into pandas
        f.write(response.content)
        df = pd.read_excel(file_path)
    print("File written")
    dfs = pd.read_excel(file_path, sheet_name=None)

    return dfs


def read_data_only(file_path):
    """
    Function that only reads the link
    this will be adapted to format the sheets for curl use.
    :return: dfs which is a variable that might involve columns at a later stage.
    """
    dfs = pd.read_excel(file_path, sheet_name=None)
    return dfs


# dataset_link = lawa_download_link_groundwater()
#
# dfs = download_excel_workbook(dataset_link)

# modification to just read the file takes same string as the downloader

""" Jacobs test"""
# original
# data_file = "Lawa_ground_water-" + str(date.today()) + ".xlsx"
# test
data_file = "Lawa_ground_water-2024-04-01" + ".xlsx"
dfs = read_data_only(data_file)

for sheet_name, df in dfs.items():  # dfs is a dictionary of workbook:pandas.df pairs
    if sheet_name == "State Results":
        print(f"Working on Sheet name: {sheet_name}")
        # example of getting location {'measure_unit': df.loc[:, "measure"], 'obs_value': df.loc[:,"median"]}
        # print(f"{df.loc[:, ["Indicator", "Units", "State"]]}")
        # df.loc[:, ["Indicator", "Units", "State"]]
        curl_data = pd.DataFrame(
            {"measurement_unit": df.loc[:, "Indicator"], "Units": df.loc[:, "Units"], "obs_value": df.loc[:, "State"]})
        # print(curl_data)
    # print(df.head())

curl_token = pg_conf.open_pg_conf("pgrest_conf/test_curl_post.sh", "TOKEN")
url = 'http://localhost:3000/data'


def db_commit(db_data):
    # data = HTTPHeaderDict()
    # for key,value in db_data.items():
    #     data.add(f'{key}', f'{value}')
    print(db_data)
    print(type(db_data))
    headers = {
        'Authorization': f'Bearer {curl_token}',
        'Content-Type': 'text/csv'

    }
    """
    text/csv example
    first row = fields
    second row = columns
    """

    """ commit data to the actual database """
    # print(db_data)
    print(type(db_data))
    # db_data = """obs_value,measure_unit\n10.5,Chlorine\n200.5, Magnesium'"""
    # db_data = """obs_value,measure_unit\nDetect,E.coli\n287.55,Electrical conductivity\n11.25,Nitrate nitrogen\n18.35,Chloride\n"""
    print(db_data)
    r = requests.post(url,
                      headers=headers,
                      data=db_data  # from payload_data
                      )
    print(r.status_code)


def prepare_data(dataset):
    """
    Commit data to the dataset
    function takes a dictionary and inserts the appropriate variables for
    requests to post the data to the table called data under schema db_access
    :param dataset:
    :return:
    """
    # payload_data = []
    # print(dataset)
    # convert to dictionary
    # dataset = dataset.to_csv()
    # drop fields with detect
    drop_fields = ['Detect', 'NonDetect']

    dataset['obs_value'] = pd.to_numeric(dataset['obs_value'], errors='coerce')
    # Drop rows where 'obs_value' is NaN (i.e., rows with non-numeric values)
    dataset = dataset.dropna(subset=['obs_value'])

    payload_data = pd.DataFrame(
        {
            'obs_value': dataset["obs_value"],
            'measure_unit': dataset["measurement_unit"]
        }
    ).to_csv(index=False)

    print(payload_data)
    # problem with obs time.
    m_unit = []
    obs_value = []
    # shape the dataset for pandas dataframe.

    # for key, value in dataset.items():
    #     # get the appropriate fields.
    #     # ignoring detect for now
    #     if isinstance(value["obs_value"], (int, float)):
    #         m_unit.append(value["measure_unit"])
    #         obs_value.append(value["obs_value"])
    # payload_data = pd.
    # payload_data.to_csv('csv_data.csv')
    db_commit(payload_data)


prepare_data(curl_data)
