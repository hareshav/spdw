import requests
import json
def get_playlist_songs(playlist_id, access_token):
    headers = {'Authorization': 'Bearer '+access_token}
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    response = requests.get(url, headers=headers)
    playlist_data = json.loads(response.text)
    # print(playlist_data)
    return playlist_data['items']

playlist_id = '31KX9NowUb4lvDRGSykddb'
access_token = "BQBkW1k4LCMsv9bN7y2jqyBpUg01lROOC2hVizw09WtEmdXfIj1XEY-9Ue0DU-2mk573yJHNRYu7cn2c2xN3s4f0ZA7Fj_8iBXVsmYj_CWf-OZwDKmNrabk4gn7mLxYm0dgwYePzGWhkuPG_tUNU0y8AEiRMlU7NSGpcVrCQM66xrYOKOCoHqx8O3QxVD1i3nRqYYNJAwnJFyXgyyceXb9bMjqwYgNlcezzSbVRhlxYHDqOnvCHQ9HTZ5I_R5RS8in9uhM3p1_rlIz11r2asoShw"
songs = get_playlist_songs(playlist_id, access_token)
for song in songs:
    track = song['track']
    print(track['name'], 'by', track['artists'][0]['name'])