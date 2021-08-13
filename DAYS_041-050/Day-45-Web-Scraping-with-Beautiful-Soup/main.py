from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.p)
# print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
print(section_heading.get("class"))

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(selector=".heading")
print(headings)

# input_tag = soup.find(name="input")
# print(input_tag)
# max_length = input_tag.get("maxlength")
# print(max_length)
