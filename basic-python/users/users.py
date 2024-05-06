class User:
    def __init__(self, conn):
        self.conn = conn

    def create_user(self, user):
        sql = """ INSERT INTO users(name,email)
                  VALUES(?,?) """
        cur = self.conn.get_cursor()
        cur.execute(sql, user)
        return cur.lastrowid

    def get_user_by_email(self, email):
        cur = self.conn.get_cursor()
        cur.execute("SELECT * FROM users WHERE email=?", (email,))
        rows = cur.fetchall()
        return rows

    def update_user(self, user):
        sql = """ UPDATE users
                  SET name = ? ,
                      email = ? 
                  WHERE id = ?"""
        cur = self.conn.get_cursor()
        cur.execute(sql, user)
        self.conn.get_connection().commit()

    def delete_user(self, id):
        sql = "DELETE FROM users WHERE id=?"
        cur = self.conn.get_cursor()
        cur.execute(sql, (id,))
        self.conn.get_connection().commit()
