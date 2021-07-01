import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

CHROME_DRIVER_PATH = os.environ.get("DRIVER")
SIMILAR_ACCOUNT = "geeks_for_geeks"
USERNAME = os.environ.get("INSTAGRAM_EMAIL")
PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.counter_followers = 0
        self.all_followers = 0
        self.driver.maximize_window()

    def login(self):
        # Log In page
        self.driver.get(url="https://www.instagram.com/accounts/login/")
        time.sleep(8)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(3)
        password.send_keys(Keys.ENTER)
        time.sleep(10)

        # Checking whether there is any Login Info PopUp came in front
        # If came then don't save Login Data
        try:
            login_info = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
            login_info.click()
            time.sleep(8)
        except NoSuchElementException:
            pass

        # Checking whether there is any Notification PopUp came in front
        # If came then Don't accept notification
        try:
            notification_popup = self.driver.find_element_by_xpath('//button[normalize-space()="Not Now"]')
            # notification_popup = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
            notification_popup.click()
            time.sleep(5)
        except NoSuchElementException:
            pass

    def find_followers(self):
        time.sleep(5)

        self.driver.get(url=f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(5)

        # Receive all amount followers from target user
        self.all_followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span'
        ).get_attribute("title").replace(',', '')
        self.all_followers = int(self.all_followers)
        print(f"All followers - {self.all_followers}")

        # Open body with users followers
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        )
        followers.click()
        time.sleep(10)

    def follow(self):
        # Find number of unlocked follow fields
        follow_button_list = self.driver.find_elements_by_css_selector("li button")

        # Sort out every follower from current followers_list, beginning at counter_followers
        for follow_button in range(self.counter_followers, len(follow_button_list)):

            if follow_button_list[follow_button].text == "Follow":
                try:
                    self.counter_followers += 1
                    follow_button_list[follow_button].click()
                    print("Followed")
                    time.sleep(4)
                except ElementClickInterceptedException:
                    print("ElementClickInterceptedException")
                    pass
            else:
                self.counter_followers += 1
                continue

        # Find the followers window
        popup_window = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        # Scroll down the page(mouse down)
        for i in range(2):
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', popup_window
            )
            time.sleep(3)

        # If followers from target username was end - driver.quit or restart follow()
        if self.counter_followers + 1 >= self.all_followers:
            print(f"100 followers from {SIMILAR_ACCOUNT} with {self.all_followers} was done.")
            self.driver.quit()
        else:
            self.follow()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
