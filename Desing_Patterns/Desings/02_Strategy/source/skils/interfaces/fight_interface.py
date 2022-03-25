from abc import ABC, abstractmethod

class SkillInterface(ABC):
    @abstractmethod
    def behavior(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def level_atribute(self) -> None:
        raise NotImplementedError