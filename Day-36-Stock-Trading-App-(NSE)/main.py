import requests
from twilio.rest import Client
import os
import time

TWILIO_SID = os.environ.get("SID_KEY")
TWILIO_AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"

COMPANY_STOCKS = {
    "ICICIBANK.NS": "ICICI Bank Ltd",
    "TATACONSUM.NS": "Tata Consumers Products Ltd",
    "HDFCBANK.NS": "HDFC Bank Ltd",
    "ONGC.NS": "Oil and Natural Gas Corporation Ltd",
    "WIPRO.NS": "Wipro Ltd",
    "TCS.NS": "Tata Consultancy Services Ltd",
    "BPCL.NS": "Bharat Petroleum Corporation Ltd",
    "DRREDDY.NS": "Dr.Reddy's Laboratories Ltd",
    "INFY.NS": "Infosys Ltd",
    "LT.NS": "Larsen & Toubro Ltd",
}
# -------------------- STOCK API FETCHING --------------------- #
for stock_name in COMPANY_STOCKS:

    # ##### THIS LINK WAS WORKING EARLIER BUT NOW IT'S SHOWING ERROR MESSAGE:- AVAILABLE FOR PREMIUM MEMBERS ONLY
    # #####
    # stock_parameters = {
    #   "timeseries": 5,
    #   "apikey": os.environ.get("STOCK_API_KEY") }
    # response = requests.get(
    #   url=f"https://fmpcloud.io/api/v3/historical-price-full/" + stock_name,
    #   params=stock_parameters
    # )
    # ############################################################################################################# #

    stock_parameters = {
        "period": 10,
        "type": "ema",
        "apikey": os.environ.get("STOCK_API_KEY")
    }

    response = requests.get(
        url=f"https://fmpcloud.io/api/v3/technical_indicator/daily/" + stock_name,
        params=stock_parameters
    )
    response.raise_for_status()
    data = response.json()

    yesterday_data = data[0]
    yesterday_opening_price = yesterday_data["open"]
    yesterday_closing_price = yesterday_data["close"]
    yesterday_date = yesterday_data["date"]
    yesterday_change = (yesterday_closing_price - yesterday_opening_price) / yesterday_opening_price
    yesterday_change_percent = yesterday_change * 100
    if yesterday_change_percent > 0:
        yesterday_change_up_down = "🔺"
    else:
        yesterday_change_up_down = "🔻"
    print(yesterday_change_percent)
    print(yesterday_closing_price)

    day_before_yesterday_data = data[1]
    day_before_yesterday_opening_price = day_before_yesterday_data["open"]
    day_before_yesterday_closing_price = day_before_yesterday_data["close"]
    day_before_yesterday_date = day_before_yesterday_data["date"]
    day_before_yesterday_change = (day_before_yesterday_closing_price - day_before_yesterday_opening_price) / day_before_yesterday_opening_price
    day_before_yesterday_change_percent = day_before_yesterday_change * 100
    if day_before_yesterday_change_percent > 0:
        day_before_change_up_down = "🔺"
    else:
        day_before_change_up_down = "🔻"
    print(day_before_yesterday_change_percent)
    print(day_before_yesterday_closing_price)

    # Finding the positive difference between 1 and 2
    difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
    if difference > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    diff_percent = (difference / float(day_before_yesterday_closing_price)) * 100
    print(diff_percent)

    stock_msg = f"{stock_name} --> {COMPANY_STOCKS[stock_name]}\n" \
                f"{yesterday_date}: {yesterday_change_up_down}{'{:.3f}'.format(yesterday_change_percent)}%\n" \
                f"{day_before_yesterday_date}: {day_before_change_up_down}" \
                f"{'{:.3f}'.format(day_before_yesterday_change_percent)}%" \
                f"\n Market Indication: {up_down}{'{:.2f}'.format(diff_percent)}%"

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=stock_msg,
        from_=os.environ.get("FROM_NUMBER"),
        to=os.environ.get("TO_NUMBER")
    )
    print(message.status)
    time.sleep(6)
time.sleep(20)

# ----------------------------------- NEWS API FETCHING ------------------------------------ #
news_parameters = {
    "country": "in",
    "category": "business",
    "apiKey": os.environ.get("NEWS_API_KEY")
}

news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()
articles = news_response.json()["articles"]
ten_articles = articles[:10]

formatted_articles = [f"🏷️Headline ➡️: {article['title']}."
                      f"\n🏷️Description ➡️: {article['description']}" for article in ten_articles]
print(formatted_articles)

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_=os.environ.get("FROM_NUMBER"),
        to=os.environ.get("TO_NUMBER")
    )
    print(message.status)
    time.sleep(4)
