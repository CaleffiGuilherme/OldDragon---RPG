import os
import sys
from typing import List, Dict, Tuple

from flask import Flask, render_template, request, redirect, url_for, session, flash

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PY_SRC_DIR = os.path.dirname(CURRENT_DIR)
if PY_SRC_DIR not in sys.path:
    sys.path.append(PY_SRC_DIR)

from model.attribute_roller import AttributeRoller, ATTRIBUTE_ORDER
from view.GameSystem import Character
from model.player.races.HumanRace import Human
from model.player.races.ElfRace import Elf
from model.player.races.DwarfRace import Dwarf
from model.player.races.GnomeRace import Gnome
from model.player.races.HalflingRace import Halfling
from model.player.races.HalfElfRace import HalfElf
from model.player.classes.WarriorClass import Warrior
from model.player.classes.MageClass import Mage
from model.player.classes.PaladinClass import Paladin


app = Flask(__name__)
app.secret_key = "oldragon_webapp_dev_key"


def get_races() -> Dict[str, Tuple[str, object]]:
    return {
        "1": ("Human", Human()),
        "2": ("Elf", Elf()),
        "3": ("Dwarf", Dwarf()),
        "4": ("Gnome", Gnome()),
        "5": ("Halfling", Halfling()),
        "6": ("Half-Elf", HalfElf()),
    }


def get_classes() -> Dict[str, Tuple[str, object]]:
    return {
        "1": ("Warrior", Warrior()),
        "2": ("Mage", Mage()),
        "3": ("Paladin", Paladin()),
    }


def normalize_style(style: str) -> str:
    if not style:
        return "classic"
    return style.strip().lower()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/guide")
def guide():
    return render_template("guide.html")


@app.route("/character", methods=["GET", "POST"])
def character():
    races = get_races()
    classes = get_classes()
    roller = AttributeRoller()

    rolls: List[int] = session.get("char_rolls", [])
    style = session.get("char_style", "classic")
    assigned: Dict[str, int] = {}
    conditions: Dict[str, str] = {}
    remaining_values: List[int] = []
    character_description = None
    character_view: Dict[str, object] | None = None
    error = None
    show_assign = False

    if request.method == "POST":
        step = request.form.get("step", "setup")

        if step == "setup":
            name = request.form.get("name", "").strip()
            race_key = request.form.get("race")
            class_key = request.form.get("char_class")
            style = normalize_style(request.form.get("style", "classic"))

            if not name or race_key not in races or class_key not in classes:
                flash("Please fill all fields.")
                return redirect(url_for("character"))

            session["char_name"] = name
            session["char_race_key"] = race_key
            session["char_class_key"] = class_key
            session["char_style"] = style

            rolls = roller.roll_six(style)
            session["char_rolls"] = rolls
            session["char_assigned"] = {}
            remaining_values = rolls[:]
            show_assign = True

        elif step == "assign":
            name = session.get("char_name")
            race_key = session.get("char_race_key")
            class_key = session.get("char_class_key")
            style = session.get("char_style", "classic")
            rolls = session.get("char_rolls", [])
            current_assigned = session.get("char_assigned", {})

            if not all([name, race_key, class_key, rolls]):
                flash("Session expired. Start over.")
                return redirect(url_for("character"))

            if style == "classic":
                assigned = roller.assign_classic(rolls)
                remaining_values = []
            else:
                attr_to_assign = request.form.get("assign_attr")
                if attr_to_assign and attr_to_assign in ATTRIBUTE_ORDER:
                    try:
                        value_raw = request.form.get("value")
                        value = int(value_raw)
                        current_remaining = rolls[:]
                        for assigned_attr, assigned_value in current_assigned.items():
                            if assigned_value in current_remaining:
                                current_remaining.remove(assigned_value)
                        
                        if value not in current_remaining:
                            error = f"Value {value} not available for {attr_to_assign}"
                        else:
                            current_assigned[attr_to_assign] = value
                            session["char_assigned"] = current_assigned
                            assigned = current_assigned.copy()
                    except Exception as exc:
                        error = str(exc)
                else:
                    assigned = current_assigned.copy()
                
                remaining_values = rolls[:]
                for assigned_value in assigned.values():
                    if assigned_value in remaining_values:
                        remaining_values.remove(assigned_value)

            if not error and assigned:
                for attr in ATTRIBUTE_ORDER:
                    if attr in assigned:
                        conditions[attr] = roller.get_attribute_condition(attr, assigned[attr])

                if len(assigned) == len(ATTRIBUTE_ORDER):
                    race_obj = races[race_key][1]
                    class_obj = classes[class_key][1]

                    character_obj = Character(
                        name=name,
                        strength=assigned["STR"],
                        dexterity=assigned["DEX"],
                        constitution=assigned["CON"],
                        intelligence=assigned["INT"],
                        wisdom=assigned["WIS"],
                        charisma=assigned["CHA"],
                        race=race_obj,
                        char_class=class_obj,
                    )
                    character_description = character_obj.description()
                    character_view = {
                        "name": name,
                        "race_name": race_obj.__class__.__name__,
                        "class_name": class_obj.__class__.__name__,
                        "attributes": assigned,
                        "race_info": race_obj.traits(),
                        "class_info": class_obj.features(),
                    }

                    for key in [
                        "char_name",
                        "char_race_key",
                        "char_class_key",
                        "char_style",
                        "char_rolls",
                        "char_assigned",
                    ]:
                        session.pop(key, None)
                else:
                    show_assign = True

    return render_template(
        "character.html",
        races=get_races(),
        classes=get_classes(),
        style=style,
        rolls=rolls,
        assigned=assigned,
        conditions=conditions,
        remaining_values=remaining_values,
        character_description=character_description,
        character_view=character_view,
        show_assign=show_assign,
        ATTRIBUTE_ORDER=ATTRIBUTE_ORDER,
        error=error,
    )


def create_app():
    return app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)


