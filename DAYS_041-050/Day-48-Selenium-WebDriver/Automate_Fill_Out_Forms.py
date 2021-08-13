from selenium import webdriver


chrome_driver_path = "C:\Development_Driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

form_page = driver.get(url="http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Subhajit")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Saha")

email_id = driver.find_element_by_name("email")
email_id.send_keys("londonsaha@gmail.com")

submit_button = driver.find_element_by_tag_name("button")
# submit_button = driver.find_element_by_css_selector("form button")
submit_button.click()
