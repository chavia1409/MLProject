from abc import ABC, abstractmethod


class ProjectCodeStyler(ABC):
    """class for improve style of generated code"""

    @abstractmethod
    def improve_style(self, code: str) -> str:
        """takes given code and returns the best possible styled code"""
