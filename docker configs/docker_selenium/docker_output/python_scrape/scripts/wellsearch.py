"""This is intended to be run as a module"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
import os
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests
import csv
#########
from pyvirtualdisplay import Display


display = Display(visible=0, size=(1200, 800))
display.start()

def get_obs_link(well_code):
    """This function takes a well code and returns the url (and the ID) of the most recent water quality report"""
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1200x800")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    baseurl = "https://www.ecan.govt.nz/data/well-search/"

    driver.get(baseurl)

    input_field_xpath = """//*[@id="WellsSearchForm-keywords"]"""
    input_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, input_field_xpath)))
    input_field.send_keys(well_code)
    input_field.send_keys(Keys.RETURN)

    table_xpath = """//*[@id="well-search-results"]"""
    table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, table_xpath)))
    first_link = table.find_element(By.TAG_NAME, 'a')

    link_href = first_link.get_attribute('href')
    link_text = first_link.text
    driver.quit()
    return link_href, link_text


def get_csv_download_link(link, ID):
    """This Function takes the well link from the well code (and the ID), and returns the direct download link of the most recent csv report"""
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1200x800")
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.get(link)
    water_qual_xpath = """//*[@id="main"]/div/ul/li[5]"""
    water_qual_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, water_qual_xpath))).click()
    table_xpath = """//*[@id="waterQualitySamples"]"""
    table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, table_xpath)))
    first_link = table.find_element(By.TAG_NAME, 'a').click()

    export_data_selector = """#waterQualitySamples > tbody > tr:nth-child(2) > td > div > div > h3 > a.button.button-small.export-sample.pull-right"""
    export_data_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, export_data_selector)))
    export_link = export_data_button.get_attribute('href')
    #print(export_link)    
    return export_link, ID


def download_excel_workbook(url, ID):
    """Takes the url of the direct csv download link (and the ID) and downloads the csv into a folder called well_data"""
    directory = os.getcwd()
    if not os.path.basename(directory) == 'well_data':
        os.makedirs('well_data', exist_ok=True)
        os.chdir('well_data')
        directory = os.getcwd()

    print(f"Downloading content from {url}")
    response = requests.get(url)
    print(url.endswith)
    new_id = ID.replace('/', '-')
    file_path = os.path.join(directory, f'{new_id}.csv')
    with open(file_path, 'wb') as f: #Its safer to write the dataset to disk first, then read it into pandas
        f.write(response.content)
    return 1


def get_and_download_well_info(codes):
    """Main function for this script, brings everyone together. Given a list-like of well codes, it will create a folder called well_data and download the most recent csv reports into that folder"""
    for code in codes:
        try:
            well_link, ID = get_obs_link(code)
            csv_link, ID = get_csv_download_link(well_link, ID)
            download_excel_workbook(csv_link, ID)
        except Exception as e:
            print(f"There was an error: {e} when trying to download the code: {code}")
    return 1

display.stop()
example_codes = ['I39/0007',
                 'H38/0004',
                 'J40/0217',
                 'N33/0212',
                 'K37/0243',
                 'CB19/5076',
                 'K38/0066',
                 'K38/0066',
                 'BW24/0274'] # Some codes for testing if you want to

# get_and_download_well_info(example_codes)