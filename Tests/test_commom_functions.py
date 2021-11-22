from Logic.SongsServerLogic import *
from Logic.Data_Helper import *
import random
import pytest


user1 = UserHelper("test_user1", "12345", "test_user2", "playlist1", "56789")
user2 = UserHelper("test_user2", "abcde", "test_user2", "playlist1", "56789")

songs = [SongsHelper("jazz", "best_performer", "jazz_song", "2020"),
         SongsHelper("pop", "best_performer", "pop_song", "2020"),
         SongsHelper("classic", "best_performer", "classic_song", "2020")
         ]


@pytest.fixture()
def pretest_actions_delete():
    delete_songs()
    delete_users()


@pytest.fixture()
def pretest_actions_insert_songs():
    insert_songs_into_db(songs)


def add_user_with_songs(username, password, playlist, playlist_songs):
    add_user(username, password)
    add_playlist(playlist, username, password)
    for song in playlist_songs:
        add_song_to_playlist(playlist, song.song_title, username, password)


def insert_songs_into_db(playlist_songs):
    for song in playlist_songs:
        add_song(song.song_genre, song.song_performer, song.song_title, song.song_year)


def add_users_and_vote(users, playlist_songs):
    user_name = user1.user_name
    rating = 0

    for i in range(0, users):
        user_name = user_name + str(i)
        add_user_with_songs(user_name, user1.user_password, user1.playlist_name, playlist_songs)
        if random.choice([True, False]):
            increase_rating(user1.playlist_name, playlist_songs[0].song_title, user_name, user1.user_password)
            rating = rating + 1
        else:
            decrease_rating(user1.playlist_name, playlist_songs[0].song_title, user_name, user1.user_password)
            rating = rating - 1 if rating > 0 else 0
        assert rating == get_song_rating(get_song(playlist_songs[0].song_title))
        user_name = user_name[0:9]


def prepare_songs_ratings(playlist_songs):
    user_name = user1.user_name

    for i in range(0, 8):
        user_name = user_name + str(i)
        add_user_with_songs(user_name, user1.user_password, user1.playlist_name, playlist_songs)
        increase_rating(user1.playlist_name, playlist_songs[0].song_title, user_name, user1.user_password)
        if i < 6:
            increase_rating(user1.playlist_name, playlist_songs[1].song_title, user_name, user1.user_password)
        if i < 3:
            increase_rating(user1.playlist_name, playlist_songs[2].song_title, user_name, user1.user_password)
        user_name = user_name[0:9]




