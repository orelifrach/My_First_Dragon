from os import path
from range_error import RangeError
import logging


class Pet:
    pet_number = 1
    
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
    HAPPINESS_AFTER_SLEEP = -10
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
    def verify_pet_type(Pet, type: str):
        return type in Pet._pet_type_list

    @classmethod
    def verify_pet_name(Pet, name: str):
        return 2 <= len(name) <= 9 and name.isalpha()

    def __init__(
        self,
        pet_name: str,
        pet_type: str,
        hunger: int = HUNGER,
        happiness: int = HAPPINESS,
        energy: int = ENERGY,
        points: int = POINTS,
        log_file: str = None
    ):
        self._pet_name = pet_name
        self._pet_type = pet_type
        self._hunger = hunger
        self._happiness = happiness
        self._energy = energy
        self._points = points
        
        abs_path = path.abspath(path.dirname("pet.py"))
        if log_file is None:
            self._log_file = f"pet{Pet.pet_number}"
            Pet.pet_number += 1
        else:
            self._log_file = log_file
        self._log_path = path.join(abs_path, "history_logs", f"{self._log_file}")


        logging.basicConfig(
            filename=self._log_path,
            format="%(asctime)s  %(levelname)s | %(message)s",
            datefmt="%d/%m/%Y %I:%M %p",
            level=logging.DEBUG,
        )

    def eat(self):
        try:
            self._check_field("points", Pet.POINTS_AFTER_EAT)
            self._check_field("hunger", Pet.HUNGER_AFTER_EAT)
            self._check_field("energy", Pet.ENERGY_AFTER_EAT)

            self._change_field("points", Pet.POINTS_AFTER_EAT)
            self._change_field("hunger", Pet.HUNGER_AFTER_EAT)
            self._change_field("energy", Pet.ENERGY_AFTER_EAT)
            self._change_field("happiness", Pet.HAPPINESS_AFTER_EAT)

            msg = f"{self._pet_name} has eaten"
            msg_status = "success"

        except RangeError as err:
            msg = f"Action eat was not made | {err}"
            msg_status = "error"

        self._write_history(msg_status, msg)
        return msg

    def sleep(self):
        try:
            self._check_field("hunger", Pet.HUNGER_AFTER_SLEEP)
            self._check_field("happiness", Pet.HAPPINESS_AFTER_SLEEP)
            self._check_field("energy", Pet.ENERGY_AFTER_SLEEP)

            self._change_field("hunger", Pet.HUNGER_AFTER_SLEEP)
            self._change_field("happiness", Pet.HAPPINESS_AFTER_SLEEP)
            self._change_field("energy", Pet.ENERGY_AFTER_SLEEP)

            msg = f"{self._pet_name} has slept"
            msg_status = "success"

        except RangeError as err:
            msg = f"Action sleep was not made | {err}"
            msg_status = "error"

        self._write_history(msg_status, msg)
        return msg

    def play(self):
        try:
            self._check_field("points", Pet.POINTS_AFTER_PLAY)
            self._check_field("hunger", Pet.HUNGER_AFTER_PLAY)
            self._check_field("energy", Pet.ENERGY_AFTER_PLAY)

            self._change_field("points", Pet.POINTS_AFTER_PLAY)
            self._change_field("hunger", Pet.HUNGER_AFTER_PLAY)
            self._change_field("energy", Pet.ENERGY_AFTER_PLAY)
            self._change_field("happiness", Pet.HAPPINESS_AFTER_PLAY)

            msg = f"{self._pet_name} has played"
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

    def get_pet_name(self):
        return self._pet_name
    
    def get_pet_type(self):
        return self._pet_type

    def get_hunger(self, only_num: bool = False):
        if only_num:
            return str(self._hunger)
        return f"The hunger level of {self._pet_name} is {self._hunger}"

    def get_happiness(self, only_num: bool = False):
        if only_num:
            return str(self._happiness)
        return f"The happiness level of {self._pet_name} is {self._happiness}"

    def get_energy(self, only_num: bool = False):
        if only_num:
            return str(self._energy)
        return f"The energy level of {self._pet_name} is {self._energy}"

    def get_points(self, only_num: bool = False):
        if only_num:
            return str(self._points)
        return f"You have {self._points} points"
    
    def get_log_file(self):
        return self._log_file

    def get_total_state(self):
        state = (
            self._happiness * Pet.HAPPINESS_PERCENT
            + self._energy * Pet.ENERGY_PERCENT
            - self._hunger * Pet.HUNGER_PERCENT
        )
        state_str = (
            f"The total state of {self._pet_name} the {self._pet_type}"
            f"is {state}"
        )
        return state_str

    def get_status(self):
        description = f"""------------------------------
name: {self._pet_name}
type: {self._pet_type}

hunger level: {self._hunger}
happiness level: {self._happiness}
energy level: {self._energy}
total state: {self.get_total_state()}

points: {self._points}
------------------------------"""
        return description

    def _write_history(self, msg_status, msg):
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
