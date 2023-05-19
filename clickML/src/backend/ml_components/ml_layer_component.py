"""Module that declares structure of MLComponents as interface between GUI and backend."""

from __future__ import annotations
from abc import ABC, abstractmethod
import uuid
from backend.project_toolkit import ProjectToolkit
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.component_enum import Components


class MLLayerComponent(ABC):

    toolkit: ProjectToolkit = ProjectToolkit([])

    def __init__(self, component_id: uuid) -> None:
        self.__id: uuid = component_id

    @property
    def id(self) -> uuid:
        return self.__id

    @abstractmethod
    def to_code(self) -> str:
        """Returns string with code snippet for this layer in shape 'model.add(LayerName(parameters))'."""

    @staticmethod
    @abstractmethod
    def get_needed_imports() -> list[str]:
        """Returns list with all needed imports for code snippet of this layer as strings."""

    @abstractmethod
    def check_if_valid(self) -> None:
        """
        Points that need to be checked:
        - all data that is specified by user fits it´s domain (e.g. any probability might be between 0 and 1)
        - all data that is required and not just optional from the user is set (means the variable is != DEFAULT)
        - composition between user inputs is valid (e.g. var_1 = 42 then var_3 isn`t allowed to be 43)

        Methode raises exceptions if any of the points is hurt.
        """

    @abstractmethod
    def set_output_shape(self, output_shape: str) -> bool:
        """sets Output-Shape in last layer and returns True, returns False if this layer is not a valid last layer"""

    @abstractmethod
    def type(self) -> Components:
        pass
