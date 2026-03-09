import sqlite3
from pet import Pet

class database:
    def __init__(self):
        # Pet table positions
        self._pet_positions = {
            "USERNAME": 1,
            "PASSWORD": 2,
            "PET_NAME": 3,
            "PET_TYPE": 4,
            "HUNGER": 5,
            "HAPPINESS": 6,
            "ENERGY": 7,
            "POINTS": 8,
            "LOG_FILE": 9,
        }
        
        
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
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            pet_name TEXT NOT NULL,
            pet_type TEXT NOT NULL,
            hunger INTEGER NOT NULL,
            happiness INTEGER NOT NULL,
            energy INTEGER NOT NULL,
            points INTEGER NOT NULL,
            log_file TEXT NOT NULL
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
        pet = Pet(
            pet_name = self._pet_positions["PET_NAME"],
            pet_type = self._pet_positions["PET_TYPE"],
            hunger = self._pet_positions["HUNGER"],
            happiness = self._pet_positions["HAPPINESS"],
            energy = self._pet_positions["ENERGY"],
            points = self._pet_positions["POINTS"],
            log_file = self._pet_positions["LOG_FILE"]
        )
        return pet

s = database()
print(s.get_pet("ooo", "ooo"))