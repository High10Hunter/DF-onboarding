from database.connection import (
    DatabaseConnection,
)
from users.users import User
from posts.posts import Post


def main():
    database_file = "test.sqlite"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        email text NOT NULL
                                    ); """

    sql_create_posts_table = """CREATE TABLE IF NOT EXISTS posts (
                                    id integer PRIMARY KEY,
                                    title text NOT NULL,
                                    content text,
                                    user_id integer NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES users (id)
                                );"""

    conn = DatabaseConnection(database_file)

    if conn is not None:
        conn.create_table(sql_create_users_table)
        conn.create_table(sql_create_posts_table)
    else:
        print("Error! cannot create the database connection.")

    userManager = User(conn)
    postManager = Post(conn)

    # insert users
    users = [
        ("User 1", "user1@gmail.com"),
        ("User 2", "user2@gmail.com"),
        ("User 3", "user3@gmail.com"),
    ]

    for user in users:
        print("Creating user with name: ", user[0])
        userManager.create_user(user)

    # get the user by email
    email = "user1@gmail.com"
    user = userManager.get_user_by_email(email)
    user_id = user[0][0]

    posts = [
        ("First post", "First post content", user_id),
        ("Second post", "Second post content", user_id),
    ]

    for post in posts:
        print("Creating post with title: ", post[0])
        postManager.create_post(post)

    updated_user = ("User 1 updatedddd", "user1.updated@gmail.com", user_id)
    print("Updating user with id: ", user_id)
    userManager.update_user(updated_user)

    print("Deleting user with id: ", user_id)
    userManager.delete_user(user_id)

    conn.close_connection()


if __name__ == "__main__":
    main()
