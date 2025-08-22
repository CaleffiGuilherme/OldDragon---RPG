import random
from typing import List

class RollStrategy:
    def roll(self, sides: int = 6) -> List[int]:
        raise NotImplementedError

class ClassicRoll(RollStrategy):
    def roll(self, sides: int = 6) -> List[int]:
        return [random.randint(1, sides) for _ in range(3)]

class HeroicRoll(RollStrategy):
    def roll(self, sides: int = 6) -> List[int]:
        return [random.randint(1, sides) for _ in range(4)]

class AdventurerRoll(RollStrategy):
    def roll(self, sides: int = 6) -> List[int]:
        return [random.randint(1, sides) for _ in range(3)]


