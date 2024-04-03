import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from utils.config import Config

class TestProductDetails(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=Config.CHROME_DRIVER_PATH)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_view_product_details(self):
        self.driver.get(Config.BASE_URL)

        # Scroll down the page
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

        # Wait for the page to load
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "xpath=//div[@id='__next']/div[2]/main/div/div[3]/div/div[3]/ul")))

        # Locate the product element and click on it
        product_element = self.driver.find_element(By.XPATH, "xpath=//div[@id='__next']/div[2]/main/div/div[3]/div/div[3]/ul")
        product_element.click()

        # Wait for the product details page to load
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'product_details')))

        # Assert that the product details are displayed correctly
        product_name_element = self.driver.find_element(By.ID, 'product_name')
        product_price_element = self.driver.find_element(By.ID, 'product_price')
        # Add more assertions as needed for other product details

        self.assertTrue(product_name_element.is_displayed())
        self.assertTrue(product_price_element.is_displayed())
        # Add more assertions as needed to validate product details

if __name__ == '__main__':
    unittest.main()
