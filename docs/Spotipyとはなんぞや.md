# Spotipyなんぞやあああ

Spotipy

## Spotifyt API（Spotipy）の仕様

### インスコ

```cmd
pip install spotipy
```

### インポト

```python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #ここ以降にいろいろ追加
```

何入ってるのか気になったのでほかに`json`とか`pprint`とか入れてた

### 必須情報

```python
my_id = '発行したCLIANT ID'
my_secret = '発行したCLIANT SECRET'
```

Spotify for Developersから取ってきてね

### 準備

ユーザー情報いらないとき

```python
ccm = SpotifyClientCredentials(client_id = my_id, client_secret = my_secret)
sp = spotipy.Spotify(client_credentials_manager = ccm)
```

ユーザー情報いるとき

```python
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=my_id,
                                               client_secret=my_secret,
                                               redirect_uri="http://localhost:3000/",
                                               scope="user-read-recently-played"))
```

スコープに欲しい情報の要素入れて、リダイレクト先で承認したら通る

## メソッド

関数で定義しています

### キューに楽曲を追加

```python
"""
「次に再生」キューの最後に指定楽曲を追加する
Parameters
----------
uri : string
    曲のURIかID, URL
device_id : string
    SpotifyデバイスのID, Noneの場合はアクティブなデバイス

Scope
-----
app-remote-control, user-modify-playback-state
"""
sp.add_to_queue(uri, device_id=None)
```

### アルバムの情報を取得

```python
"""
指定したアルバムの情報を取得
Parameters
----------
album_id : string (22文字の英数字)
    アルバムのURIかID, URL
market : string (`JP`等)
    市場コード(基本的にNoneでOK)

Return
------
album_info : dict
    アルバムの構成情報
"""
sp.album(album_id, market=None)
```





### 楽曲の情報取得

```python
music_id = "楽曲のID"
result = spotify.audio_features(music_id)
pprint.pprint(result)
```

こんな感じの情報が返ってくる（サカナクション「忘れられないの」の場合）

```python
[{'acousticness': 0.35,
  'analysis_url': 'https://api.spotify.com/v1/audio-analysis/7a3LbQFgp7NCuNcGlTgSsN',
  'danceability': 0.642,
  'duration_ms': 238000,
  'energy': 0.645,
  'id': '7a3LbQFgp7NCuNcGlTgSsN',
  'instrumentalness': 0.00349,
  'key': 6,
  'liveness': 0.191,
  'loudness': -7.358,
  'mode': 0,
  'speechiness': 0.0375,
  'tempo': 172.1,
  'time_signature': 4,
  'track_href': 'https://api.spotify.com/v1/tracks/7a3LbQFgp7NCuNcGlTgSsN',
  'type': 'audio_features',
  'uri': 'spotify:track:7a3LbQFgp7NCuNcGlTgSsN',
  'valence': 0.917}]
```

アコースティックさ、ダンサビリティ、元気さ、インストか、みたいな変なパラメータが取得できる。

