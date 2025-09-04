from model.player.classes.ClassBase import ClassBase
from typing import Dict

class Paladin(ClassBase):
    def features(self) -> Dict:
        return {
            "HitDice": "1d10 per level",
            "Weapons": "All",
            "Armor": "All",
            "Special": "Lay on hands, detect evil, immunity to disease, aura of protection"
        }   