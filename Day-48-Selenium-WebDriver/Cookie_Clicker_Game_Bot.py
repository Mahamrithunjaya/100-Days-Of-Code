import time

from selenium import webdriver

# Initiate Selenium
chrome_driver_path = "C:\Development_Driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

game_url = driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

# Get cookies to click on.
cookie = driver.find_element_by_id("cookie")

# Get id's of the item to Upgrade.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time()
five_min = time.time() + 60*5

while True:
    cookie.click()

    # For Every 1 seconds
    if time.time() - timeout >= 2:

        try:
            # Get all upgrade form <b> tag
            all_prices = driver.find_elements_by_css_selector("#store b")
            item_prices = []

            # Convert <b> text into an integer
            for price in all_prices:
                element_text = price.text
                if element_text != "":
                    element_cost = int(element_text.split("-")[1].strip().replace(",", ""))
                    item_prices.append(element_cost)

            # Create dictionary of store items and prices
            cookie_upgrades = {}
            for n in range(len(item_prices)):
                cookie_upgrades[item_prices[n]] = item_ids[n]

            # Get the current cookie Count
            money_element = driver.find_element_by_id("money").text
            if "," in money_element:
                money_element = money_element.replace(",", "")
            cookie_count = int(money_element)

            # Find upgrades that we can currently afford
            affordable_upgrades = {}
            for cost, id_ in cookie_upgrades.items():
                if cookie_count > cost:
                    affordable_upgrades[cost] = id_

            # print(affordable_upgrades)

            # Purchase the most expensive affordable upgrade
            highest_price_affordable_upgrade = max(affordable_upgrades)
            # print(highest_price_affordable_upgrade)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element_by_id(to_purchase_id).click()
        except ValueError:
            pass
        # Adding another 1 second until the next check
        timeout = time.time()

    # After 5 minutes stop the bot and check the cookies per second count
    if time.time() > five_min:
        cookie_per_second = driver.find_element_by_id("cps").text
        print(cookie_per_second)
        break
