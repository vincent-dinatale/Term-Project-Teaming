from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

app = Flask(__name__)

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = base64.b64encode(auth_string.encode("utf-8"))
    auth_base64 = auth_bytes.decode("utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_playlist(token, playlist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"q={playlist_name}&type=playlist&limit=1"

    query_url = url + '?' + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["playlists"]["items"]
    if len(json_result) == 0:
        return None

    return json_result[0]

def get_tracks_from_playlist(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["items"]
    return json_result

def get_playlist_details(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    return json.loads(result.content)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        playlist_name = request.form['playlist_name']
        token = get_token()
        playlist = search_for_playlist(token, playlist_name)

        if playlist:
            playlist_id = playlist["id"]
            playlist_details = get_playlist_details(token, playlist_id)
            playlist_link = playlist_details["external_urls"]["spotify"]
            playlist_name = playlist_details["name"]
            playlist_art = playlist_details["images"][0]["url"] if playlist_details["images"] else None
            tracks = get_tracks_from_playlist(token, playlist_id)

            return render_template('index.html', playlist_name=playlist_name, playlist_link=playlist_link, playlist_art=playlist_art, tracks=tracks)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



