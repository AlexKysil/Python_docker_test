import sqlite3
import random
import string

class test_db:
    connect = None
    cursor = None

    def __init__(self):
        self.connect = sqlite3.connect("is_this_work.db")
        self.cursor = self.connect.cursor()

    def create_db(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tt(id integer, unit_name text, data integer)")

    def set_test_user(self):
        for _ in range (10):
            user_name= ''.join(random.choice(string.ascii_lowercase)for x in range (7))
            self.cursor.execute("INSERT into tt values (?, ?, ?)", [_ + 1, user_name, _+7] )

        self.connect.commit()


    def take_data(self):
        self.cursor.execute("SELECT * FROM tt")
        figna = self.cursor.fetchall()
        for row in figna:
            print(row)

    def clean_up(self):
        self.cursor.execute("DROP TABLE tt")

if __name__=='__main__':
    tdb = test_db()
    tdb.create_db()
    tdb.set_test_user()
    tdb.take_data()
    tdb.clean_up()