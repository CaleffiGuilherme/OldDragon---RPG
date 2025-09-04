# OldDragon RPG - Character Creation System

A complete character creation system for OldDragon RPG, developed in Python with object orientation and **clean, organized architecture**.

## 🎯 Features

### ✅ Attribute System
- **Classic Style**: Fixed attribute distribution (STR, DEX, CON, INT, WIS, CHA)
- **Heroic Style**: Free choice of values for each attribute
- **Adventurer Style**: Free choice of values for each attribute

### ✅ Race System
- **Human**: Movement 9m, no infravision, any alignment
- **Elf**: Movement 9m, infravision 18m, neutral tendency
- **Dwarf**: Movement 6m, infravision 18m, order
- **Gnome**: Movement 6m, infravision 18m, neutral
- **Halfling**: Movement 6m, no infravision, neutral
- **Half-Elf**: Movement 9m, infravision 9m, chaos

### ✅ Class System
- **Warrior**: Hit dice 1d10, all weapons and armor
- **Mage**: Hit dice 1d4, only daggers and staffs, no armor
- **Paladin**: Hit dice 1d10, all weapons and armor

### ✅ User Experience
- **Interactive Flow**: Step-by-step character creation process
- **Menu Control**: Press 0 to return to main menu after character creation
- **Clear Navigation**: Intuitive menu system with proper flow control
- **Natural Timing**: Strategic pauses for better readability and immersion
- **Smooth Transitions**: Well-paced information display with appropriate delays

## 🏗️ Clean and Organized Architecture

### ✨ **Applied Design Principles**
- **Single Responsibility Principle**: Each method has a single responsibility
- **Clean Code**: Readable, maintainable, and well-documented code
- **Method Extraction**: Large methods broken into smaller, focused methods
- **Descriptive Naming**: Names that describe exactly what they do

### 🔧 **Organized Structure**
- **Interface Methods**: Manage user presentation
- **Logic Methods**: Separate business logic from interface
- **Validation Methods**: Check inputs and states
- **Creation Methods**: Coordinate character creation flow

## 🚀 How to Run

1. Navigate to the project directory:
```bash
cd rpg/src/python
```

2. Run the game:
```bash
python run.py
```

## 🎮 How to Play

1. **Main Menu**: Choose option [1] - Create Complete Character
2. **Name**: Enter your character's name
3. **Race**: Select one of the 6 available races (1-6)
4. **Class**: Choose one of the 3 classes (1-3)
5. **Attributes**: Choose distribution style and roll dice
6. **Result**: View your complete character created!
7. **Return**: **Press 0 to return to main menu**

## 🏗️ Project Architecture

```
rpg/src/python/
├── controller/          # Game controllers
├── model/              # Data models
│   ├── player/         # Character classes
│   │   ├── races/      # Race implementations
│   │   └── classes/    # Class implementations
│   └── attribute_roller.py  # Rolling system
├── view/               # User interface
│   └── GameSystem.py   # Main system (REFACTORED!)
└── main/               # Main files
    └── main.py         # Entry point
```

## 🎲 Technical Characteristics

- **Language**: Python 3.x
- **Paradigm**: Object Orientation
- **Patterns**: MVC (Model-View-Controller)
- **Architecture**: Clean Code + Single Responsibility Principle
- **Inheritance**: Abstract base classes for races and classes
- **Polymorphism**: Specific implementations for each race/class
- **User Experience**: Strategic timing with `time.sleep()` for natural flow

## 📋 Requirements

- Python 3.6+
- No external dependencies

## 🎯 Evaluation Criteria

- ✅ Use of object orientation
- ✅ Implementation of 3 attribute distribution forms
- ✅ Race system with common and specific characteristics
- ✅ Class system with specific rules
- ✅ Functional user interface
- ✅ **Organized, clean, and well-structured code**
- ✅ **Architecture following Clean Code principles**
- ✅ **Proper user flow control and navigation**
- ✅ **Enhanced user experience with natural timing**

### ✅ **Structural Organization**
- Clear separation between interface and logic
- Well-organized private methods
- Linear and clear execution flow

### ✅ **User Experience**
- **Interactive character creation flow**
- **Proper menu navigation control**
- **Clear instructions for user actions**
- **Natural timing and pacing**
- **Smooth transitions between steps**

## 🚀 Future Improvements

- Character saving system
- Class requirement validation
- Equipment system
- Graphical interface
- Combat system
- **Automated unit tests**
- **Logging system**
