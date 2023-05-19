"""Module that declares structure of MLComponents as interface between GUI and backend."""

from __future__ import annotations

import uuid
from abc import ABC, abstractmethod
from typing import Any, TYPE_CHECKING
from backend.project_toolkit import ProjectToolkit
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor

if TYPE_CHECKING:
    from backend.component_enum import Components


class MLComponent(ABC):

    toolkit: ProjectToolkit = ProjectToolkit([])

    def __init__(self, component_id: uuid) -> None:
        self.__id: uuid = component_id

    @property
    def id(self) -> uuid:
        return self.__id

    @property
    @abstractmethod
    def predecessors(self) -> list[PredecessorDescriptor]:
        """returns list containing all PredecessorDescriptors of this component"""

    @property
    @abstractmethod
    def successors(self) -> list[SuccessorDescriptor]:
        """returns list containing all SuccessorDescriptors of this component"""

    @property
    @abstractmethod
    def values_for_successors(self) -> dict[str, Any]:
        """dict pointing from name of SuccessorDescriptor to data that should be retrieved from next component"""

    @abstractmethod
    def to_code(self) -> str:
        """Returns string with code snippet for this component."""

    @abstractmethod
    def get_needed_imports(self) -> list[str]:
        """Returns list with all needed imports for code snippet of this component as strings."""

    @abstractmethod
    def check_if_valid(self) -> None:
        """
        Points that need to be checked:
        - all data that is specified by user fits it´s domain (e.g. any probability might be between 0 and 1)
        - all data that is required and not just optional from the user is set (means the variable is != DEFAULT)
        - composition between user inputs is valid (e.g. var_1 = 42 then var_3 isn`t allowed to be 43)
        - all specified predecessors (means pre.name_prev != DEFAULT) are connected in a valid way (use
            backend/ml_components/valid_connections to define valid connections);
            you can use toolkit.check_pre_connection_validity()
        - all required predecessors are set (means pre.name_prev != DEFAULT);
            you can use toolkit.get_data_from_predecessors()

        Methode raises exceptions if any of the points is hurt.
        """

    @abstractmethod
    def do_preprocessing(self) -> None:
        """
        retrieving needed data from Predecessors via the values_for_successors property, might do some more things
        depending on the component
        """

    @abstractmethod
    def type(self) -> Components:
        """returns type from Components Enum"""
        pass
