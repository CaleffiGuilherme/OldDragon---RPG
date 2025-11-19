import time
from controller.DiceGameController import DiceGameController
from model.attribute_roller import AttributeRoller, ATTRIBUTE_ORDER
from model.player.races.HumanRace import Human
from model.player.races.ElfRace import Elf
from model.player.races.DwarfRace import Dwarf
from model.player.races.GnomeRace import Gnome
from model.player.races.HalflingRace import Halfling
from model.player.races.HalfElfRace import HalfElf
from model.player.classes.WarriorClass import Warrior
from model.player.classes.MageClass import Mage
from model.player.classes.PaladinClass import Paladin
from model.player.CharacterBase import CharacterBase
from database.save_character import save_character_to_json

class GameSystem:
    def __init__(self, exit_number: int = 0):
        self.controller = DiceGameController()
        self.exit_token = str(exit_number)
        self._init_races_and_classes()

    def _init_races_and_classes(self):
        self.races = {
            "1": ("Human", Human()),
            "2": ("Elf", Elf()),
            "3": ("Dwarf", Dwarf()),
            "4": ("Gnome", Gnome()),
            "5": ("Halfling", Halfling()),
            "6": ("Half-Elf", HalfElf())
        }
        self.classes = {
            "1": ("Warrior", Warrior()),
            "2": ("Mage", Mage()),
            "3": ("Paladin", Paladin())
        }

    def run(self) -> None:
        self._show_welcome()
        
        while True:
            self._show_main_menu()
            choice = input("Choose: ").strip()
            
            if choice == self.exit_token:
                self._exit_game()
                return
            elif choice == "1":
                self._create_character()
            elif choice == "2":
                self._run_dice_loop()
            elif choice == "3":
                self._run_attribute_flow()
            else:
                print("Invalid option.\n")
                time.sleep(1)

    def _show_welcome(self):
        print("Welcome to OldDragon RPG!")
        time.sleep(1)
        print(f"Type {self.exit_token} at any prompt to exit.\n")
        time.sleep(1)

    def _show_main_menu(self):
        self._show_ascii_art()
        time.sleep(0.5)
        print("[1] - Create Complete Character")
        print("[2] - Roll Dice")
        print("[3] - Roll Attributes")
        print(f"[{self.exit_token}] - Exit")

    def _show_ascii_art(self):
        print("""
        ________  .____     ________  ________                                      
        \\_____  \\ |    |    \\______ \\ \\______ \\____________     ____   ____   ____  
        /   |   \\|    |     |    |  \\ |    |  \\_  __ \\__  \\   / ___\\ /  _ \\ /    \\ 
        /    |    \\    |___  |    `   \\|    `   \\  | \\// __ \\_/ /_/  >  <_> )   |  \\
        \\_______  /_______ \\/_______  /_______  /__|  (____  /\\___  / \\____/|___|  /
                \\/        \\/        \\/        \\/           \\//_____/             \\/ """)
        time.sleep(0.3)
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

    def _exit_game(self):
        print("Goodbye!")
        time.sleep(1)

    def _create_character(self) -> None:
        print("\n=== CHARACTER CREATION ===\n")
        time.sleep(1)
        
        name = self._get_character_name()
        if not name:
            return
            
        race = self._select_race()
        if not race:
            return
            
        char_class = self._select_class(name, race[0])
        if not char_class:
            return
            
        attributes = self._roll_and_distribute_attributes(name)
        if not attributes:
            return
            
        self._create_and_display_character(name, race[1], char_class[1], attributes)

    def _get_character_name(self) -> str:
        name = input("Enter your character's name: ").strip()
        time.sleep(0.5)
        return name if name != self.exit_token else None

    def _select_race(self) -> tuple:
        print("\n--- SELECT YOUR RACE ---")
        time.sleep(1)
        self._display_race_options()
        
        while True:
            choice = input("Choose your race (1-6): ").strip()
            if choice == self.exit_token:
                return None
            if choice in self.races:
                time.sleep(0.5)
                return self.races[choice]
            print("Invalid option. Choose from 1 to 6.")
            time.sleep(1)

    def _display_race_options(self):
        for key, (race_name, race_obj) in self.races.items():
            traits = race_obj.traits()
            print(f"[{key}] - {race_name}")
            print(f"     Movement: {traits['Movement']}")
            print(f"     Infravision: {'Yes' if traits['Infravision'] else 'No'}")
            print(f"     Alignment: {traits['Alignment']}")
            print(f"     Abilities: {', '.join(traits['Abilities'])}")
            print()
            time.sleep(0.3)

    def _select_class(self, char_name: str, race_name: str) -> tuple:
        print(f"\n--- SELECT YOUR CLASS (Character: {char_name} - {race_name}) ---")
        time.sleep(1)
        self._display_class_options()
        
        while True:
            choice = input("Choose your class (1-3): ").strip()
            if choice == self.exit_token:
                return None
            if choice in self.classes:
                time.sleep(0.5)
                return self.classes[choice]
            print("Invalid option. Choose from 1 to 3.")
            time.sleep(1)

    def _display_class_options(self):
        for key, (class_name, class_obj) in self.classes.items():
            features = class_obj.features()
            print(f"[{key}] - {class_name}")
            print(f"     Hit Dice: {features['HitDice']}")
            print(f"     Weapons: {features['Weapons']}")
            print(f"     Armor: {features['Armor']}")
            print(f"     Special: {features['Special']}")
            print()
            time.sleep(0.3)

    def _roll_and_distribute_attributes(self, char_name: str) -> dict:
        print(f"\n--- ATTRIBUTE ROLLING FOR {char_name.upper()} ---")
        time.sleep(1)
        
        roller = AttributeRoller()
        style = self._get_attribute_style()
        if not style:
            return None
            
        rolls = roller.roll_six(style)
        print(f"\nResults of the 6 dice: {', '.join(str(v) for v in rolls)}")
        time.sleep(1.5)
        
        if style.lower() == "classic":
            return self._assign_classic_attributes(roller, rolls)
        else:
            return self._assign_custom_attributes(roller, rolls)

    def _get_attribute_style(self) -> str:
        style_input = input(
            "Choose your distribution style:\n[Classic] - Classic\n[Heroic] - Heroic\n[Adventurer] - Adventurer\n"
        ).strip()
        time.sleep(0.5)
        return style_input if style_input != self.exit_token else None

    def _assign_classic_attributes(self, roller: AttributeRoller, rolls: list) -> dict:
        assigned = roller.assign_classic(rolls)
        print("\nAttributes (fixed order):")
        for attr in ATTRIBUTE_ORDER:
            condition = roller.get_attribute_condition(attr, assigned[attr])
            print(f"{attr}: {assigned[attr]} ({condition})")
            time.sleep(0.3)
        return assigned

    def _assign_custom_attributes(self, roller: AttributeRoller, rolls: list) -> dict:
        remaining = rolls[:]
        assigned = {}
        
        for attr in ATTRIBUTE_ORDER:
            while True:
                print(f"\nAssign value for {attr}. Remaining values: {remaining}")
                raw = input("Enter an exact value from the list: ").strip()
                
                if raw == self.exit_token:
                    return None
                    
                try:
                    value = int(raw)
                except ValueError:
                    print("Invalid input.")
                    time.sleep(1)
                    continue
                    
                if value in remaining:
                    assigned[attr] = value
                    remaining.remove(value)
                    time.sleep(0.5)
                    break
                print("Value not found in the remaining list.")
                time.sleep(1)
        
        print("\nFinal attributes:")
        for attr in ATTRIBUTE_ORDER:
            condition = roller.get_attribute_condition(attr, assigned[attr])
            print(f"{attr}: {assigned[attr]} ({condition})")
            time.sleep(0.3)
        
        return assigned

    def _create_and_display_character(self, name: str, race, char_class, attributes: dict):
        print("Creating your character...")
        time.sleep(1)
        
        character = Character(
            name=name,
            strength=attributes["STR"],
            dexterity=attributes["DEX"],
            constitution=attributes["CON"],
            intelligence=attributes["INT"],
            wisdom=attributes["WIS"],
            charisma=attributes["CHA"],
            race=race,
            char_class=char_class
        )
        
        print(f"\n=== CHARACTER CREATED SUCCESSFULLY! ===")
        time.sleep(0.5)
        print(character.description())
        try:
            saved_path = save_character_to_json(character)
            print(f"Character saved to: {saved_path}")
        except Exception as exc:
            print(f"Could not save character: {exc}")
        print()
        time.sleep(1)
        
        while True:
            user_input = input(f"Press {self.exit_token} to return to main menu: ").strip()
            if user_input == self.exit_token:
                print("\nReturning to main menu...")
                time.sleep(1)
                print()
                break
            else:
                print("Invalid input. Please press 0 to continue.")
                time.sleep(1)

    def _run_dice_loop(self) -> None:
        style_input = input(
            "Choose style \n[Classic] - Classic\n[Heroic] - Heroic\n[Adventurer] - Adventurer\n"
        ).strip()
        if style_input == self.exit_token:
            return
        self.controller.set_style(style_input or "classic")
        time.sleep(0.5)

        while True:
            self.controller.play_game()
            print()
            time.sleep(0.5)
            user_input = input(
                f"Press Enter to roll again, or type {self.exit_token} to exit: "
            ).strip()
            if user_input == self.exit_token:
                break
            time.sleep(0.5)

    def _run_attribute_flow(self) -> None:
        roller = AttributeRoller()
        style_input = input(
            "Choose your style \n[Classic] - Classic\n[Heroic] - Heroic\n[Adventurer] - Adventurer\n"
        ).strip()
        if style_input == self.exit_token:
            return
        style = style_input or "classic"
        time.sleep(0.5)
        rolls = roller.roll_six(style)
        print(f"\nResults of the 6 dice: {', '.join(str(v) for v in rolls)}")
        time.sleep(1)

        if style.lower() in ("classic"):
            assigned = roller.assign_classic(rolls)
            print("\nAttributes (fixed order):")
            for attr in ATTRIBUTE_ORDER:
                condition = roller.get_attribute_condition(attr, assigned[attr])
                print(f"{attr}: {assigned[attr]} ({condition})")
                time.sleep(0.3)
            print()
            time.sleep(1)
            return

        remaining = rolls[:]
        assigned = {}
        for attr in ATTRIBUTE_ORDER:
            while True:
                print(f"\nAssign value for {attr}. Remaining values: {remaining}")
                raw = input("Enter an exact value from the list: ").strip()
                if raw == self.exit_token:
                    return
                try:
                    value = int(raw)
                except ValueError:
                    print("Invalid input.")
                    time.sleep(1)
                    continue
                if value in remaining:
                    assigned[attr] = value
                    remaining.remove(value)
                    time.sleep(0.5)
                    break
                print("Value not found in the remaining list.")
                time.sleep(1)

        print("\nFinal attributes:")
        for attr in ATTRIBUTE_ORDER:
            condition = roller.get_attribute_condition(attr, assigned[attr])
            print(f"{attr}: {assigned[attr]} ({condition})")
            time.sleep(0.3)
        print()
        time.sleep(1)


class Character(CharacterBase):    
    def description(self) -> str:
        race_info = self.get_race_info()
        class_info = self.get_class_info()
        
        return f"""
Name: {self.name}
Race: {self.race.__class__.__name__}
Class: {self.char_class.__class__.__name__}

ATTRIBUTES:
Strength: {self.strength}
Dexterity: {self.dexterity}
Constitution: {self.constitution}
Intelligence: {self.intelligence}
Wisdom: {self.wisdom}
Charisma: {self.charisma}

RACE CHARACTERISTICS:
Movement: {race_info['Movement']}
Infravision: {'Yes' if race_info['Infravision'] else 'No'}
Alignment: {race_info['Alignment']}
Abilities: {', '.join(race_info['Abilities'])}

CLASS CHARACTERISTICS:
Hit Dice: {class_info['HitDice']}
Weapons: {class_info['Weapons']}
Armor: {class_info['Armor']}
Special: {class_info['Special']}
"""

