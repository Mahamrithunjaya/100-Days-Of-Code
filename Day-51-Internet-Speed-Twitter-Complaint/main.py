import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 25
PROMISED_UP = 25
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSCODE")
CHROME_DRIVER_PATH = os.environ.get("DRIVER")


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        time.sleep(10)

        # Checking the Internet Speed
        go_button = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
        )
        go_button.click()
        time.sleep(90)

        # Get the UP and DOWN results of Internet Speed
        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
            '1]/div[3]/div/div[2]/span '
        ).get_attribute("textContent")
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
            '1]/div[2]/div/div[2]/span '
        ).get_attribute("textContent")

        print(f"UP SPEED ->  {self.up}  and DOWN SPEED ->  {self.down}")

    def tweet_at_provider(self):
        self.driver.get(url="https://twitter.com/")
        time.sleep(10)

        # Logging In Twitter
        log_in_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]'
        )
        log_in_button.click()
        time.sleep(5)

        # Entering Email and Password
        email_id = self.driver.find_element_by_name("session[username_or_email]")
        email_id.send_keys(TWITTER_EMAIL)
        password = self.driver.find_element_by_name("session[password]")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(10)

        # Finding the Twitter Button And click on it.
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a'
        )
        tweet_button.click()
        time.sleep(5)

        # Finding the Tweet Textbox and Entering the Tweets.
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div['
            '1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div '
        )
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}Mbps down/{self.up}Mbps up when I pay " \
                f"for {PROMISED_DOWN}Mbps down/{PROMISED_UP}Mbps up."
        tweet_compose.send_keys(tweet)
        time.sleep(10)

        # Finding the Tweet Publish Button and Click on it.
        tweet = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div['
            '1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4] '
        )
        tweet.click()
        time.sleep(8)

        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

bot.get_internet_speed()
bot.tweet_at_provider()
