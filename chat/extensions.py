import os

from youtube import YouTube

client_secrets_file = os.environ["CLIENT_SECRET_FILE"]
youtube_client = YouTube(client_secret_file=client_secrets_file)
youtube_client_object = youtube_client.authenticate()
youtube_client.youtube_client = youtube_client_object
