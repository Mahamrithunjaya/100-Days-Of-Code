import pandas as pd
from bs4 import BeautifulSoup
import requests

records = []

first_page_endpoint = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
next_page_endpoint = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/"
response = requests.get(first_page_endpoint)
response.raise_for_status()
website_data = response.text

soup = BeautifulSoup(website_data, "html.parser")
# print(soup.prettify())


# ############################# Finding the Total Page Numbers ############################## #
inner_buttons = soup.find_all("div", {"class": "pagination__btn--inner"})
page_numbers = [inner_button.getText() for inner_button in inner_buttons if inner_button.getText().isnumeric()]
total_pages = int(max(page_numbers))
# print(page_numbers)
# print(total_pages)

# ############################ Getting Data From Table ####################################### #
for current_page in range(total_pages):
    if current_page == 0:
        data = website_data
    else:
        response = requests.get(next_page_endpoint+str(current_page + 1))
        response.raise_for_status()
        data = response.text

    soup = BeautifulSoup(data, "html.parser")

    rows = soup.select("table.data-table tbody tr")
    for row in rows:
        cells = row.select("span.data-table__value")
        record = {
            "Major": cells[1].getText(),
            "Early Career Pay": float(cells[3].getText().strip("$").replace(",", "")),
            "Mid-Career Pay": float(cells[4].getText().strip("$").replace(",", "")),
            "% High Meaning": cells[5].getText(),
        }
        records.append(record)

    # ################ Another Way to Scrape the data from the Table given in the website ################## #
    #
    # This Code will start from Line 35
    #
    # majors = soup.findAll(class_='data-table__row')
    # for major in majors:
    #     records.append({
    #         "Major": major.select('td:nth-of-type(2) > span.data-table__value')[0].text,
    #         "Early Career Pay": major.select('td:nth-of-type(4) > span.data-table__value')[0].text,
    #         "Mid-Career Pay": major.select('td:nth-of-type(5) > span.data-table__value')[0].text,
    #         "% High Meaning": major.select('td:nth-of-type(6) > span.data-table__value')[0].text
    #     })

pd.DataFrame(records).to_csv("salaries_by_college_major_updated.csv", index=False)
