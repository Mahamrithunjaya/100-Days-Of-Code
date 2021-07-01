import os
import time

from selenium import webdriver


CHROME_DRIVER_PATH = os.environ.get("DRIVER")


class DataEntryAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.maximize_window()

    def send_form(self, house):
        self.driver.get(url=os.environ.get("GOOGLE_FORM"))
        time.sleep(3)

        property_address = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )
        property_address.send_keys(house['address'])
        time.sleep(1)

        price = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )
        price.send_keys(house['price'])
        time.sleep(1)

        property_link = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )
        property_link.send_keys(house['url'])
        time.sleep(1)

        submit_button = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div'
        )
        submit_button.click()
