from test_common_functions import *


def test_passwords_encoded(pretest_actions_delete):
    add_user(user1.user_name, user1.user_password)
    db_password = load_json_file()[user1.user_name]['password']
    assert db_password != user1.user_password, f'password in db not encoded: {db_password}'


