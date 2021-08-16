import sqlite3

# module-wide variable to make sure the DB class constructor
# doesn't get called outside de get_instance method
__SECRET__ = object()

class DB:
    _instance = None

    def __init__(self):
        if (__SECRET__ is None):
            raise RuntimeError("The DB class is a singleton and cannot be instantiated directly. Use the DB.get_instance method instead.")
        else:
            self.con = sqlite3.connect("replies.db")

        try:
            with self.con:
                self.con.execute("""CREATE TABLE IF NOT EXISTS comments (
                                        comment_id text primary key not null,
                                        created_utc integer not null,
                                        replied_utc integer not null
                                    )""")
                self.con.execute("""CREATE TABLE IF NOT EXISTS errors (
                                        comment_id text primary key not null,
                                        message text not null,
                                        error_utc integer not null
                                    )""")
        except sqlite3.DatabaseError:
            print("Could not create sqlite database")

    @staticmethod
    def get_instance(self):
        if self._instance == None:
            self._instance = self.__init__()
        return self._instance
