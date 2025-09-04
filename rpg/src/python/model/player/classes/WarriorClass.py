from model.player.classes.ClassBase import ClassBase
from typing import Dict

class Warrior(ClassBase):
    def features(self) -> Dict:
        return {
            "HitDice": "1d10 per level",
            "Weapons": "All",
            "Armor": "All",
            "Special": "Better attack progression, physical resistance"
        }



