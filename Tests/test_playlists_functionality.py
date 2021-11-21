import Logic.SongsServerLogic as sl
import Logic.data_helper as dh
import pytest


@pytest.fixture()
def pretest_actions():
    sl.delete_songs()
    sl.delete_users()
    sl.add_song("jazz", "best_performer", "jazz_song", "2020")
    sl.add_song("pop", "best_performer", "pop_song", "2020")
    sl.add_song("classic", "best_performer", "classic_song", "2020")


def test_add_song_to_playlist(pretest_actions):
    sl.add_user(dh.user1.user_name, dh.user1.user_password)
    sl.add_playlist(dh.user1.playlist_name, dh.user1.user_name, dh.user1.user_password)
    sl.add_song_to_playlist(dh.user1.playlist_name, "pop_song", dh.user1.user_name, dh.user1.user_password)
    sl.add_song_to_playlist(dh.user1.playlist_name, "jazz_song", dh.user1.user_name, dh.user1.user_password)
    resp = sl.get_playlist(dh.user1.playlist_name, dh.user1.user_name, dh.user1.user_password)
    assert "jazz_song" in dh.get_playlist_songs(resp), f'playlist doesnt contain requested song'


def test_add_non_existing_song_to_playlist(pretest_actions):
    sl.add_user(dh.user1.user_name, dh.user1.user_password)
    sl.add_playlist(dh.user1.playlist_name, dh.user1.user_name, dh.user1.user_password)
    resp = sl.add_song_to_playlist(dh.user1.playlist_name, "rock_song", dh.user1.user_name, dh.user1.user_password)
    assert dh.check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


def test_add_song_to_playlist_wrong_password(pretest_actions):
    sl.add_user(dh.user1.user_name, dh.user1.user_password)
    resp = sl.add_playlist(dh.user1.playlist_name, dh.user1.user_name, dh.user2.user_password)
    assert dh.check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


def test_add_song_which_already_in_playlist(pretest_actions):
    sl.add_user(dh.user1.user_name, dh.user1.user_password)
    sl.add_song_to_playlist(dh.user1.playlist_name, "rock_song", dh.user1.user_name, dh.user1.user_password)
    resp = sl.add_song_to_playlist(dh.user1.playlist_name, "rock_song", dh.user1.user_name, dh.user1.user_password)
    assert dh.check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'
