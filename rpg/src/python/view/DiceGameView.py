class DiceGameView:
    def show_rolls(self, rolls, sides=6):
        for idx, value in enumerate(rolls, start=1):
            print(f"Rolling a {sides}-sided dice #{idx}: {value}")

    def show_total(self, total):
        print(f"Total: {total}")

    def show_result(self, is_success):
        if is_success:
            print("Success!")
        else:
            print("Failure.")