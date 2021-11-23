from test_common_functions import *


def test_add_song_to_playlist(pretest_actions_delete, pretest_actions_insert_songs):
    add_user(user1.user_name, user1.user_password)
    add_playlist(user1.playlist_name, user1.user_name, user1.user_password)
    add_song_to_playlist(user1.playlist_name, songs[0].song_title, user1.user_name, user1.user_password)
    resp = get_playlist(user1.playlist_name, user1.user_name, user1.user_password)
    assert songs[0].song_title in get_playlist_songs_response(resp), f'playlist doesnt contain requested song'


def test_add_non_existing_song_to_playlist(pretest_actions_delete, pretest_actions_insert_songs):
    add_user(user1.user_name, user1.user_password)
    add_playlist(user1.playlist_name, user1.user_name, user1.user_password)
    resp = add_song_to_playlist(user1.playlist_name, "rock_song", user1.user_name, user1.user_password)
    assert check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


@pytest.mark.parametrize(("user_name", "user_password"), INVALID_USER_DATA)
def test_add_song_to_playlist_wrong_data(pretest_actions_delete, pretest_actions_insert_songs,
                                         user_name, user_password):
    add_user(user1.user_name, user1.user_password)
    resp = add_playlist(user1.playlist_name, user_name, user_password)
    assert check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


def test_add_song_to_playlist_wrong_playlist_name(pretest_actions_delete, pretest_actions_insert_songs):
    add_user_with_songs(user1.user_name, user1.user_password, user1.playlist_name, songs)
    resp = add_song_to_playlist("aaaaa", songs[1].song_title, user1.user_name, user1.user_password)
    assert check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


def test_add_song_which_already_in_playlist(pretest_actions_delete, pretest_actions_insert_songs):
    add_user_with_songs(user1.user_name, user1.user_password, user1.playlist_name, songs)
    resp = add_song_to_playlist(user1.playlist_name, songs[1].song_title, user1.user_name, user1.user_password)
    assert check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


@pytest.mark.skip("no functionality to delete song from playlist found")
def test_delete_song_from_playlist(pretest_actions_delete, pretest_actions_insert_songs):
    add_user_with_songs(user1.user_name, user1.user_password, user1.playlist_name, songs)


@pytest.mark.skip("no functionality to delete song from playlist found")
def test_delete_song_from_playlist_wrong_password(pretest_actions_delete, pretest_actions_insert_songs):
    add_user_with_songs(user1.user_name, user1.user_password, user1.playlist_name, songs)

