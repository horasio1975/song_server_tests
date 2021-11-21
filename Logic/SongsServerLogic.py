from Infra.Requests_API import RequestsApi

session = RequestsApi("http://127.0.0.1:3002", {'Content-Type': 'application/json'})


# /users logic
def add_user(user_name, user_password):
    return session.post("/users/add_user", dict(user_name=user_name, user_password=user_password))


def get_user(user_name):
    return session.get("/users/get_user", dict(user_name=user_name))


def add_playlist(playlist, user_name, user_password):
    return session.post("/users/add_playlist", dict(playlist_name=playlist, user_name=user_name,
                                                    user_password=user_password))


def get_playlist(playlist, user_name, user_password):
    return session.get("/users/get_playlist", dict(playlist_name=playlist, user_name=user_name,
                                                   user_password=user_password))


def add_friend(user_name, user_password, friend_name):
    return session.put("/users/add_friend",
                       dict(user_name=user_name, user_password=user_password, friend_name=friend_name))


def change_password(user_name, user_new_password, user_password):
    return session.put("/users/change_password",
                       dict(user_name=user_name, user_new_password=user_new_password, user_password=user_password))


# /songs logic
def add_song(song_genre, song_performer, song_title, song_year):
    return session.post("/songs/add_song",
                        dict(song_genre=song_genre, song_performer=song_performer,
                             song_title=song_title, song_year=song_year))


def decrease_rating(playlist_name, song_title, user_name, user_password):
    return session.put("/songs/downvote",
                       dict(playlist_name=playlist_name, song_title=song_title,
                            user_name=user_name, user_password=user_password))


def increase_rating(playlist_name, song_title, user_name, user_password):
    return session.put("/songs/upvote",
                       dict(playlist_name=playlist_name, song_title=song_title,
                            user_name=user_name, user_password=user_password))


def get_song(song_title):
    return session.get("/songs/get_song", dict(song_title=song_title))


def get_ranked_songs(rank, op):
    return session.get("/songs/ranked_songs", dict(rank=rank, op=op))


# /playlist logic
def add_song_to_playlist(playlist_name, song_title, user_name, user_password):
    return session.post("/playlists/add_song",
                        dict(playlist_name=playlist_name, song_title=song_title,
                             user_name=user_name, user_password=user_password))


# /admin logic
def delete_users():
    return session.delete("/admin/delete_all_users")


def delete_songs():
    return session.delete("/admin/delete_all_songs")


def admin_add_users(input_data):
    return session.post("/admin/set_users", input_data)


def admin_add_songs(input_data):
    return session.post("/admin/set_songs", input_data)



