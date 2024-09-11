# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:15:25 2024

@author: dell
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your chromedriver executable
# CHROMEDRIVER_PATH = '/path/to/chromedriver'
CHROMEDRIVER_PATH=r"D:/chromedriver.exe"#-.------------- TO EDIT


# Set up Selenium options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode (no GUI)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Initialize the WebDriver
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open the BBC News website
    driver.get('https://www.bbc.com/news')

    # Wait for the headlines to be present in the DOM
    wait = WebDriverWait(driver, 10)

    # Use the updated selector based on data-testid attribute
    headlines_elements = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h2[data-testid="card-headline"]'))
    )

    # Print out all headlines
    for element in headlines_elements:
        print(element.text)

finally:
    # Close the WebDriver
    driver.quit()


