from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.service import Service
import os
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def lawa_download_link_groundwater():
    lawa_url = "https://www.lawa.org.nz/download-data/"
    """This Function goes to the lawa downloads page, clicks download, then graps the download link of the 
    confirm button (this makes sure we have the latest dataset). It returns a string url"""
    #Currently this is hardcoded to look for the Groundwater quality dataset on the lawa downloads page
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    download_dir = os.path.join(os.getcwd(), 'LawaDownloads')
    os.makedirs(download_dir, exist_ok=True)

    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.get(lawa_url)

    ground_water_xpath = """//*[@id="body"]/div[2]/div/div/div[4]/div[1]/div/a"""
    driver.find_element(By.XPATH, ground_water_xpath).click()
    confirm_xpath = """//*[@id="download-data-gwquality-dataset"]/div[1]/div/a"""
    element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, confirm_xpath))).click()
    #element.find_element(By.XPATH, confirm_xpath).click()
    #exel_file_download_link = element.get_attribute('href')
    #print(exel_file_download_link)
    time.sleep(100)
    driver.quit()
    return True

#lawa_download_link_groundwater()