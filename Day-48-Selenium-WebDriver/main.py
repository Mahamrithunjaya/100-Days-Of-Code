from selenium import webdriver

chrome_driver_path = "C:\Development_Driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url="https://www.python.org/")

title = driver.find_element_by_css_selector(".medium-widget.event-widget.last h2")
print(title.text)

event_times = driver.find_elements_by_css_selector(".event-widget time")
# for time in event_times:
#     print(time.text)

event_names = driver.find_elements_by_css_selector(".event-widget li a")
# for name in event_names:
#     print(name.text)

# Using List Comprehension
# events_list = {n: {"time": event_times[n].text, "event": event_names[n].text} for n in range(len(event_times))}
# print(events_list)

# Using For Loop
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "event_name": event_names[n].text
    }
print(events)

# driver.close()
driver.quit()
