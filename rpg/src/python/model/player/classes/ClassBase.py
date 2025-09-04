from abc import ABC, abstractmethod
from typing import Dict

class ClassBase(ABC):
    @abstractmethod
    def features(self) -> Dict:
        pass
