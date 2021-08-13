import json
from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
website_data = response.text

soup = BeautifulSoup(website_data, "html.parser")
# print(soup.prettify())


# ############################### MOVIE NAME LIST  ################################## #

script_text = soup.find(name="script", type="application/json")
json_text = script_text.string
bs4_dict = json.loads(json_text)
html_dict = bs4_dict["props"]["pageProps"]["apolloState"]

movie_names = [value["titleText"] for (key, value) in html_dict.items() if "ImageMeta" in key[0:9]]

# for key, value in html_dict.items():
#     if "ImageMeta" in key[0:9]:
#         movie_names.append(value["titleText"])
# print(movie_names[::-1])

movie_titles = movie_names[::-1]


# ############################### MOVIE YEAR LIST  ################################## #

movie_article = soup.find_all(name="div", class_="jsx-3821216435 listicle-item")
movie_year = []
for year in movie_article:
    is_year = year.select_one("p strong")
    is_link = year.select_one("p strong a")
    if is_link:
        movie_year.append("NA")
    elif is_year is None:
        movie_year.append("NA")
    elif is_year:
        movie_year.append(is_year.getText())

movie_year = movie_year[::-1]

# print(movie_year)
# print(movie_titles)

# ########################## CREATING AND WRITING TO A FILE  ############################ #

year_index = 0

try:
    with open(file="top_100_movies.txt", mode="a") as file:
        for movie in movie_titles:
            file.writelines(f"{movie} --> Released Year: {movie_year[year_index]}\n")
            year_index += 1

except FileNotFoundError:
    with open(file="top_100_movies.txt", mode="w") as file:
        for movie in movie_titles:
            file.writelines(f"{movie} --> Released Year: {movie_year[year_index]}\n")
            year_index += 1
