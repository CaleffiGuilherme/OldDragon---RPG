from model.player.races.RaceBase import RaceBase
from typing import Dict

class Dwarf(RaceBase):
    def traits(self) -> Dict:
        return {
            "Movement": "6m",
            "Infravision": "18m",
            "Alignment": "Order",
            "Abilities": [
                "Miners",
                "Vigorous",
                "Large Weapons",
                "Enemies"
            ]
        }