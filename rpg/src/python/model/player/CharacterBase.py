from abc import ABC, abstractmethod
from model.player.races.RaceBase import RaceBase
from model.player.classes.ClassBase import ClassBase
from typing import Dict

class CharacterBase(ABC):
    def __init__(self, name: str, strength: int, dexterity: int, constitution: int,
                 intelligence: int, wisdom: int, charisma: int, race: "RaceBase", char_class: "ClassBase"):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.race = race
        self.char_class = char_class

    @abstractmethod
    def description(self) -> str:
        pass

    def get_attributes(self) -> Dict:
        return {
            "STR": self.strength,
            "DEX": self.dexterity,
            "CON": self.constitution,
            "INT": self.intelligence,
            "WIS": self.wisdom,
            "CHA": self.charisma,
        }

    def get_race_info(self) -> Dict:
        return self.race.traits()

    def get_class_info(self) -> Dict:
        return self.char_class.features()
