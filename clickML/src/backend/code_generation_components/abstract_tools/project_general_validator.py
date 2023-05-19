from abc import ABC, abstractmethod

from backend.ml_components.ml_component import MLComponent


class ProjectGeneralValidator(ABC):
    """
    checks if general requirements to projects are fulfilled
    (without checking requirements for special project categories).
    """

    @abstractmethod
    def check_if_valid(self, components: list[MLComponent]) -> None:
        """
        checks general requirements, makes use of check_if_valid methods in MLComponents,
        raises exceptions if something is wrong
        """
