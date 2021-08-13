import requests
import lxml
from re import sub
from decimal import Decimal
import smtplib
import os
from bs4 import BeautifulSoup


MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
RECIPIENT_EMAIL = os.environ.get("RECIPIENT_EMAIL")

# ################################## REQUESTING DATA FROM WEBSITE ################################## #

URL = "https://www.amazon.in/Logitech-Gaming-Mouse-Mechanical-Keyboard/dp/B07XPBPDGY/ref=lp_21702871031_1_3"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/90.0.4430.93 Safari/537.36",
}

response = requests.get(url=URL, headers=headers)
response.raise_for_status()
website_data = response.text


# ######################################## WEBSITE SCRAPING ######################################## #
soup = BeautifulSoup(website_data, "lxml")
print(soup.prettify())

# PRODUCT TITLE
product_title = soup.find(id="productTitle").getText().strip()
print(product_title)

# PRODUCT PRICE
price = soup.find(id="priceblock_ourprice").getText()
print(price)
# price_without_currency = price.split("₹")[1]
# print(price_without_currency)
final_price = Decimal(sub(r'[^\d.]', '', price))
print(final_price)


# SETTING PRODUCT BUYING PRICE
PRODUCT_BUYING_PRICE = 10000.00


# #################################### CHECKING PRICE AND SEND EMAIL #################################### #

# CHECKING IF THE CURRENT PRICE MATCHES WITH MY BUYING PRICE
if final_price <= PRODUCT_BUYING_PRICE:
    message = f"{product_title} is now {price}"

    # IF MATCHES THEN SEND EMAIL TO ME.
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIPIENT_EMAIL,
            msg=f"From: \"{os.environ.get('SENDER_NAME')}\"<{MY_EMAIL}>\n"
                f"To: {RECIPIENT_EMAIL}\n"
                f"Subject: Amazon Price Alert ‼‼‼\n\n{message}\n{URL}".encode("utf-8")
        )
