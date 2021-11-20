import Logic.SongsServerLogic as sl
import Logic.data_helper as dh
import pytest


@pytest.fixture()
def pretest_actions():
    sl.delete_songs()
    sl.delete_users()


def test_add_new_user(pretest_actions):
    sl.add_user(dh.user1.user_name, dh.user1.user_password)
    resp = sl.get_user(dh.user1.user_name)
    actual_user = dh.get_username(resp)
    assert actual_user == dh.user1.user_name, f'expected: {dh.user1.user_name}, actual: {actual_user}'


def test_add_existing_user(pretest_actions):
    sl.add_user(dh.user1.user_name, dh.user1.user_password)
    resp = sl.add_user(dh.user1.user_name, dh.user1.user_password)
    assert dh.check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


def test_add_friend(pretest_actions):
    sl.add_user(dh.user1.user_name, dh.user1.user_password)
    sl.add_user(dh.user2.user_name, dh.user2.user_password)
    sl.add_friend(dh.user1.user_name, dh.user1.user_password, dh.user2.user_name)
    resp = sl.get_user(dh.user1.user_name)
    assert dh.user2.user_name in dh.get_friend(resp)


#failure
def test_add_friend_non_existing_user(pretest_actions):
    sl.add_user(dh.user1.user_name, dh.user1.user_password)
    sl.add_friend(dh.user1.user_name, dh.user1.user_password, dh.user2.user_name)
    resp = sl.get_user(dh.user1.user_name)
    assert dh.check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


# add test with wrong username
def test_add_friend_with_wrong_password(pretest_actions):
    sl.add_user(dh.user1.user_name, dh.user1.user_password)
    sl.add_user(dh.user2.user_name, dh.user2.user_password)
    resp = sl.add_friend(dh.user1.user_name, dh.user2.user_password, dh.user2.user_name)
    assert dh.check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


def test_add_playlist(pretest_actions):
    sl.add_user(dh.user1.user_name, dh.user1.user_password)
    sl.add_playlist(dh.user1.playlist_name, dh.user1.user_name, dh.user1.user_password)
    assert dh.user1.playlist_name in dh.get_user_playlists(sl.get_user(dh.user1.user_name)),\
        f'{dh.user1.user_name} playlists doesnt contain added playlist name'


# add test with wrong username
def test_add_playlist_with_wrong_password(pretest_actions):
    sl.add_user(dh.user1.user_name, dh.user1.user_password)
    resp = sl.add_playlist(dh.user1.playlist_name, dh.user1.user_name, dh.user2.user_password)
    assert dh.check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


def test_2_different_users_add_same_playlist(pretest_actions):
    sl.add_user(dh.user1.user_name, dh.user1.user_password)
    sl.add_user(dh.user2.user_name, dh.user2.user_password)
    sl.add_playlist(dh.user1.playlist_name, dh.user1.user_name, dh.user1.user_password)
    sl.add_playlist(dh.user1.playlist_name, dh.user2.user_name, dh.user2.user_password)
    assert dh.user1.playlist_name in dh.get_user_playlists(sl.get_user(dh.user1.user_name)),\
        f'{dh.user1.user_name} playlists doesnt contain added playlist name'
    assert dh.user1.playlist_name in dh.get_user_playlists(sl.get_user(dh.user2.user_name)),\
        f'{dh.user2.user_name} playlists doesnt contain added playlist name'


def test_add_existing_playlist(pretest_actions):
    sl.add_user(dh.user1.user_name, dh.user1.user_password)
    sl.add_playlist(dh.user1.playlist_name, dh.user1.user_name, dh.user1.user_password)
    resp = sl.add_playlist(dh.user1.playlist_name, dh.user1.user_name, dh.user1.user_password)
    assert dh.check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'
