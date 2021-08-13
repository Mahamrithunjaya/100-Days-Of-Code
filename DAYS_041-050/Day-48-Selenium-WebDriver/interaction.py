from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development_Driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_element_by_css_selector("#articlecount a")
# print(articles.text)

# ########## CLick on the link by holding the <a> tag ########## #
# articles.click()

# ########## Click on the link text by using find method ########## #
portals = driver.find_element_by_link_text("All portals")
# portals.click()

# ########## Automated Typing ########## #
# Finding the SEARCH bar
search = driver.find_element_by_name("search")
# Typing in "Python"
search.send_keys("Python")
# Then Hitting the ENTER key
search.send_keys(Keys.ENTER)
