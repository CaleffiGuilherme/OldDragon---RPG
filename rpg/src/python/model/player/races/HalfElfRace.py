from model.player.races.RaceBase import RaceBase
from typing import Dict

class HalfElf(RaceBase):
    def traits(self) -> Dict:
        return {
            "Movement": "9m",
            "Infravision": "9m",
            "Alignment": "Chaos",
            "Abilities": [
                "Learning",
                "Graceful and Vigorous",
                "Extra Language",
                "Immunities"
            ]
        }