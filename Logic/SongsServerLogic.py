from Infra.Requests_API import RequestsApi

session = RequestsApi("http://127.0.0.1:3002", {'Content-Type': 'application/json'})


# /users logic
def add_user(input_data):
    session.post("/users/add_user", input_data)


def get_user(input_data):
    return session.get("/users/get_user", input_data)


def add_playlist(input_data):
    session.post("/users/add_playlist", input_data)


def get_playlist(input_data):
    session.get("/users/get_playlist", input_data)


def add_friend(input_data):
    session.put("/users/add_friend", input_data)


def change_password(input_data):
    session.put("/users/change_password", input_data)


# /songs logic
def add_song(input_data):
    session.post("/songs/add_song", input_data)


def decrease_rating(input_data):
    session.put("/songs/downvote", input_data)


def increase_rating(input_data):
    session.put("/songs/upvote", input_data)


def get_song(input_data):
    session.get("/songs/get_song", input_data)


def get_ranked_songs(input_data):
    session.get("/songs/ranked_songs", input_data)


# /playlist logic
def add_song_to_playlist(input_data):
    session.post("/playlists/add_song", input_data)


# /admin logic
def delete_users():
    session.delete("/admin/delete_all_users")


def delete_songs():
    session.delete("/admin/delete_all_songs")

