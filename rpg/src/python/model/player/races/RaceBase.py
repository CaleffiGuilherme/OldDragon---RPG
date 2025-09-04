from abc import ABC, abstractmethod
from typing import Dict

class RaceBase(ABC):
    @abstractmethod
    def traits(self) -> Dict:
        return {
            "Movement": "Any",
            "Infravision": False,
            "Alignment": "Any",
            "Abilities": []
        }

