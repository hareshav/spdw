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
token = 'BQB4OC5KWkNAeZSGHKMm-ig6nDOrLzkoAPJvtXVZMfOZHkE1A1IKtvd_Hn-D3dQAof_1kqWN9zwTDiorjW7c8Im9PrREGMgYon5S4YgVvtDI7EyLNRe2W5ydE1lAJjxfQy-ExUC4JyONLBQQKVJ5K2vi1rWckakxzm6c_5DErVyGP-c_6wuQcuL7gP1go3bz_ITWhwiUunn4RCxar6IhO9PobQoMyOvN3PV43X2GlvHTtvVLKkBEvD1wU4ENqTdPEXzkwQz7EXT1a6BopiFkIYgQ'

songs = get_playlist_songs(playlist_id,token)
for song in songs:
    track = song['track']
    print(track['name'], 'by', track['artists'][0]['name'])