from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

# Optionally uncomment the next line for interactive input
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
billboard_page = response.text

soup = BeautifulSoup(billboard_page, "html.parser")
list_of_songs = soup.find_all(attrs={'class': 'o-chart-results-list-row-container'})

song_list = []
for song in list_of_songs:
    song_list.append(song.h3.getText().strip())

Client_ID = "831299fa7b1f4193aa61f1e94526d248"
Client_Secret = "ce13ac4df8fe4f8bb48c56399f6e6fa3"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Client_ID,
                                               client_secret=Client_Secret,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private playlist-modify-public",
                                               show_dialog=True,
                                               cache_path='token.txt',
                                               username="Pantvedant7"))

user_id = sp.current_user()["id"]

year = date.split("-")[0]

songs_uris = []
for name in song_list:
    query = f"track: {name} year: {year}"
    songs = sp.search(q=query, type="track", limit=1)
    tracks = songs["tracks"]["items"]
    if tracks:
        uri = tracks[0]["uri"]
        songs_uris.append(uri)
    else:
        print(f"song '{name}' not found in spotify in {year}.")

pprint.pp(songs_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100",
                                   description="this playlist charts billboard "
                                               "top 100 songs for the mentioned date")

add_tracks = sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"],tracks=songs_uris)
print(add_tracks)
