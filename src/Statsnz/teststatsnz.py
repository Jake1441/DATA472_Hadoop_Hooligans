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

link_statsnz = "https://www.stats.govt.nz/indicators/groundwater-quality"
iframeXPATH = '//*[@id="shinyiframe"]'

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.get(link_statsnz)
#############Navigate to the iframe and the download tab button#################################
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, iframeXPATH)))
download_buttonXPATH = """/html/body/div[1]/nav/div/ul/li[4]/a"""

download_tab = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, download_buttonXPATH)))
new_frame_page = download_tab.get_attribute('href')
#################################################################################################

print(new_frame_page)

driver.close()

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.get(new_frame_page)
time.sleep(5)

download_tab_2_xpath = """/html/body/div[1]/nav/div/ul/li[4]/a"""
download_content_xpath = """//*[@id="download"]"""
download_tab_2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, download_tab_2_xpath))).click()
download_link = driver.find_element(By.ID, 'download')
download_content = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, download_content_xpath))).click()

#driver.execute_script("arguments[0].click();", download_link)

driver.save_screenshot('debug_screenshot.png')
time.sleep(3000)
driver.quit()


