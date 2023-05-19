from abc import ABC, abstractmethod

from backend.ml_components.ml_component import MLComponent


class ProjectHeaderMaker(ABC):
    """Class responsible for creating Python-Code file header."""

    @abstractmethod
    def create_file_header(self, components: list[MLComponent], project_name: str) -> str:
        """returns header of the generated code file as str"""
