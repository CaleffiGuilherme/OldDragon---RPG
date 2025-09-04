from model.player.races.RaceBase import RaceBase
from typing import Dict

class Halfling(RaceBase):
    def traits(self) -> Dict:
        return {
            "Movement": "6m",
            "Infravision": False,
            "Alignment": "Neutral",
            "Abilities": [
                "Stealth",
                "Bold",
                "Good Aim",
                "Small",
                "Restrictions"
            ]
        }