'''
example from https://www.geeksforgeeks.org/download-file-in-selenium-using-python/
modified by Jacob Reid to work without having to download the chrome executable.
'''


# Import Module
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import from webdriver_manager (using underscore)
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium.webdriver.common.keys import Keys

# Open URL
driver.get(
    'http://demo.automationtesting.in/FileDownload.html')

time.sleep(5)

items = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, 'textbox')))

# Enter text
text_box = driver.find_element(By.ID, 'textbox')
text_box.send_keys("Hello world")

# Generate Text File
generate_txt = driver.find_element(By.ID, 'createTxt')
generate_txt.click()

# Click on Download Button
driver.find_element(By.ID, 'link-to-download').click()
time.sleep(3)
# make sure the driver closes
driver.quit()