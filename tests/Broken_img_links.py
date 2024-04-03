import pytest
from selenium import webdriver
from pages.base_page import BasePage
from utils.config import Config
import logging
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import Config
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def check_broken_images_and_links(url):
    # Initialize Chrome WebDriver
    # Specify the path to Chromedriver
    chromedriver_path = 'C:\\chromedriver.exe'

    # Initialize Chrome WebDriver with the specified path
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.get(url)

    # Find all images on the webpage
    images = driver.find_elements(By.TAG_NAME, "img")

    # Check each image source
    print("Checking for broken images:")
    for image in images:
        src = image.get_attribute("src")
        response = requests.head(src)
        if response.status_code != 200:
            print(f"Broken image found: {src}")

    # Find all links on the webpage
    links = driver.find_elements(By.TAG_NAME, "a")

    # Check each link URL
    print("Checking for broken links:")
    for link in links:
        href = link.get_attribute("href")
        if href:
            response = requests.head(href)
            if response.status_code != 200:
                print(f"Broken link found: {href}")

    # Close the WebDriver
    driver.quit()

# Example usage
check_broken_images_and_links("https://test0106store1a.goshopkey.com/")
