import sys
import spotipy
import spotipy.util as util
import settings
import os

# https://developer.spotify.com/documentation/web-api/concepts/scopes
scope = 'user-library-read user-read-playback-state playlist-read-private user-read-recently-played playlist-read-collaborative playlist-modify-public playlist-modify-private'

# https://developer.spotify.com/dashboard
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = 'http://localhost:8889/callback'

# https://developer.spotify.com/documentation/web-api/reference/get-current-users-profile
username = 'sly'

token = util.prompt_for_user_token(username, scope, client_id=client_id ,client_secret=client_secret, redirect_uri=redirect_uri)
print(token)