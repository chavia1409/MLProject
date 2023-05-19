from abc import ABC, abstractmethod

from backend.ml_components.ml_component import MLComponent


class ProjectLinearizer(ABC):
    """class that puts branched MLComponents into a valid linear sequence"""

    @abstractmethod
    def to_linear_sequence(self, components: list[MLComponent]) -> list[MLComponent]:
        """uses pre and suc of MLComponents to determine a valid order"""
