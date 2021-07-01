from pprint import pprint
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import os


# ########################## Scraping Billboard 100 ########################## #

BILLBOARD_CHART_URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

BILLBOARD_CHART_DATE_URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url=BILLBOARD_CHART_DATE_URL)
response.raise_for_status()
website_data = response.text

soup = BeautifulSoup(website_data, "html.parser")
# print(soup.prettify())

# song_artists = soup.find(name="span", class_="chart-element__information")
# print(song_name)

song_names = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

song_titles = [song_name.getText() for song_name in song_names]
# print(song_titles)

# ############################ Spotify Authentication ############################ #

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.environ.get("CLIENT_ID"),
        client_secret=os.environ.get("CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# ##################### Searching Spotify for Songs by Title of Song  ##################### #

song_uris = []
year = date.split("-")[0]

for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# ####################### Creating A New Private Playlist In Spotify ####################### #

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", description="Enjoy Music.", public=False)
# print(playlist)

# ######################## Adding Found Songs Into The New PlayList ######################## #

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
