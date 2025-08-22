from model.roll_strategies import RollStrategy, ClassicRoll


class DiceGameModel:
    def __init__(self, strategy: RollStrategy | None = None):
        self.dice_rolls: list[int] = []
        self.total = 0
        self.strategy: RollStrategy = strategy if strategy is not None else ClassicRoll()

    def set_strategy(self, strategy: RollStrategy) -> None:
        self.strategy = strategy

    def roll(self, sides: int = 6) -> None:
        self.dice_rolls = self.strategy.roll(sides)
        self.total = sum(self.dice_rolls)

    def is_success(self) -> bool:
        return self.total > 6
