from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.ml_components.ml_component import MLComponent


class ProjectCodeGenerator(ABC):
    """class for putting code and import snippets of MLComponents together"""

    @abstractmethod
    def to_code(self, components: list[MLComponent], project_name: str) -> str:
        """returns a string containing the code for given components"""
