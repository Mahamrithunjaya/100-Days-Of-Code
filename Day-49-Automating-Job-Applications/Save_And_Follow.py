import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


# -------------------- Initiate Selenium -------------------- #
chrome_driver_path = "C:\Development_Driver\chromedriver.exe"
# Configure Chrome to open in fullScreen / kiosk mode.
options = webdriver.ChromeOptions()
options.add_argument("--kiosk")
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)


# -------------------- Load search results and login. -------------------- #
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102257491&keywords=python%20developer&location"
           "=London%2C%20England%2C%20United%20Kingdom&sortBy=R")

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

# Wait for the next page to load
time.sleep(5)

email_field = driver.find_element_by_id("username")
email_field.send_keys(os.environ.get("USERNAME"))

password_field = driver.find_element_by_id("password")
password_field.send_keys(os.environ.get("PASSWORD"))
password_field.send_keys(Keys.ENTER)
time.sleep(4)

# not_now = driver.find_element_by_link_text("Not now")
# not_now.click()

# remember_me = driver.find_element_by_link_text("Remember")
# remember_me.click()

# min_msg_bubble = driver.find_element_by_class_name("msg-overlay-bubble-header__details")
# min_msg_bubble.click()
# time.sleep(5)

# -------------------- Retrieve all search results and add to a list. -------------------- #
jobs = driver.find_elements_by_class_name("jobs-search-results__list-item")

# Now For each job in the jobs list, click the Save button, scroll down to the bottom of the right hand pane and then
# click the Follow button.
for job in jobs:
    job.click()
    time.sleep(4)
    print("Job Clicked")
    # Finding SAVE button and click on it.
    try:
        save_button = driver.find_element_by_class_name("jobs-save-button")
        save_button.click()
        print("Saved")
        time.sleep(2)
    except NoSuchElementException:
        print("Already Applied")
        pass

    # Click the right hand rail and scroll down to the bottom of the page to reveal the Follow button.
    job_detail = driver.find_element_by_class_name("jobs-search__right-rail")
    job_detail.click()
    html = driver.find_element_by_tag_name("html")
    html.send_keys(Keys.END)
    time.sleep(5.5)

    # Exception handling for instances in which the company does not have a Follow button.
    try:
        follow = driver.find_element_by_class_name("follow")
        follow.click()
        print("Followed")
        time.sleep(2)
    except NoSuchElementException:
        continue
