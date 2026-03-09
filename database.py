import sqlite3

class database:
    def __init__(self):
        self._sqlite_connection = sqlite3.connect("pet.db")
        self._cursor = self._sqlite_connection.cursor()
        # self._cursor.execute(
        # """CREATE TABLE logs (
        #     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        #     timestamp TIMESTAMP NOT NULL,
        #     action TEXT NOT NULL,
        #     hunger INTEGER NOT NULL,
        #     happiness INTEGER NOT NULL,
        #     energy INTEGER NOT NULL,
        #     state REAL NOT NULL
        #     );
        # """
        # )
        self._cursor.execute(
        """CREATE TABLE IF NOT EXISTS pets (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            log_file TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            pet_name TEXT NOT NULL,
            type TEXT NOT NULL,
            hunger INTEGER NOT NULL,
            happiness INTEGER NOT NULL,
            energy INTEGER NOT NULL,
            points INTEGER NOT NULL
            );
        """
        )
        print(self._cursor)
    
    def get_pet(self, username: str, password: str):
        self._cursor.execute(
        f"""SELECT * FROM pets
            WHERE username = '{username}'
            AND password = '{password}';
        """
        )
        user_data_list = self._cursor.fetchone()
        return user_data_list

s = database()
print(s.get_pet("ooo", "ooo"))