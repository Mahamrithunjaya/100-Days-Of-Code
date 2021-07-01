from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
news_web_page = response.text

soup = BeautifulSoup(news_web_page, "html.parser")

# article_tags = soup.find(name="a", class_="storylink")
# article_title = article_tags.getText()
#
# article_link = article_tags.get("href")
#
# # upvote_tag = soup.find(name="span", class_="score")
# # article_upvote = upvote_tag.getText()
# article_upvote = soup.find(name="span", class_="score").getText()

articles = soup.find_all(name="a", class_="storylink")
article_titles = []
article_links = []
for article_tag in articles:
    title = article_tag.getText()
    article_titles.append(title)

    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = []
upvotes = soup.find_all(name="td", class_="subtext")

for score in upvotes:
    is_votes = score.find(name="span", class_="score")

    if is_votes is None:
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(is_votes.string.split()[0]))

print(article_titles)
print(article_links)
print(article_upvotes)
highest_upvote = max(article_upvotes)
highest_index = article_upvotes.index(highest_upvote)
# print(highest_upvote)
# print(highest_index)

print(article_titles[highest_index])
print(article_links[highest_index])
