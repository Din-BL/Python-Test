from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

class WeatherAppTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5000')

    def test_positive_location_response(self):
        search_box = self.driver.find_element(By.ID, 'location')
        search_box.clear()
        search_box.send_keys('New York')
        search_box.send_keys(Keys.RETURN)
        time.sleep(1) 

        temp_element = self.driver.find_element(By.XPATH, '//h2[contains(text(),"°")]')
        self.assertTrue(temp_element.is_displayed(), "Temperature element should be displayed")

    def test_negative_location_response(self):
        search_box = self.driver.find_element(By.ID, 'location')
        search_box.clear()
        search_box.send_keys('InvalidCityName')
        search_box.send_keys(Keys.RETURN)
        time.sleep(1)  

        error_button = self.driver.find_element(By.XPATH, '//button[text()="Go Home"]')
        self.assertTrue(error_button.is_displayed(), "Error button should be displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
