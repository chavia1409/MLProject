from abc import ABC, abstractmethod

from backend.ml_components.ml_component import MLComponent


class ProjectValidator(ABC):
    """class for checking if project status is valid"""

    @abstractmethod
    def check_if_valid(self, components: list[MLComponent]) -> None:
        """does nothing if project model is valid, raises exception otherwise"""
