import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

my_id = 'cd417d1614f8410097489fe4330f584d'
my_secret = '585d6e31103c49bca21d7acf1a11fc3d'

# アプリケーションの情報を設定します
client_credentials_manager = SpotifyClientCredentials(client_id="my_id",client_secret="my_secret")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# ジャンルとダンス性を指定して曲の推奨を取得します
genres = "electronic"
danceability = 0.8
energy = 0.9
tempo = 130
recommendations = sp.recommendations(seed_genres=['electronic'], 
                                     target_danceability=0.8, 
                                     target_energy=0.9,
                                     target_tempo=130,
                                     limit=20)

# 曲のタイトルとアーティスト名を表示します
for track in recommendations['tracks']:
    print('Title: {}, Artist: {}'.format(track['name'], track['artists'][0]['name']))