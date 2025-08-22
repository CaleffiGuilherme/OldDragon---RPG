from abc import ABC, abstractmethod

class CharacterBase(ABC):
    def __init__(self, strength: int, dexterity: int, constitution: int,
                intelligence: int, wisdom: int, charisma: int):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    @abstractmethod
    def description(self) -> str:
        """Return a description of the character."""
        pass

    def get_attributes(self) -> dict:
        """Return the character's attributes as a dictionary."""
        return {
            "STR": self.strength,
            "DEX": self.dexterity,
            "CON": self.constitution,
            "INT": self.intelligence,
            "WIS": self.wisdom,
            "CHA": self.charisma
        }
