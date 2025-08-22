from model.DiceGameModel import DiceGameModel
from model.roll_strategies import ClassicRoll, HeroicRoll, AdventurerRoll, RollStrategy
from view.DiceGameView import DiceGameView

class DiceGameController:
    def __init__(self):
        self.model = DiceGameModel()
        self.view = DiceGameView()

    def set_style(self, style: str) -> None:
        normalized = style.strip().lower()
        strategy: RollStrategy
        if normalized in ("classic"):
            strategy = ClassicRoll()
        elif normalized in ("heroic"):
            strategy = HeroicRoll()
        elif normalized in ("adventurer"):
            strategy = AdventurerRoll()
        else:
            strategy = ClassicRoll()
        self.model.set_strategy(strategy)

    def play_game(self):
        self.model.roll()
        self.view.show_rolls(self.model.dice_rolls)
        self.view.show_total(self.model.total)
        self.view.show_result(self.model.is_success())