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
	filterPlaylists()
	createOutput()

def filterPlaylists():
	playlists =	 sp.user_playlists('spotify')
	count = 1
	while playlists:
		for i, playlist in enumerate(playlists['items']):
			playlist = sp.playlist(playlist['id'])
			playlist_name = playlist['name']
			if (checkPlaylist(playlist, playlist_name) == True):
				print(str(count) + '. ' + playlist_name.upper())
				for item in playlist['tracks']['items']:
					try:
						album_id = item['track']['album']['id']
						album_object = sp.album(album_id)
						album_label = album_object['label']
						label_count[album_label] += 1
					except TypeError:
						pass
				count += 1
		if playlists['next']:
			playlists = sp.next(playlists)
		else:
			playlists = None

def createOutput():
	pass

def checkPlaylist(playlist, playlist_name):
	if (playlist['followers']['total'] > 500000):
		if (playlist_name[:7] != 'This Is'):
			if (playlist_name[:9] != 'I Love My'):
				if (bool(re.search(r'\d', playlist_name)) == False):
					return True
	return False

if __name__ == '__main__':
	main()