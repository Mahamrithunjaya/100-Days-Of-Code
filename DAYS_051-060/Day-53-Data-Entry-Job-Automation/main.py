from zillow_scrapping import ZillowScrapper
from automation_form_fillup import DataEntryAutomation


zillow_scrapper = ZillowScrapper()
houses = zillow_scrapper.get_houses_data()
print(houses)

form_automation = DataEntryAutomation()

for house in houses:
    form_automation.send_form(house)

form_automation.driver.quit()
