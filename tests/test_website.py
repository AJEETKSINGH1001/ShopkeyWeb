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

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture
def browser():
    # Initialize the WebDriver instance
    driver = webdriver.Chrome(executable_path=Config.CHROME_DRIVER_PATH)
    # Wait for elements up to 10 seconds
    driver.implicitly_wait(10)
    # Return the driver instance to test functions
    yield driver
    # Quit the WebDriver instance after the test
    driver.quit()

@pytest.fixture
def base_page(browser):
    return BasePage(browser)

def test_title(base_page):
    logger.info("Navigating to the website")
    base_page.driver.get(Config.BASE_URL)
    assert "" in base_page.driver.title

def test_login(base_page):
    logger.info("Navigating to the website")
    base_page.driver.get(Config.BASE_URL2)


     # Find country dropdown and select the country code
    country_dropdown = Select( driver.find_element(By.ID, 'country_dropdown'))
    country_dropdown.select_by_visible_text('United States')  # Change this to the desired country

      # Find contact number field and enter contact number
    contact_number_field = self.driver.find_element(By.ID, 'contact_number')
    contact_number_field.send_keys('1234567890')  # Enter the contact number

      # Find password field and enter password
    password_field = self.driver.find_element(By.ID, 'password')
    password_field.send_keys('your_password')  # Enter the password

    # Find login button and click it
    login_button = self.driver.find_element(By.ID, 'login_button')
    login_button.click()


'''
def test_login(base_page):
    logger.info("Navigating to the login page")
    base_page.driver.get(Config.BASE_URL)
    logger.info("Entering login details")
    base_page.wait_for_element(("a", "login")).click()
    #logger.info("Entering username and password")
    base_page.wait_for_element(("name", "Phone Number")).send_keys(Config.USERNAME)
    base_page.wait_for_element(("name", "password")).send_keys(Config.PASSWORD)
    logger.info("Submitting login form")
    base_page.wait_for_element(("name", "Sign with Password")).click()
    # Add assertions or further actions after login as needed
    assert "My Account" in base_page.driver.title'''