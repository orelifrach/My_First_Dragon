from os import path
from range_error import RangeError
import logging

class Pet():    
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
    HUNGER_PERCENT = 1-0.3 # we need the "not hungry" percent
    HAPPINESS_PERCENT = 0.4
    ENERGY_PERCENT = 0.3
    
    # Actions list
    _actions_list = ["eat", "sleep", "play", "state", "dascription"]
    # Pet type list
    _pet_type_list = ["dog", "cat", "fish"]
    
    def get_actions_list():
        return Pet._actions_list
    
    def get_pet_type_list():
        return Pet._pet_type_list
    
    def verify_type(type: str):
        return type in Pet._pet_type_list
    
    def verify_name(name: str):
        return 2 < len(name) < 9 and name.isalpha()
    
    
    def __init__(self, name: str, type: str):
        self._name = name
        self._type = type
        self._hunger = Pet.HUNGER
        self._happiness = Pet.HAPPINESS
        self._energy = Pet.ENERGY
        self._points = Pet.POINTS
        self._log_path = path.join(path.abspath(path.dirname("pet.py")), "history_log")

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
        print(msg)
    
    
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
        print(msg)
            
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
        print(msg)

    def state(self) -> float:
        state = self._hunger * Pet.HUNGER_PERCENT + self._happiness * Pet.HAPPINESS_PERCENT + self._energy * Pet.ENERGY_PERCENT
        return state

    def __str__(self):
        description = f"""------------------------------
name: {self._name}
type: {self._type}

hunger level: {self._hunger}
happiness level: {self._happiness}
energy level: {self._energy}

points: {self._points}
------------------------------"""
        return description
    
    
    def _check_field(self, field: str, change: int):
        if field == "hunger":
            if self._hunger + change > 100:
                raise RangeError("Your pet is too hungry to make this action")
            elif self._hunger + change < 0:
                raise RangeError("Your pet is too full to make this action")
        elif field == "energy":
            if self._energy + change < 0:
                raise RangeError("Your pet doesnt have enough energy to make this action")
        elif field == "points":
            if self._points + change < 0:
                raise RangeError("You dont have enough points to make this action")
    
    def _change_field(self, field: str, change: int):
        err_msg = ""
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

    def _write_history(self, msg_status, msg):
        logging.basicConfig(filename=self._log_path, format="%(asctime)s  %(levelname)s | %(message)s", datefmt="%m/%d/%Y %I:%M %p", level=logging.DEBUG)
        if msg_status == "success":
            logging.info(msg)
        elif msg_status == "error":
            logging.error(msg)
        

p = Pet("puppy", "dog")
p.eat()
p.eat()
p.eat()
p.eat()
p.eat()
p.eat()
p.sleep()
p.play()
p.play()
p.play()
p.play()
p.play()
p.play()
p.play()
p.play()
p.play()
p.play()
p.play()
