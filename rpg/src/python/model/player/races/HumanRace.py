from model.player.races.RaceBase import RaceBase
from typing import Dict

class Human(RaceBase):
    def traits(self) -> Dict:
        return {
            "Movement": "9m",
            "Infravision": False,
            "Alignment": "Any",
            "Abilities": [
                "Learning",
                "Adaptability"
            ]
        }