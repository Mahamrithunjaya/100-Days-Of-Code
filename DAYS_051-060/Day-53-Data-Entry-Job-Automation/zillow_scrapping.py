from bs4 import BeautifulSoup
import requests


URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22" \
      "%3A%7B%22west%22%3A-122.8563026328125%2C%22east%22%3A-122.0103553671875%2C%22south%22%3A37.627519442100244%2C" \
      "%22north%22%3A37.92276869053922%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B" \
      "%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22" \
      "%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C" \
      "%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22" \
      "%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D "

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/90.0.4430.93 Safari/537.36",
    "Accept-Language": "en-US"
}


class ZillowScrapper:
    def __init__(self):
        self.houses_data = []

    def get_houses_data(self):
        response = requests.get(url=URL, headers=HEADERS)
        response.raise_for_status()
        website_data = response.text

        soup = BeautifulSoup(website_data, "html.parser")
        # print(soup.prettify())

        houses_card = soup.findAll(name="div", class_="list-card-info")

        self.houses_data = [{
            "price": house.findChild(name="div", class_="list-card-price").text[:6],
            "url": house.findChild(name="a").get("href") if house.findChild(name="a").get("href").startswith("h")
            else f"https://www.zillow.com/{house.findChild(name='a').get('href')} ",
            "address": house.findChild(name="address").text
        } for house in houses_card]

        return self.houses_data
