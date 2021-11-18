import Logic.SongsServerLogic as sl
import Logic.response_parser as rp
import pytest

user1 = {
    "user_name": "test_user1",
    "user_password": "12345"
}

user2 = {
    "user_name": "test_user2",
    "user_password": "12345"
}

get_user1 = {"user_name": "test_user1"}

add_friend = {
    "user_name": "test_user1",
    "user_password": "12345",
    "friend_name": "test_user2"
}


@pytest.fixture()
def pretest_actions():
    sl.delete_songs()
    sl.delete_users()


def test_add_new_user(pretest_actions):
    sl.add_user(user1)
    resp = sl.get_user(get_user1)
    print(resp)
    actual_user = rp.get_username(resp)
    assert actual_user == "test_user1", f'expected: test_user1, actual: {actual_user}'


def test_add_existing_user(pretest_actions):
    sl.add_user(user1)
    resp = sl.add_user(user1)
    print(resp)


def test_add_friend(pretest_actions):
    sl.add_user(user1)
    sl.add_user(user2)
    sl.add_friend(add_friend)
    resp = sl.get_user(user1)
    print(rp.get_friend(resp))

