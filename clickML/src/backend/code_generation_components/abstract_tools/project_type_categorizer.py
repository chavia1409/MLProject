from abc import ABC, abstractmethod

from backend.component_enum import Categories
from backend.ml_components.ml_component import MLComponent


class ProjectTypeCategorizer(ABC):
    """class that matches project to one of the possible use cases (e.g. regression, text generation)"""

    @abstractmethod
    def get_category(self, components: list[MLComponent]) -> Categories:
        """returns guess what type of project it is meant to be and returns matching Categories Enum member value"""
