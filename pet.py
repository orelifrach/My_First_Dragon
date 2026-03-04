from os import path
from range_error import RangeError
import logging


class Pet:
    # Initial state
    HUNGER = 50
    HAPPINESS = 70
    ENERGY = 70
    POINTS = 10

    # Default changes
    HUNGER_AFTER_EAT = -15
    HAPPINESS_AFTER_EAT = 5
    ENERGY_AFTER_EAT = 10
    POINTS_AFTER_EAT = -3

    HUNGER_AFTER_SLEEP = 15
    ENERGY_AFTER_SLEEP = 20

    HUNGER_AFTER_PLAY = 10
    HAPPINESS_AFTER_PLAY = 15
    ENERGY_AFTER_PLAY = -10
    POINTS_AFTER_PLAY = 2

    # State Calculation
    HUNGER_PERCENT = 0.4
    HAPPINESS_PERCENT = 0.6
    ENERGY_PERCENT = 0.4

    # Actions list
    _actions_list = ["eat", "sleep", "play", "state", "status"]
    # Pet type list
    _pet_type_list = ["dog", "cat", "fish"]

    @classmethod
    def get_actions_list(Pet):
        return Pet._actions_list

    @classmethod
    def get_pet_type_list(Pet):
        return Pet._pet_type_list

    @classmethod
    def verify_type(Pet, type: str):
        return type in Pet._pet_type_list

    @classmethod
    def verify_name(Pet, name: str):
        return 2 <= len(name) <= 9 and name.isalpha()

    def __init__(self, name: str, type: str):
        self._name = name
        self._type = type
        self._hunger = Pet.HUNGER
        self._happiness = Pet.HAPPINESS
        self._energy = Pet.ENERGY
        self._points = Pet.POINTS
        abs_path = path.abspath(path.dirname("pet.py"))
        self._log_path = path.join(abs_path, "history_log")

    def eat(self):
        try:
            self._check_field("points", Pet.POINTS_AFTER_EAT)
            self._check_field("hunger", Pet.HUNGER_AFTER_EAT)
            self._check_field("energy", Pet.ENERGY_AFTER_EAT)

            self._change_field("points", Pet.POINTS_AFTER_EAT)
            self._change_field("hunger", Pet.HUNGER_AFTER_EAT)
            self._change_field("energy", Pet.ENERGY_AFTER_EAT)
            self._change_field("happiness", Pet.HAPPINESS_AFTER_EAT)

            msg = f"{self._name} has eaten"
            msg_status = "success"

        except RangeError as err:
            msg = f"Action eat was not made | {err}"
            msg_status = "error"

        self._write_history(msg_status, msg)
        return msg

    def sleep(self):
        try:
            self._check_field("hunger", Pet.HUNGER_AFTER_SLEEP)
            self._check_field("energy", Pet.ENERGY_AFTER_SLEEP)

            self._change_field("hunger", Pet.HUNGER_AFTER_SLEEP)
            self._change_field("energy", Pet.ENERGY_AFTER_SLEEP)

            msg = f"{self._name} has slept"
            msg_status = "success"

        except RangeError as err:
            msg = f"Action sleep was not made | {err}"
            msg_status = "error"

        self._write_history(msg_status, msg)
        return msg

    def play(self):
        try:
            self._check_field("points", Pet.POINTS_AFTER_PLAY)
            self._check_field("hungry", Pet.HUNGER_AFTER_PLAY)
            self._check_field("energy", Pet.ENERGY_AFTER_PLAY)

            self._change_field("points", Pet.POINTS_AFTER_PLAY)
            self._change_field("hungry", Pet.HUNGER_AFTER_PLAY)
            self._change_field("energy", Pet.ENERGY_AFTER_PLAY)
            self._change_field("happiness", Pet.HAPPINESS_AFTER_PLAY)

            msg = f"{self._name} has palyed"
            msg_status = "success"

        except RangeError as err:
            msg = f"Action play was not made | {err}"
            msg_status = "error"

        self._write_history(msg_status, msg)
        return msg

    def _check_field(self, field: str, change: int):
        if field == "hunger":
            if self._hunger + change > 100:
                raise RangeError("Your pet is too hungry to make this action")
            elif self._hunger + change < 0:
                raise RangeError("Your pet is too full to make this action")
        elif field == "energy":
            if self._energy + change < 0:
                raise RangeError(
                    "Your pet doesnt have enough energy to make this action"
                )
        elif field == "points":
            if self._points + change < 0:
                raise RangeError(
                    "You dont have enough points to make this action"
                )

    def _change_field(self, field: str, change: int):
        if field == "hunger":
            self._hunger += change
        elif field == "happiness":
            if self._happiness + change > 100:
                self._happiness = 100
            elif self._happiness + change < 0:
                self._happiness = 0
            else:
                self._happiness += change
        elif field == "energy":
            if self._energy + change > 100:
                self._energy = 100
            else:
                self._energy += change
        elif field == "points":
            self._points += change

    def get_data(self, data):
        if data == " hunger":
            return self._hunger
        if data == "happiness":
            return self._happiness
        if data == "energy":
            return self._energy
        if data == "points":
            return self._points
        if data == "state":
            return self.get_total_state()
    
    def get_hunger(self):
        return f"The hunger level of {self._name} is {self._hunger}"
    
    def get_happiness(self):
        return f"The happiness level of {self._name} is {self._happiness}"
    
    def get_energy(self):
        return f"The energy level of {self._name} is {self._happiness}"
    
    def get_points(self):
        return f"You have {self._points} points"
    
    def get_total_state(self) -> None:
        state = (
            self._happiness * Pet.HAPPINESS_PERCENT
            + self._energy * Pet.ENERGY_PERCENT
            - self._hunger * Pet.HUNGER_PERCENT
        )
        state_str = f"The total state of {self._name} the {self._type} is {state}"
        return state_str
    
    def get_status(self):
        description = f"""------------------------------
name: {self._name}
type: {self._type}

hunger level: {self._hunger}
happiness level: {self._happiness}
energy level: {self._energy}
total state: {self.get_total_state()}

points: {self._points}
------------------------------"""
        return description
    
    def _write_history(self, msg_status, msg):
        logging.basicConfig(
            filename=self._log_path,
            format="%(asctime)s  %(levelname)s | %(message)s",
            datefmt="%m/%d/%Y %I:%M %p",
            level=logging.DEBUG,
        )
        if msg_status == "success":
            logging.info(msg)
        elif msg_status == "error":
            logging.error(msg)


# p = Pet("puppy", "dog")
# p.eat()
# p.eat()
# p.eat()
# p.eat()
# p.eat()
# p.eat()
# p.sleep()
# p.play()
# p.play()
# p.play()
# p.play()
# p.play()
# p.play()
# p.play()
# p.play()
# p.play()
# p.play()
# p.play()
# print("5".isdigit())
