import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_SID = os.environ.get("SID_KEY")
TWILIO_AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

# -------------------- STOCK API FETCHING --------------------- #
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": os.environ.get("STOCK_API_KEY")
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
# Performing list comprehension on Python dictionary
data_list = [value for (key, value) in data.items()]

# Getting yesterday's closing stock price.
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# Getting the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Finding the positive difference between 1 and 2
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Finding the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(day_before_yesterday_closing_price)) * 100
print(diff_percent)

if diff_percent > 0:
    # ----------------------------------- NEWS API FETCHING ------------------------------------ #
    # --------------- AND USING THE NEWS API TO GET ARTICLES RELATED TO THE COMPANY_NAME ---------------- #
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": os.environ.get("NEWS_API_KEY")
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

    if len(articles) > 3:
        three_articles = articles[:3]
        print(three_articles)
        formatted_articles = [f"{STOCK_NAME}: {up_down}{'{:.2f}'.format(diff_percent)}%\nHeadLine: {article['title']}."
                              f"\n\nBrief: {article['description']}" for article in three_articles]

    else:
        print(articles)
        formatted_articles = [f"{STOCK_NAME}: {up_down}{'{:.2f}'.format(diff_percent)}%\nHeadLine: {article['title']}."
                              f"\n\nBrief: {article['description']}" for article in articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=os.environ.get("FROM_NUMBER"),
            to=os.environ.get("TO_NUMBER")
        )
        print(message.status)
