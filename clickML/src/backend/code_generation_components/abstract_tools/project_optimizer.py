from abc import ABC, abstractmethod

from backend.ml_components.ml_component import MLComponent


class ProjectOptimizer(ABC):
    """class for trimming project to the best possible shape"""

    @abstractmethod
    def optimize_project(self, components: list[MLComponent]) -> list[MLComponent]:
        """returns project in the best possible shape by eliminating unnecessary components"""
