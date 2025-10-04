from model.player.classes.ClassBase import ClassBase
from typing import Dict

class Mage(ClassBase):
    def features(self) -> Dict:
        return {
            "HitDice": "1d4 per level",
            "Weapons": "Daggers, Staffs",
            "Armor": "None",
            "Special": "Magic spells, Grimory"
        }   