import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import pandas as pd
import settings

# スコープを設定
scope = "user-read-currently-playing playlist-modify-public user-top-read app-remote-control user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope), language='ja')

# 楽曲idから内部オプションを抽出

# 聴いている曲の上位を取得しファイルに書き込む

def get_top_song():
    """current_user_top_tracks
    Param:
        limit - 返すエンティティの数
        offset - 返す最初のエンティティのインデックス
        time_range - 集計期間(short_term,medium_term,long_term)
    Return:
        dict
    """
    result = sp.current_user_top_tracks(
        limit=1, offset=0, time_range='short_term')

    # 必要なデータを抜き出す
    album_name = result['items']['album']['name']
    album_release_date = result['items']['album']['release_date']
    # 保存用csvファイルの読み込み
    df = pd.read_csv('save.csv')
    for item in result['items']:
        # nameの値が重複しないようにする
        if item['name'] not in df['name'].values:
            print(f"name: {item['name']}, artist:{item['artists'][0]['name']}")
            # csvファイルにresultの内容を書き込む
            df = df.append(item, ignore_index=True)
    df.to_csv('save.csv', index=False)
    return result

# 聴いているアーティストの上位を取得

def get_top_artist():
    """current_user_top_artists
    Param:
        limit - 返すエンティティの数
        offset - 返す最初のエンティティのインデックス
        time_range - 集計期間(short_term,medium_term,long_term)
    Return:
        dict
    """
    result = sp.current_user_top_artists(
        limit=50, offset=0, time_range='short_term')
    song_ids = []
    # 結果を表示
    for item in result['items']:
        print(f"artist: {item['name']}, genre:{item['genres']}")
        song_ids.append(item['id'])
    return song_ids

#アーティスト名を検索
def search_artist():
    artist_name = input("アーティスト名を入力してください: ")
    result = sp.search(q='artist:' + artist_name, type='artist')
    try:
        artist = result['artists']['items'][0]
        print(f"アーティスト名: {artist['name']}")
    except IndexError:
        print("アーティストが見つかりませんでした")
    return artist

#曲名を検索
def search_song():
    title_name = input("曲名を入力してください: ")
    result = sp.search(q='track:' + title_name, type='track', limit=10)
    try:
        tracks = result['tracks']['items']
        for i, track in enumerate(tracks):
            print(f"{i+1}. 曲名: {track['name']}, アーティスト: {track['artists'][0]['name']}")
        track_number = int(input("上記の曲の中から選んでください（番号）: "))
        selected_track = tracks[track_number-1]
        return {'name': selected_track['name'], 'id': selected_track['id']}
    except IndexError:
        print("曲が見つかりませんでした")
        return {'name': None, 'id': None}

#ジャンルを検索
def search_genres():
    genre_name = input("ジャンル名を入力してください: ")
    result = sp.recommendation_genre_seeds()
    try:
        genres = result['genres']
        if genre_name in genres:
            print(f"ジャンル名: {genre_name}")
        else:
            print("ジャンルが見つかりませんでした")
    except IndexError:
        print("エラーが発生しました")
    return genre_name

def hoge(genres, artists, tracks, features):

    # 内部パラメータをバラバラに

    query = {}

    res = sp.recommendations(
        seed_genres=genres, seed_artist=artists, seed_tracks=tracks, limit=20)

    return artists

def menu():
    options = {
        '1': {'function': search_artist, 'name': 'アーティスト名検索'},
        '2': {'function': search_song, 'name': '曲名検索'},
        '3': {'function': search_genres, 'name': 'ジャンル検索'}
    }
    results = []
    while options:
        print("選択肢:")
        for key, value in options.items():
            print(f"{key}: {value['name']}")
        choice = input("選択してください: ")
        if choice in options:
            result = options[choice]['function']()
            results.append(result)
            del options[choice]
            if options:
                print("他の条件で検索しますか？")
                yn = input("1: はい, 2: いいえ")
                if yn == '2':
                    break
        else:
            print("無効な選択です。もう一度選択してください。")
    print("検索結果:")
    for result in results:
        print(result)

if __name__ == '__main__':
    menu()
