import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import src.spotipy_test.getFeatureCSV as gf
import settings
import pprint as pprint
import pandas as pd

# スコープを設定,アクセス権限的なヤツ
scope = "user-read-currently-playing playlist-modify-public user-top-read app-remote-control user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope), language='ja')

# 聴いているアーティストの上位を取得
def get_top_artist():
    result = sp.current_user_top_artists(
        limit=50, offset=0, time_range='long_term')
    song_ids = []
    for item in result['items']:
        print(f"artist: {item['name']}, genre:{item['genres']}")
        song_ids.append(item['id'])
    return song_ids

# 聴いている曲の上位を取得
def get_top_song():
    result = sp.current_user_top_tracks(
        limit=50, offset=0, time_range='short_term')
    song_ids = []
    for item in result['items']:
        print(f"name: {item['name']}, artist:{item['artists'][0]['name']}")
        song_ids.append(item['id'])
    return result

# プレイリストから曲を取得
def get_to_playlist(playlist_id):
    playlist = sp.playlist(playlist_id)
    track_ids = []
    for item in playlist['tracks']['items']:
        track = item['track']
        if not track['id'] in track_ids:
            track_ids.append(track['id'])
        else:
            for item in playlist['tracks']['items']:
                track = item['track']
                if not track['id'] in track_ids:
                    track_ids.append(track['id'])
    return track_ids

if __name__ == '__main__':
    res = get_top_song()

    df = pd.DataFrame(res)

    df.to_json('hogehoge.jsonl', orient='records', force_ascii=False, lines=True)
    # pl2 = get_to_playlist("37i9dQZF1EQqedj0y9Uwvu")
    # ab = np.concatenate([pl1,pl2])
    # print(ab)
    # id_to_csv(ab)
