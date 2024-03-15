from langchain.tools.base import BaseTool
import spotipy
import json
import os
import settings

class SearchRecommendTool(BaseTool):
    """A tool that recommends songs from Spotify."""

    name = "SearchRecommendTool"
    description = (
        "Tool to recommend songs from Spotify"
        "This tool can only be used after using SpotifyTool and SearchArtistTool"
        "This tool requires two or more arguments. The arguments are as follows:"
        "1. an artist ID of type String"
        "2. the song ID as a String"
        "3. a genre list of type String"
    )

    def _run(self, track_ids, artist_id) -> str:
        token = os.getenv('SPOTIFY_TOKEN')
        if not token:
            raise ValueError("SPOTIFY_TOKEN environment variable is not set.")
        sp = spotipy.Spotify(auth=token)
        artist_id = artist_id
        tracks_id = track_ids
        # ジャンルとダンス性を指定して曲の推奨を取得します
        genres = "electronic"
        danceability = 0.8
        energy = 0.9
        tempo = 130
        recommendations = sp.recommendations(seed_artists=artist_id,
                                            seed_genres=['electronic'],
                                            seed_tracks=tracks_id, 
                                            target_danceability=0.8, 
                                            target_energy=0.9,
                                            target_tempo=130,
                                            limit=20)

        # 曲のタイトルとアーティスト名を表示します
        for track in recommendations['tracks']:
            print('Title: {}, Artist: {}'.format(track['name'], track['artists'][0]['name']))

        # JSON形式に変換
        audio_features_json = json.dumps(recommendations)
        return audio_features_json

    async def _arun(self, track_ids, artist_id) -> str:
        """Use the SpotifyTool asynchronously."""
        return self._run(track_ids, artist_id)