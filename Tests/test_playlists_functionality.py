from test_commom_functions import *


def test_add_song_to_playlist(pretest_actions_delete, pretest_actions_insert_songs):
    add_user(user1.user_name, user1.user_password)
    add_playlist(user1.playlist_name, user1.user_name, user1.user_password)
    add_song_to_playlist(user1.playlist_name, songs[0].song_title, user1.user_name, user1.user_password)
    resp = get_playlist(user1.playlist_name, user1.user_name, user1.user_password)
    assert songs[0].song_title in get_playlist_songs(resp), f'playlist doesnt contain requested song'


def test_add_non_existing_song_to_playlist(pretest_actions_delete, pretest_actions_insert_songs):
    add_user(user1.user_name, user1.user_password)
    add_playlist(user1.playlist_name, user1.user_name, user1.user_password)
    resp = add_song_to_playlist(user1.playlist_name, "rock_song", user1.user_name, user1.user_password)
    assert check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


def test_add_song_to_playlist_wrong_password(pretest_actions_delete, pretest_actions_insert_songs):
    add_user(user1.user_name, user1.user_password)
    resp = add_playlist(user1.playlist_name, user1.user_name, user2.user_password)
    assert check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


def test_add_song_which_already_in_playlist(pretest_actions_delete, pretest_actions_insert_songs):
    add_user(user1.user_name, user1.user_password)
    add_song_to_playlist(user1.playlist_name, "rock_song", user1.user_name, user1.user_password)
    resp = add_song_to_playlist(user1.playlist_name, "rock_song", user1.user_name, user1.user_password)
    assert check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'
