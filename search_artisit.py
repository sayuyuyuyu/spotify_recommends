from langchain.tools.base import BaseTool
import spotipy
import json
import os
import settings

class SearchArtistTool(BaseTool):
    """Tool that fetches audio features of saved tracks from Spotify."""

    name = "SearchArtistTool"
    description = (
        "Tool to search by artist name from Spotify"
        "This tool requires one or more arguments. The arguments are artist name text of type String."
    )

    def _run(self, *args, **kwargs) -> str:
        token = os.getenv('SPOTIFY_TOKEN')
        if not token:
            raise ValueError("SPOTIFY_TOKEN environment variable is not set.")
        sp = spotipy.Spotify(auth=token)
        artist_name = args
        # result = sp.current_user_saved_tracks(limit=50)
        result = sp.search(q='artist:' + str(artist_name), type='artist', limit=1)
        
        print(result)

        # 仮定: result['tracks']['items'] はトラックのリスト
        tracks = [item['id'] for item in result['artists']['items']]
        # 各トラックのオーディオ特性を取得
        audio_features_list = [sp.audio_features(track)[0] for track in tracks]

        # uriとtrack_hrefを削除
        for features in audio_features_list:
            if 'uri' in features:
                del features['uri']
            if 'track_href' in features:
                del features['track_href']
            if 'analysis_url' in features:
                del features['analysis_url']

        # JSON形式に変換
        audio_features_json = json.dumps(audio_features_list)
        return audio_features_json
    
    

    async def _arun(self, *args, **kwargs) -> str:
        """Use the SpotifyTool asynchronously."""
        return self._run()