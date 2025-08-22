import random
from typing import List, Dict


ATTRIBUTE_ORDER: List[str] = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

ATTRIBUTE_CONDITIONS = {
    "STR": {
        (3, 8): "Weak",
        (9, 12): "Average", 
        (13, 16): "Strong",
        (17, 18): "Pretty Strong"
    },
    "DEX": {
        (3, 8): "Slow",
        (9, 12): "Average",
        (13, 16): "Quick", 
        (17, 18): "Precise"
    },
    "CON": {
        (3, 8): "Frail",
        (9, 12): "Average",
        (13, 16): "Resistant",
        (17, 18): "Healthy"
    },
    "INT": {
        (3, 8): "Dumb",
        (9, 12): "Average",
        (13, 16): "Smart",
        (17, 18): "Genius"
    },
    "WIS": {
        (3, 8): "Fool",
        (9, 12): "Average", 
        (13, 16): "Intuitive",
        (17, 18): "Prescient"
    },
    "CHA": {
        (3, 8): "No Manners",
        (9, 12): "Average",
        (13, 16): "Influencer",
        (17, 18): "Idol"
    }
}


class AttributeRoller:
    def roll_3d6(self) -> int:
        return sum(random.randint(1, 6) for _ in range(3))

    def roll_4d6_drop_lowest(self) -> int:
        rolls = sorted([random.randint(1, 6) for _ in range(4)])
        return sum(rolls[1:])

    def roll_six(self, style: str) -> List[int]:
        normalized = style.strip().lower()
        if normalized in ("classic"):
            return [self.roll_3d6() for _ in range(6)]
        if normalized in ("heroic"):
            return [self.roll_4d6_drop_lowest() for _ in range(6)]
        if normalized in ("adventurer"):
            return [self.roll_3d6() for _ in range(6)]
        # default
        return [self.roll_3d6() for _ in range(6)]

    def assign_classic(self, values: List[int]) -> Dict[str, int]:
        return {attr: values[idx] for idx, attr in enumerate(ATTRIBUTE_ORDER)}

    def get_attribute_condition(self, attribute: str, value: int) -> str:
        """Get the condition description for an attribute value."""
        if attribute not in ATTRIBUTE_CONDITIONS:
            return "Unknown"
        
        for (min_val, max_val), description in ATTRIBUTE_CONDITIONS[attribute].items():
            if min_val <= value <= max_val:
                return description
        
        return "Unknown"

    def get_all_attribute_conditions(self, attributes: Dict[str, int]) -> Dict[str, str]:
        """Get condition descriptions for all attributes."""
        return {
            attr: self.get_attribute_condition(attr, value) 
            for attr, value in attributes.items()
        }


