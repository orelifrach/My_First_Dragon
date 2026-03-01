from os import path
import os

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
    
    HUNGER_AFTER_SLEEP = -15
    ENERGY_AFTER_SLEEP = 20
    
    HUNGER_AFTER_PLAY = 10
    HAPPINESS_AFTER_PLAY = 15
    ENERGY_AFTER_PLAY = -5
    POINTS_AFTER_PLAY = 2
    
    # State Calculation
    HUNGER_PERCENT = 1-0.3 # we need the "nor hungry" percent
    HAPPINESS_PERCENT = 0.4
    ENERGY_PERCENT = 0.3
    
    
    pet_type_list = ["dog", "cat", "fish"]
    
    def __init__(self, name, type):
        self._name = name
        self._type = type
        self._hunger = Pet.HUNGER
        self._happiness = Pet.HAPPINESS
        self._energy = Pet.ENERGY
        self._points = Pet.POINTS
        self._log_path = path.join(path.abspath(path.dirname("pet.py")), "history_log")

    def eat(self):
        self._hunger += Pet.HUNGER_AFTER_EAT
        self._happiness += Pet.HAPPINESS_AFTER_EAT
        self._energy += Pet.ENERGY_AFTER_EAT
        self._points += Pet.POINTS_AFTER_EAT
    
    def sleep(self):
        self._hunger += Pet.HUNGER_AFTER_SLEEP
        self._energy += Pet.ENERGY_AFTER_SLEEP
    
    def play(self):
        self._hunger += Pet.HUNGER_AFTER_PLAY
        self._happiness += Pet.HAPPINESS_AFTER_PLAY
        self._energy += Pet.ENERGY_AFTER_PLAY
        self._points += Pet.POINTS_AFTER_PLAY

    def state(self) -> float:
        state = self._hunger * Pet.HUNGER_PERCENT + self._happiness * Pet.HAPPINESS_PERCENT + self._energy * Pet.ENERGY_PERCENT
        return state

p = Pet("puppy", "dog")
print(p.state())
p.eat()
print(p.state())
p.sleep()
print(p.state())
p.play()
print(p.state())