from abc import ABC, abstractmethod

from backend.ml_components.ml_component import MLComponent


class ProjectCodeCombiner(ABC):
    """class for combining the different code snippets of the projects MLComponents."""

    @abstractmethod
    def get_combined_code(self, components: list[MLComponent]) -> str:
        """makes use of to_code methods from MLComponent and combines code snippet to one big code string."""
