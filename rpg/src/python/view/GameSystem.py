from controller.DiceGameController import DiceGameController
from model.attribute_roller import AttributeRoller, ATTRIBUTE_ORDER

class GameSystem:
    def __init__(self, exit_number: int = 0):
        self.controller = DiceGameController()
        self.exit_token = str(exit_number)

    def run(self) -> None:
        print("Welcome to OldDragon RPG!")
        print(f"Type {self.exit_token} at any prompt to exit.\n")

        while True:
            print("""
        ________  .____     ________  ________                                      
        \\_____  \\ |    |    \\______ \\ \\______ \\____________     ____   ____   ____  
        /   |   \\|    |     |    |  \\ |    |  \\_  __ \\__  \\   / ___\\ /  _ \\ /    \\ 
        /    |    \\    |___  |    `   \\|    `   \\  | \\// __ \\_/ /_/  >  <_> )   |  \\
        \\_______  /_______ \\/_______  /_______  /__|  (____  /\\___  / \\____/|___|  /
                \\/        \\/        \\/        \\/           \\//_____/             \\/ """)
            print("""                               ______________                               
                    ,===:'.,            `-._                           
Art by                       `:.`---.__         `-._                       
 John VanderZwaag              `:.     `--.         `.                     
                                  \\.        `.         `.                   
                          (,,(,    \\.         `.   ____,-`.,                
                       (,'     `/   \\.   ,--.___`.'                         
                   ,  ,'  ,--.  `,   \\.;'         `                         
                    `{D, {    \\  :    \\;                                    
                      V,,'    /  /    //                                    
                      j;;    /  ,' ,-//.    ,---.      ,                    
                      \\;'   /  ,' /  _  \\  /  _  \\   ,'/                    
                            \\   `'  / \\  `'  / \\  `.' /                     
                             `.___,'   `.__,'   `.__,'  VZ""")
            print("[1] - Roll dice")
            print("[2] - Roll attributes")
            print(f"[{self.exit_token}] - Exit")
            choice = input("Choose: ").strip()
            if choice == self.exit_token:
                print("Goodbye!")
                return
            if choice == "1":
                self._run_dice_loop()
            elif choice == "2":
                self._run_attribute_flow()
            else:
                print("Invalid option.\n")

    def _run_dice_loop(self) -> None:
        style_input = input(
            "Choose style \n[Classic]\n[Heroic]\n[Adventurer]\n"
        ).strip()
        if style_input == self.exit_token:
            return
        self.controller.set_style(style_input or "classic")

        while True:
            self.controller.play_game()
            print()
            user_input = input(
                f"Press Enter to roll again, or type {self.exit_token} to exit: "
            ).strip()
            if user_input == self.exit_token:
                break

    def _run_attribute_flow(self) -> None:
        roller = AttributeRoller()
        style_input = input(
            "Choose your style \n[Classic]\n[Heroic]\n[Adventurer]\n"
        ).strip()
        if style_input == self.exit_token:
            return
        style = style_input or "classic"
        rolls = roller.roll_six(style)
        print("\nResults of the 6 rolls:")
        print(", ".join(str(v) for v in rolls))

        if style.lower() in ("classic"):
            assigned = roller.assign_classic(rolls)
            print("\nAttributes (fixed order):")
            for attr in ATTRIBUTE_ORDER:
                condition = roller.get_attribute_condition(attr, assigned[attr])
                print(f"{attr}: {assigned[attr]} ({condition})")
            print()
            return

        remaining = rolls[:]
        assigned = {}
        for attr in ATTRIBUTE_ORDER:
            while True:
                print(f"\nAssign value for {attr}. Remaining: {remaining}")
                raw = input("Enter an exact value from the list: ").strip()
                if raw == self.exit_token:
                    return
                try:
                    value = int(raw)
                except ValueError:
                    print("Invalid input.")
                    continue
                if value in remaining:
                    assigned[attr] = value
                    remaining.remove(value)
                    break
                print("Value not found in the remaining list.")

        print("\nFinal attributes:")
        for attr in ATTRIBUTE_ORDER:
            condition = roller.get_attribute_condition(attr, assigned[attr])
            print(f"{attr}: {assigned[attr]} ({condition})")
        print()

