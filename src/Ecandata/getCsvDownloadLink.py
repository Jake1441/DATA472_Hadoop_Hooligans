from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from pyvirtualdisplay import Display


def get_csv_download_link(link):
    """This Function takes the well link from the well code (and the ID), and returns the direct download link of the most recent csv report"""
    #with Display(visible=0, size=(1920,1080)):
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)
    water_qual_xpath = """//*[@id="main"]/div/ul/li[5]"""
    water_qual_tab = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, water_qual_xpath))).click()
    table_xpath = """//*[@id="waterQualitySamples"]"""
    table = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, table_xpath)))
    first_link = table.find_element(By.TAG_NAME, 'a').click()
    
    export_data_selector = """#waterQualitySamples > tbody > tr:nth-child(2) > td > div > div > h3 > a.button.button-small.export-sample.pull-right"""
    export_data_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, export_data_selector)))
    export_link = export_data_button.get_attribute('href')
    #print(export_link) 
    driver.quit()   
    return export_link
    