import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import pandas as pd
import settings

# スコープを設定
scope = "user-read-currently-playing playlist-modify-public user-top-read app-remote-control user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope), language='ja')

# 楽曲idから内部オプションを抽出


def hoge(genres, artists, tracks, features):

    # 内部パラメータをバラバラに

    query = {}

    res = sp.recommendations(
        seed_genres=genres, seed_artist=artists, seed_tracks=tracks, limit=20)

    return artists
