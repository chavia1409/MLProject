from abc import ABC, abstractmethod

from backend.ml_components.ml_component import MLComponent


class ProjectImportManager(ABC):
    """class for combining the different imports of the projects MLComponents."""

    @abstractmethod
    def get_shaped_imports(self, components: list[MLComponent]) -> str:
        """makes use of get_needed_imports methods from MLComponent and combines imports to one big import string."""
