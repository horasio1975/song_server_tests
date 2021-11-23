from test_common_functions import *


def test_user_upvote_song(pretest_actions_delete, pretest_actions_insert_songs):
    add_user_with_songs(user1.user_name, user1.user_password, user1.playlist_name, songs)
    actual_rating = int(get_song_rating_response(get_song(songs[0].song_title)))
    assert actual_rating == 0, f'rating of new song not equal to 0: {actual_rating}'
    increase_rating(user1.playlist_name, songs[0].song_title, user1.user_name, user1.user_password)
    actual_rating = int(get_song_rating_response(get_song(songs[0].song_title)))
    assert actual_rating == 1, f'rating should be 1, actually: {actual_rating}'


@pytest.mark.xfail
def test_user_votes_for_any_song_twice(pretest_actions_delete, pretest_actions_insert_songs):
    add_user_with_songs(user1.user_name, user1.user_password, user1.playlist_name, songs)
    increase_rating(user1.playlist_name, songs[0].song_title, user1.user_name, user1.user_password)
    resp = increase_rating(user1.playlist_name, songs[0].song_title, user1.user_name, user1.user_password)
    assert check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'
    actual_rating = int(get_song_rating_response(get_song(songs[0].song_title)))
    assert actual_rating == 1, f'rating should be 1, actually: {actual_rating}'


def test_rating_cant_be_lower_than_0(pretest_actions_delete, pretest_actions_insert_songs):
    add_user_with_songs(user1.user_name, user1.user_password, user1.playlist_name, songs)
    decrease_rating(user1.playlist_name, songs[0].song_title, user1.user_name, user1.user_password)
    actual_rating = int(get_song_rating_response(get_song(songs[0].song_title)))
    assert actual_rating == 0, f'rating cant be lower than 0: {actual_rating}'


def test_user_votes_with_wrong_password(pretest_actions_delete, pretest_actions_insert_songs):
    add_user_with_songs(user1.user_name, user1.user_password, user1.playlist_name, songs)
    resp = increase_rating(user1.playlist_name, songs[0].song_title, user1.user_name, user1.user_new_password)
    assert check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


def test_users_upvote_song(pretest_actions_delete, pretest_actions_insert_songs):
    add_users_and_vote(100, songs)


@pytest.mark.parametrize(("rank", "op", "res"), [
    ("2", "greater", [songs[0].song_title, songs[1].song_title, songs[2].song_title, songs[3].song_title]),
    ("5", "greater", [songs[0].song_title, songs[1].song_title]),
    ("7", "greater", [songs[0].song_title]), ("10", "greater", []),
    ("6", "eq", [songs[1].song_title]),
    ("3", "eq", [songs[2].song_title, songs[3].song_title]),
    ("10", "less", [songs[0].song_title, songs[1].song_title, songs[2].song_title, songs[3].song_title]),
    ("7", "less", [songs[1].song_title, songs[2].song_title, songs[3].song_title]),
    ("4", "less", [songs[2].song_title, songs[3].song_title]), ("2", "less", [])
])
def test_search_song_by_rating(pretest_actions_delete, pretest_actions_insert_songs, rank, op, res):
    prepare_songs_ratings(songs)
    resp = get_ranked_songs_response(get_ranked_songs(rank, op))
    assert resp == res, f'expected: {res}, received from server {resp}'


def test_search_song_with_wrong_op(pretest_actions_delete, pretest_actions_insert_songs):
    resp = get_ranked_songs("0", "rank")
    assert check_response_contains(resp, "error"), f'Server response doesnt contains Error Message'


