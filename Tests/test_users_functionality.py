from test_commom_functions import *


#user1 = UserHelper("test_user1", "12345", "test_user2", "playlist1", "56789")
#user2 = UserHelper("test_user2", "abcde", "test_user2", "playlist1", "56789")


#@pytest.fixture()
#def pretest_actions_delete():
 #   delete_songs()
 #   delete_users()


def test_add_new_user(pretest_actions_delete):
    add_user(user1.user_name, user1.user_password)
    resp = get_user(user1.user_name)
    actual_user = get_username(resp)
    assert actual_user == user1.user_name, f'expected: {user1.user_name}, actual: {actual_user}'


def test_add_existing_user(pretest_actions_delete):
    add_user(user1.user_name, user1.user_password)
    resp = add_user(user1.user_name, user1.user_password)
    assert check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


def test_add_friend(pretest_actions_delete):
    add_user(user1.user_name, user1.user_password)
    add_user(user2.user_name, user2.user_password)
    add_friend(user1.user_name, user1.user_password, user2.user_name)
    resp = get_user(user1.user_name)
    assert user2.user_name in get_friend(resp)


@pytest.mark.xfail
def test_add_friend_non_existing_user(pretest_actions_delete):
    add_user(user1.user_name, user1.user_password)
    add_friend(user1.user_name, user1.user_password, user2.user_name)
    resp = get_user(user1.user_name)
    assert check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


# add test with wrong username
def test_add_friend_with_wrong_password(pretest_actions_delete):
    add_user(user1.user_name, user1.user_password)
    add_user(user2.user_name, user2.user_password)
    resp = add_friend(user1.user_name, user2.user_password, user2.user_name)
    assert check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


def test_add_playlist(pretest_actions_delete):
    add_user(user1.user_name, user1.user_password)
    add_playlist(user1.playlist_name, user1.user_name, user1.user_password)
    assert user1.playlist_name in get_user_playlists(get_user(user1.user_name)),\
        f'{user1.user_name} playlists doesnt contain added playlist name'


# add test with wrong username
def test_add_playlist_with_wrong_password(pretest_actions_delete):
    add_user(user1.user_name, user1.user_password)
    resp = add_playlist(user1.playlist_name, user1.user_name, user2.user_password)
    assert check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


def test_2_different_users_add_same_playlist(pretest_actions_delete):
    add_user(user1.user_name, user1.user_password)
    add_user(user2.user_name, user2.user_password)
    add_playlist(user1.playlist_name, user1.user_name, user1.user_password)
    add_playlist(user1.playlist_name, user2.user_name, user2.user_password)
    assert user1.playlist_name in get_user_playlists(get_user(user1.user_name)),\
        f'{user1.user_name} playlists doesnt contain added playlist name'
    assert user1.playlist_name in get_user_playlists(get_user(user2.user_name)),\
        f'{user2.user_name} playlists doesnt contain added playlist name'


def test_add_existing_playlist(pretest_actions_delete):
    add_user(user1.user_name, user1.user_password)
    add_playlist(user1.playlist_name, user1.user_name, user1.user_password)
    resp = add_playlist(user1.playlist_name, user1.user_name, user1.user_password)
    assert check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


@pytest.mark.skip("not ready")
def test_user_updates_password(pretest_actions_delete):
    add_user(user1.user_name, user1.user_password)

