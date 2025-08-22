import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from view.GameSystem import GameSystem

def main():
    game = GameSystem(exit_number=0)
    game.run()

if __name__ == "__main__":
    main()