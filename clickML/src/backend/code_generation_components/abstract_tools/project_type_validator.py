from abc import ABC, abstractmethod

from backend.ml_components.ml_component import MLComponent


class ProjectTypeValidator(ABC):
    """
    class that checks is project is valid respecting the project type.
    One class is responsible for one project type
    """

    @abstractmethod
    def check_if_valid(self, components: list[MLComponent]) -> None:
        """raises exception if something is wrong with the project"""
