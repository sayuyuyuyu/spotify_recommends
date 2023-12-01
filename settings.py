import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

OPENAI= os.environ.get("OPENAI_API_KEY") 
SP_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID") 
SP_CLIENT_SECREST = os.environ.get("SPOTIPY_CLIENT_SECRET") 
SP_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI") 