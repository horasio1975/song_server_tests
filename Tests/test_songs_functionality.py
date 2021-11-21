import Logic.SongsServerLogic as sl
import Logic.data_helper as dh
import pytest
import random


@pytest.fixture()
def pretest_actions():
    sl.delete_songs()
    sl.delete_users()
    sl.add_song("jazz", "best_performer", "jazz_song", "2020")
    sl.add_song("pop", "best_performer", "pop_song", "2020")
    sl.add_song("classic", "best_performer", "classic_song", "2020")


def add_users_and_vote(users):
    user_name = "user_"
    playlist = "my_playlist"
    password = "abc"
    rating = 0

    for i in range(0, users):
        user_name = user_name+str(i)
        sl.add_user(user_name, password)
        sl.add_playlist(playlist, user_name, password)
        sl.add_song_to_playlist(playlist, "jazz_song", user_name, password)
        if random.choice([True, False]):
            sl.increase_rating(playlist, "jazz_song", user_name, password)
            rating = rating + 1
        else:
            sl.decrease_rating(playlist, "jazz_song", user_name, password)
            rating = rating - 1 if rating > 0 else 0
        assert rating == dh.get_song_rating(sl.get_song("jazz_song"))
        user_name = user_name[0:5]


# delete this one
def test_add_songs(pretest_actions):
    sl.add_user(dh.user1.user_name, dh.user1.user_password)
    sl.add_playlist(dh.user1.playlist_name, dh.user1.user_name, dh.user1.user_password)
    sl.add_song_to_playlist(dh.user1.playlist_name, "jazz_song", dh.user1.user_name, dh.user1.user_password)
    sl.get_playlist(dh.user1.playlist_name, dh.user1.user_name, dh.user1.user_password)
    sl.increase_rating(dh.user1.playlist_name, "jazz_song", dh.user1.user_name, dh.user1.user_password)
    sl.increase_rating(dh.user1.playlist_name, "jazz_song", dh.user1.user_name, dh.user1.user_password)
    sl.get_song("jazz_song")


def test_user_upvote_song(pretest_actions):
    sl.add_user(dh.user1.user_name, dh.user1.user_password)
    sl.add_playlist(dh.user1.playlist_name, dh.user1.user_name, dh.user1.user_password)
    sl.add_song_to_playlist(dh.user1.playlist_name, "jazz_song", dh.user1.user_name, dh.user1.user_password)
    actual_rating = int(dh.get_song_rating(sl.get_song("jazz_song")))
    assert actual_rating == 0, f'rating of new song not equal to 0: {actual_rating}'
    sl.increase_rating(dh.user1.playlist_name, "jazz_song", dh.user1.user_name, dh.user1.user_password)
    actual_rating = int(dh.get_song_rating(sl.get_song("jazz_song")))
    assert actual_rating == 1, f'rating should be 1, actually: {actual_rating}'


def test_users_upvote_song(pretest_actions):
    add_users_and_vote(100)


