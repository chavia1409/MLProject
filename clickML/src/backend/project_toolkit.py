"""
ProjectToolkit that every MLComponent holds to get access to global project scope including some functions.
Also used from some code generation tools.
"""

from __future__ import annotations

import uuid
from typing import Any, TYPE_CHECKING

from backend.component_enum import Components
from common.exceptions.click_ml_exceptions import InternalError, ComponentConnectionError
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.pre_suc_descriptors import PredecessorDescriptor

if TYPE_CHECKING:
    from backend.ml_components.ml_component import MLComponent


class ProjectToolkit:

    def __init__(self, component_list: list[MLComponent]) -> None:
        self.component_list = component_list

    def get_component(self, component_id: uuid) -> MLComponent:
        """
        returns MLComponent from project that matches given component_id

        Attributes:
        component_id: uuid
            id of the searched MLComponent
        """
        for component in self.component_list:
            if component.id == component_id:
                return component
        raise InternalError("There is no component with given ID")

    def get_data_from_predecessor(self, pre_descriptor: PredecessorDescriptor) -> Any:
        """
        Gets data for preprocessing variables, makes use of MLComponent.values_for_successors property.
        Returns DEFAULT pre_descriptor does not point to another component

        Attributes:
        pre_descriptor: PredecessorDescriptor
            PreNode for which data from SucNode of another previous MLComponent should be retrieved
        """
        if pre_descriptor.id_prev == DEFAULT:
            return DEFAULT
        pre_component = self.get_component(pre_descriptor.id_prev)
        for suc in pre_component.successors:
            if suc.name == pre_descriptor.name_prev:
                return pre_component.values_for_successors[suc.name]
        raise InternalError("Value cannot be returned!")

    def check_pre_connection_validity(self, pre: PredecessorDescriptor,
                                      valid_connections: set[tuple[str, str]]) -> None:
        """
        Checks if PredecessorDescriptor points to valid Node of another MLComponent.

        Attributes:
        pre: PredecessorDescriptor
            PreDes from any MLComponent
        valid_connections: set[tuple[str, str]]
            Set of valid connections (each connection has shape (componentName, SuccessorDescriptorName)
        """
        if pre.id_prev == DEFAULT:
            return
        connection_component = self.get_component(pre.id_prev)
        connection = (connection_component.type(), pre.name_prev)
        if connection in valid_connections:
            return
        current_component_name = None
        for suc in connection_component.successors:
            if suc.name == pre.name_prev:
                current_component_name = self.get_component(suc.id_next).__class__.__name__
                break
        connection_repr = (connection[0].value, connection[1])
        raise ComponentConnectionError(current_component_name, pre.name,
                                       f"{connection_repr} is not a valid connection!")

    def has_settable_component(self, already_set: list[MLComponent]):
        """
        Checks if any MLComponent in component_list is settable (means that the component is not already set and do not
        have any unset predecessors)

        Attributes:
        already_set: list[MLComponent]
            list of components for which do_preprocessing() has already been called
        """
        for component in self.component_list:
            if not (self.has_unset_predecessors(component, already_set) or component in already_set):
                return True
        return False

    def has_unset_predecessors(self, component: MLComponent, already_set: list[MLComponent]) -> bool:
        """
        Checks if given component has any unset predecessors

        Attributes:
        component: MLComponent
            the MLComponent that has to be checked
        already_set: list[MLComponent]
            list of components for which do_preprocessing() has already been called
        """
        for pre in component.predecessors:
            if pre.name_prev != DEFAULT and self.get_component(pre.id_prev) not in already_set:
                return True
        return False

    def get_number_of_occurrences(self, types: set[Components]) -> int:
        """
        returns number of how many times a component of the types occurs in the project

        Attributes:
        types: set[Components]
            set with all component types that should be checked for
        """
        count = 0
        for component in self.component_list:
            if component.type() in types:
                count += 1
        return count

    @staticmethod
    def create_param_string(parameters: dict[str, Any], indent_depth: int = 0, max_line_len: int = 100,
                            no_repr: tuple[str, ...] = ()) -> str:
        """
        Method that creates String in shape: "param=value, param2=value2..."
        Parameters with DEFAULT-literals will be ignored.
        All entries in parameters should have appropriate reprs or can be converted to str.

        Attributes:
        parameters: dict[str, Any]
            given parameters in shape {"param_name": param_value, "param2_name": param2_value...}
        indent_depth: int
            indent depth of the code block where the param_string should be inserted in, can be used for better style
        max_line_len: int
            method will insert a newline after max_line_len chars
        no_repr: tuple[str]
            tuple of dictionary keys from parameters which values should be inserted as str() instead of repr()
        """

        # creating param string
        param_str = ""
        for var_name, var_value in parameters.items():
            if var_value != DEFAULT and var_name not in no_repr:
                param_str += (var_name + "=" + repr(var_value) + ", ")
            elif var_value != DEFAULT:
                param_str += (var_name + "=" + str(var_value) + ", ")

        # style improvements
        if len(param_str) > 200:
            param_str = "\n" + (indent_depth + 1) * "\t" + param_str
        for i in range(max_line_len, len(param_str),  max_line_len):
            index = param_str.rfind(", ", 0, i)
            if index == -1:
                continue
            param_str = param_str[:index+1] + "\n" + (indent_depth + 1) * "\t" + param_str[index+2:]
        return param_str[0:len(param_str) - 2]

    @staticmethod
    def check_needed_predecessors(predecessors: list[PredecessorDescriptor], component_name: str) -> None:
        """
        Method that checks if all predecessors in list have set a formal valid connection to another component
        (meaning that predecessor`s id_prev and name_prev are set).

        Attributes:
            predecessors: list[PredecessorDescriptor]
                list of predecessors from which a connection to another component is expected
            component_name: str
                name of the component where the predecessors belong to
        """
        for predecessor in predecessors:
            if predecessor.id_prev == DEFAULT or predecessor.name_prev == DEFAULT:
                raise ComponentConnectionError(component_name, predecessor.name,
                                               "Missing connection to other component.")
