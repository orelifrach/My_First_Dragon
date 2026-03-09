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
            "LOG_FILE": 9
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
            pet_name = user_data_list[self._pet_positions["PET_NAME"]],
            pet_type = user_data_list[self._pet_positions["PET_TYPE"]],
            hunger = user_data_list[self._pet_positions["HUNGER"]],
            happiness = user_data_list[self._pet_positions["HAPPINESS"]],
            energy = user_data_list[self._pet_positions["ENERGY"]],
            points = user_data_list[self._pet_positions["POINTS"]],
            log_file = user_data_list[self._pet_positions["LOG_FILE"]]
        )
        return pet
    
    def insert_pet(self, pet: Pet):
        # pet_name = pet.get_pet_name()
        # pet_type = pet.get_pet_type()
        # hunger = pet.get_hunger()
        # happiness = pet.get_happiness()
        # energy = pet.get_energy()
        # points = pet.get_points()
        # log_file = pet.get_log_file()
        
        params = (
            {2},
            'or-el',
            'pass',
            {pet.get_pet_name()},
            {pet.get_pet_type()},
            {int(pet.get_hunger(True))},
            {int(pet.get_happiness(True))},
            {int(pet.get_energy(True))},
            {int(pet.get_points(True))},
            {pet.get_log_file()}
        )
        self._cursor.execute(
            "INSERT INTO pets VALUES (?,?,?,?,?,?,?,?,?,?)", params)

s = database()
print(s.get_pet("ooo", "ooo"))
p = Pet("puppy", "dog", log_file="pet2")
print(p.get_log_file())
s.insert_pet(p)