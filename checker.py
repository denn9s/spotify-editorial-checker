import spotipy
import io
import re
from collections import defaultdict
from credentials import cid, secret
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id = cid, client_secret = secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

label_count = defaultdict(int) # key = label name, value = amount of songs across playlists

output_file = io.open('output.txt', 'w', encoding = 'utf-8', errors = 'ignore')

def main():
	playlists =	 sp.user_playlists('spotify')
	count = 1
	while playlists:
		for i, playlist in enumerate(playlists['items']):
			playlist = sp.playlist(playlist['id'])
			playlist_name = playlist['name']
			if (checkPlaylist(playlist, playlist_name) == True):
				pass
		if playlists['next']:
			playlists = sp.next(playlists)
		else:
			playlists = None

def checkPlaylist(playlist, playlist_name):
	if (playlist['followers']['total'] > 500000):
		if (playlist_name[:7] != 'This Is'):
			if (playlist_name[:9] != 'I Love My'):
				if (bool(re.search(r'\d', playlist_name)) == False):
					return True
	return False

if __name__ == '__main__':
	main()