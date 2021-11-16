import Logic.SongsServerLogic as sl
import pytest

user1 = {
    "user_name": "test_user1",
    "user_password": "12345"
}

get_user1 = {"user_name": "test_user1"}


def test_add_new_user():
    sl.delete_songs()
    sl.delete_users()
    sl.add_user(user1)
    resp = sl.get_user(get_user1)
    print(resp)
    u = resp['data']['user_name']
    assert u == "test_user1", f'expected: test_user1, actual: {u}'