| パラメータ         | 説明                                                         |
| ------------------ | ------------------------------------------------------------ |
| `acousticness`     | 曲がアコースティックである確率を0.0から1.0で表したもの。1.0は曲がアコースティックである確率が高いことを示す。 |
| `danceability`     | 曲がダンスに適しているかを0.0から1.0で表したもの。この値はテンポ、リズムの安定性、ビートの強さなどから計算され、1.0は曲がダンスに非常に適していることを示す。 |
| `energy`           | 曲がエネルギッシュである程度を0.0から1.0で表したもの。この値は活動的な音、速いテンポ、騒々しさなどから計算され、1.0は曲が非常にエネルギッシュであることを示す。 |
| `instrumentalness` | 曲がインストゥルメンタルである確率を0.0から1.0で表したもの。1.0は曲がインストゥルメンタル（つまり、ボーカルなし）である確率が高いことを示す。 |
| `liveness`         | 曲がライブで演奏されている確率を0.0から1.0で表したもの。1.0は曲がライブで演奏されている確率が高いことを示す。 |
| `loudness`         | 曲の全体的な音の大きさをデシベルで表したもの。この値は曲全体にわたって平均化され、値は約-60から0dbまでの範囲である。 |
| `speechiness`      | 曲に話し言葉が含まれている確率を0.0から1.0で表したもの。1.0は曲が話し言葉で構成されている確率が高いことを示す。 |
| `valence`          | 曲が陽性の感情（例えば、幸せ、楽観的、陽気）を伝える確率を0.0から1.0で表したもの。1.0は曲が陽性の感情を強く伝えることを示す。 |
| `tempo`            | 曲の全体的な推定テンポをBPM（ビート・パー・ミニット）で表したもの。 |
| `key`              | 曲の全体的なキー（音階）を示す整数。この値はピッチクラス表記法によるもので、0 = C, 1 = C#/Db, 2 = D, と続く。 |
| `mode`             | 曲のモード（主音がメジャーかマイナーか）を示す整数。1はメジャー、0はマイナーを示す。 |
| `time_signature`   | 曲の拍子記号（1小節あたりの拍数）を示す整数。                |

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

```json
{'album': {'album_type': 'album',
           'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/38WbKH6oKAZskBhqDFA8Uj'},     
                        'href': 'https://api.spotify.com/v1/artists/38WbKH6oKAZskBhqDFA8Uj',
                        'id': '38WbKH6oKAZskBhqDFA8Uj',   
                        'name': 'ずっと真夜中でいいのに。',
                        'type': 'artist',
                        'uri': 'spotify:artist:38WbKH6oKAZskBhqDFA8Uj'}],
           'available_markets': ['JP'],
           'external_urls': {'spotify': 'https://open.spotify.com/album/1mtciArMoiLPqOdflY5dWQ'},
           'href': 'https://api.spotify.com/v1/albums/1mtciArMoiLPqOdflY5dWQ',
           'id': '1mtciArMoiLPqOdflY5dWQ',
           'images': [{'height': 640,
                       'url': 'https://i.scdn.co/image/ab67616d0000b273f5c5c21c1bd67ae9fc86064c',
                       'width': 640},
                      {'height': 300,
                       'url': 'https://i.scdn.co/image/ab67616d00001e02f5c5c21c1bd67ae9fc86064c',
                       'width': 300},
                      {'height': 64,
                       'url': 'https://i.scdn.co/image/ab67616d00004851f5c5c21c1bd67ae9fc86064c',
                       'width': 64}],
           'name': '沈香学',
           'release_date': '2023-06-06',
           'release_date_precision': 'day',
           'total_tracks': 13,
           'type': 'album',
           'uri': 'spotify:album:1mtciArMoiLPqOdflY5dWQ'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/38WbKH6oKAZskBhqDFA8Uj'},
              'href': 'https://api.spotify.com/v1/artists/38WbKH6oKAZskBhqDFA8Uj',
              'id': '38WbKH6oKAZskBhqDFA8Uj',
              'name': 'ずっと真夜中でいいのに。',
              'type': 'artist',
              'uri': 'spotify:artist:38WbKH6oKAZskBhqDFA8Uj'}],
 'available_markets': ['AR'],
 'disc_number': 1,
 'duration_ms': 246293,
 'explicit': False,
 'external_ids': {'isrc': 'JPPO02104528'},
 'external_urls': {'spotify': 'https://open.spotify.com/track/5znJrB6cvS8lffgUFnNETf'},
 'href': 'https://api.spotify.com/v1/tracks/5znJrB6cvS8lffgUFnNETf',
 'id': '5znJrB6cvS8lffgUFnNETf',
 'is_local': False,
 'name': '猫リセット',
 'popularity': 51,
 'preview_url': 'https://p.scdn.co/mp3-preview/ac6aeb61e373f70f6cedad38322fc8c24072fd4c?cid=cd417d1614f8410097489fe4330f584d',
 'track_number': 3,
 'type': 'track',
 'uri': 'spotify:track:5znJrB6cvS8lffgUFnNETf'}
```
