import os
import json
from typing import Optional
from model.player.CharacterBase import CharacterBase


def save_character_to_json(character: CharacterBase, filename: Optional[str] = None) -> str:
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    saves_dir = os.path.join(base_dir, "saves")
    os.makedirs(saves_dir, exist_ok=True)

    name = getattr(character, "name", "character")
    safe_name = "_".join(name.split())
    filename = filename or os.path.join(saves_dir, f"{safe_name}.json")

    data = character.__dict__.copy()

    try:
        race_obj = getattr(character, "race", None)
        data["race"] = race_obj.__class__.__name__ if race_obj is not None else None
        if hasattr(character, "get_race_info"):
            data["race_info"] = character.get_race_info()
    except Exception:
        data["race"] = str(data.get("race"))

    try:
        class_obj = getattr(character, "char_class", None)
        data["char_class"] = class_obj.__class__.__name__ if class_obj is not None else None
        if hasattr(character, "get_class_info"):
            data["class_info"] = character.get_class_info()
    except Exception:
        data["char_class"] = str(data.get("char_class"))

    for k in ["race_info", "class_info"]:
        if k in data:
            try:
                json.dumps(data[k])
            except TypeError:
                data[k] = str(data[k])

    with open(filename, "w", encoding="utf-8") as fout:
        json.dump(data, fout, indent=4, ensure_ascii=False)

    return filename
