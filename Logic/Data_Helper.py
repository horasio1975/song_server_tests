

class UserHelper:
    def __init__(self, user_name, user_password, friend_name,
                 playlist_name, user_new_password):
        self.user_name = user_name
        self.user_password = user_password
        self.friend_name = friend_name
        self.playlist_name = playlist_name
        self.user_new_password = user_new_password


class SongsHelper:
    def __init__(self, song_genre, song_performer, song_title, song_year):
        self.song_genre = song_genre
        self.song_performer = song_performer
        self.song_title = song_title
        self.song_year = song_year


def get_username(my_data):
    return my_data['data']['user_name']


def get_friend(my_data):
    return my_data['data']['friends'][0]


def get_user_playlists(my_data):
    return my_data['data']['playlists']


def get_playlist_songs(my_data):
    playlist_songs = []
    for song in my_data['data']:
        playlist_songs.append(song['title'])

    return playlist_songs


def get_song_rating(my_data):
    return my_data['data']['rating']


def check_response_contains(my_data, substring):
    if substring in my_data:
        return True
    return False

