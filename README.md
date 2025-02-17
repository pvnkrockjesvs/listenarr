# listenarr

A script to add your most played artists from ListenBrainz to your Lidarr.

## Installation

Install listenarr with pip:

```bash
git clone https://gitlab.com/pvnkrockjesvs/listenarr.git
cd listenarr
pip install -r requirements.txt
```

## Environment Variables

To run this project, you need to add a .env file with your Lidarr URL, Lidarr API key, Lidarr music folder, and ListenBrainz username as follows:

```
URL = 'http://localhost:8686'
API = '12abcdefghijkl'
ROOT_FOLDER = '/music'
USERNAME = 'pvnkrockjesvs'
```

## Configuration Options

You can modify the following configuration options in the Python file:

```python
range = 'week'                    # Options: 'this_week', 'this_month', 'this_year', 'week', 'month', 'quarter', 'year', 'half_yearly', 'all_time'
count = 50                        # Number of artists to return
min_listen = 5                    # Minimum number of listens for artists within the range
add_excluded_artists = True       # Set to True to add artists even if they are on the Import List Exclusions
```

## Usage

You can run the script using either the bash script or Python directly:

Using the bash script:
```bash
/path/to/project/listenarr.sh
```

Using Python directly:
```bash
python3 listenarr.py
```

## Acknowledgements

- [ListenBrainz API](https://listenbrainz.readthedocs.io/en/latest/users/api/index.html)
- [Lidarr API](https://lidarr.audio/docs/api/)

## License

[MIT](https://choosealicense.com/licenses/mit/)
