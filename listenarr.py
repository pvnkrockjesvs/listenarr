import requests
import os
from dotenv import load_dotenv
load_dotenv()


def get_excluded_artists(lidarr_url, api_key):
    headers = {
        'X-Api-Key': api_key,
    }
    response = requests.get(f'{lidarr_url}/api/v1/importlistexclusion', headers=headers)
    if response.status_code == 200:
        return [exclusion['foreignId'] for exclusion in response.json()]
    else:
        print(f"Failed to fetch exclusion list. Status code: {response.status_code}")
        return []

def add_artist_to_lidarr(lidarr_url, api_key, mbid, artist_name, root_folder, excluded_artists):
    if mbid in excluded_artists:
        print(f"Skipping excluded artist: {artist_name} (MBID: {mbid})")
        return

    headers = {
        'X-Api-Key': api_key,
        'Content-Type': 'application/json'
    }

    payload = {
        'foreignArtistId': mbid,
        'artistName': artist_name,
        'rootFolderPath': root_folder,
        'monitored': True,
        'qualityProfileId': 1,
        'metadataProfileId': 1,
        "addOptions": {
            "searchForMissingAlbums": False     # set as True if you want to search for the missing albums on add
        },
    }


    response = requests.post(f'{lidarr_url}/api/v1/artist', headers=headers, json=payload)

    if response.status_code == 201:
        print(f"Successfully added artist: {artist_name} (MBID: {mbid})")

def get_top_artists(username, range, count, min_listen):
    url = f"https://api.listenbrainz.org/1/stats/user/{username}/artists"
    params = {
        'range': range,
        'count': count
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    artists = data['payload']['artists']

    return [artist for artist in artists if artist['listen_count'] > min_listen]

# Configuration
lidarr_url = os.getenv("URL")
api_key = os.getenv("API")
root_folder = os.getenv("ROOT_FOLDER")
username = os.getenv("USERNAME")
range = 'week'                          # 'this_week', 'this_month', 'this_year', 'week', 'month', 'quarter', 'year', 'half_yearly', 'all_time'
count = 50                              # number of artists to return
min_listen = 5                          # set the minimum listen for artists within the range
add_excluded_artists = False             # set to True if you want to add artists even if they are on the Import List Exclusions


excluded_artists = get_excluded_artists(lidarr_url, api_key) if not add_excluded_artists else []

artists = get_top_artists(username, range, count, min_listen)

for artist in artists:
    add_artist_to_lidarr(lidarr_url, api_key, artist['artist_mbid'], artist['artist_name'], root_folder, excluded_artists)

