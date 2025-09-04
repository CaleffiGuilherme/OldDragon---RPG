from model.player.races.RaceBase import RaceBase
from typing import Dict

class Elf(RaceBase):
    def traits(self) -> Dict:
        return {
            "Movement": "9m",
            "Infravision": "18m",
            "Alignment": "Neutral Tendency",
            "Abilities": [
                "Natural Perception",
                "Graceful",
                "Racial Weapon",
                "Immunity to sleep/Ghoul paralysis"
            ]
        }