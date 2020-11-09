import spotipy
import io
import re
import datetime
from collections import defaultdict
from credentials import cid, secret
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id = cid, client_secret = secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

date = datetime.date.today()

label_count = defaultdict(int) # key = label name, value = amount of songs across playlists
firefly_songs = set()

output_dir = 'output/output' + ' (' + str(date) + ').txt'
output_file = io.open(output_dir, 'w', encoding = 'utf-8', errors = 'ignore')
firefly_dir = 'firefly_songs/firefly_songs' + ' (' + str(date) + ').txt'
firefly_file = io.open(firefly_dir, 'w', encoding = 'utf-8', errors = 'ignore')

def main():
	filterPlaylists()
	createOutput()
	createFireflyOutput()

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
						if (checkFireflyEntertainment(album_label)):
							track_name = item['track']['name']
							track_artist = item['track']['artists'][0]['name']
							track_all = track_artist + " - " + track_name
							firefly_songs.add(track_all)
						label_count[album_label] += 1
					except TypeError:
						pass
				count += 1
		if playlists['next']:
			playlists = sp.next(playlists)
		else:
			playlists = None

def createOutput():
	total_songs = 0
	label_list = []

	for key, value in label_count.items():
		if (value == None):
			value = 0
		combo = (key, value)
		label_list.append(combo)
	label_list.sort(key = lambda x:x[1])
	label_list.reverse()

	for item in label_list:
		first = ''
		if (item[0] == None):
			first = 'N/A'
		else:
			first = item[0]
		print(first, item[1])
		output_file.write(first + ': ' + str(item[1]) + '\n')
		total_songs += item[1]

	output_file.write('TOTAL SONGS: ' + str(total_songs))

def createFireflyOutput():
	for song in sorted(firefly_songs):
		firefly_file.write(song + '\n')

def checkPlaylist(playlist, playlist_name):
	if (playlist['followers']['total'] > 500000):
		if (playlist_name[:7] != 'This Is'):
			if (playlist_name[:9] != 'I Love My'):
				if (bool(re.search(r'\d', playlist_name)) == False):
					return True
	return False

def checkFireflyEntertainment(label_name):
	if (re.search('Firefly Entertainment', label_name, re.IGNORECASE)):
		return True
	else:
		return False

if __name__ == '__main__':
	main()