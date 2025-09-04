from model.player.races.RaceBase import RaceBase
from typing import Dict

class Gnome(RaceBase):
    def traits(self) -> Dict:
        return {
            "Movement": "6m",
            "Infravision": "18m",
            "Alignment": "Neutral",
            "Abilities": [
                "Evaluators",
                "Sagacious and Vigorous",
                "Restrictions"                            
                ]
        }