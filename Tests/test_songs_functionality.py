from test_commom_functions import *


# delete this one
def test_add_songs(pretest_actions_delete, pretest_actions_insert_songs):
    add_user(user1.user_name, user1.user_password)
    add_playlist(user1.playlist_name, user1.user_name, user1.user_password)
    add_song_to_playlist(user1.playlist_name, songs[0].song_title, user1.user_name, user1.user_password)
    get_playlist(user1.playlist_name, user1.user_name, user1.user_password)
    increase_rating(user1.playlist_name, songs[0].song_title, user1.user_name, user1.user_password)
    increase_rating(user1.playlist_name, songs[0].song_title, user1.user_name, user1.user_password)
    get_song(songs[0].song_title)


def test_user_upvote_song(pretest_actions_delete, pretest_actions_insert_songs):
    add_user(user1.user_name, user1.user_password)
    add_playlist(user1.playlist_name, user1.user_name, user1.user_password)
    add_song_to_playlist(user1.playlist_name, songs[0].song_title, user1.user_name, user1.user_password)
    actual_rating = int(get_song_rating(get_song(songs[0].song_title)))
    assert actual_rating == 0, f'rating of new song not equal to 0: {actual_rating}'
    increase_rating(user1.playlist_name, songs[0].song_title, user1.user_name, user1.user_password)
    actual_rating = int(get_song_rating(get_song(songs[0].song_title)))
    assert actual_rating == 1, f'rating should be 1, actually: {actual_rating}'


def test_users_upvote_song(pretest_actions_delete, pretest_actions_insert_songs):
    add_users_and_vote(100, songs)


# not finished
def test_search_song_by_rating(pretest_actions_delete, pretest_actions_insert_songs):
    prepare_songs_ratings(songs)
