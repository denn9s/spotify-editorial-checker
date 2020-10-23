import spotipy
from collections import defaultdict
from credentials import cid, secret
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id = cid, client_secret = secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

label_count = defaultdict(int) # key = label name, value = amount of songs across playlists

playlists = sp.user_playlists('spotify')
count = 1
while playlists:
	for i, playlist in enumerate(playlists['items']):
		pass
	if playlists['next']:
		playlists = sp.next(playlists)
	else:
		playlists = None
