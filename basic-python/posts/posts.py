class Post:
    def __init__(self, conn):
        self.conn = conn

    def create_post(self, post):
        sql = """ INSERT INTO posts(title,content,user_id)
                  VALUES(?,?,?) """
        cur = self.conn.get_cursor()
        cur.execute(sql, post)
        return cur.lastrowid
