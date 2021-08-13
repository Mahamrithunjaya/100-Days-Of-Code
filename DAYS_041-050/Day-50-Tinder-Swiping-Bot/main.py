import time
import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys


URL = "https://tinder.com/"
USERNAME = os.environ.get("EMAIL_ID")
PASSWORD = os.environ.get("PASSCODE")

# -------------------- Initiate Selenium -------------------- #
chrome_driver_path = "C:\Development_Driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


# -------------------- Load page and login. -------------------- #

# Loading Tinder URL
driver.get(url=URL)
# Wait for the page to load
time.sleep(15)

# Log in to Tinder request
log_in_button = driver.find_element_by_xpath('//*[@id="c-174738105"]/div/div[1]/div/main/div['
                                             '1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in_button.click()
# Wait for the page to load
time.sleep(4)

try:
    more_options = driver.find_element_by_xpath('//button[normalize-space()="More Options"]')
    more_options.click()
    time.sleep(2)
except NoSuchElementException:
    pass

# Facebook login request
fb_login = driver.find_element_by_xpath(
    '//*[@id="c-1903119181"]/div/div/div[1]/div/div[3]/span/div[2]/button'
)
fb_login.click()
time.sleep(5)

# Base Window
base_window = driver.window_handles[0]

# Switch to Facebook login window
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Login and Hit enter
email_id = driver.find_element_by_xpath('//*[@id="email"]')
email_id.send_keys(USERNAME)
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

# Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

# Delay by 20 seconds to allow page to load.
time.sleep(20)

# --------------- Dealing with the pop-up requests of Tinder Website --------------- #

# Location Pop-Up -> Allowing it
location = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div/div/div[3]/button[1]')
location.click()
time.sleep(5)

# Notification Pop_Up -> Disallowing it
notify = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div/div/div[3]/button[2]')
notify.click()
time.sleep(5)

# Cookies Pop-Up -> Allowing it
try:
    cookies_notify = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
    cookies_notify.click()
    time.sleep(3)
except NoSuchElementException:
    pass


# As Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while
# loop.

for n in range(100):

    # Adding a 3 seconds delay between likes
    time.sleep(3)

    try:
        print("CALLED")
        like_button = driver.find_element_by_xpath(
            '//*[@id="c-174738105"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button'
        )
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            # Catches the cases where there is a "ADD-HOME" pop-up in front of the "Like" button:
            try:
                add_home_dismiss = driver.find_element_by_xpath('//button[normalize-space()="Not interested"]')
                add_home_dismiss.click()
                time.sleep(3)
            except NoSuchElementException:
                # Catches the cases where there is a "LIKE BUYING OPTION" pop-up in front of the "Like" button:
                try:
                    member_option_dismiss = driver.find_element_by_xpath('//button[normalize-space()="No Thanks"]')
                    member_option_dismiss.click()
                    time.sleep(3)
                except NoSuchElementException:

                    time.sleep(1)

            time.sleep(3)

driver.quit()
