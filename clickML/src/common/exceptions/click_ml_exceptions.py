"""Collection of exceptions for clickML project"""

from typing import Any


class ProjectCompositionError(Exception):
    """
    Exception for invalid sequence of MLComponents in ClickMLProjectModel.

    Attributes:
        __message: str
            Description why this composition is invalid.
    """
    def __init__(self, message: str) -> None:
        self.__message = message

    def __str__(self) -> str:
        return f"Composition of components not valid: {self.__message}"


class ComponentCompositionError(Exception):
    """
    Exception for invalid composition of parameters within a MLComponent or MLLayerComponent.

    Attributes:
        __component_name: str
            Name of the component with invalid composition.
        __message: str
            Description why this composition is invalid.
    """
    def __init__(self, component_name: str, message: str) -> None:
        self.__component_name = component_name
        self.__message = message

    def __str__(self) -> str:
        return f"Wrong composition in '{self.__component_name}' component: {self.__message}"


class SpecificationError(Exception):
    """
    Exception for invalid specification of MLComponent, MLLayerComponent and ClickMLProjectModel properties.

    Attributes:
        __param_name: str
            Name of the component parameter which is wrong specified.
        __param_value: Any
            (Invalid!) Value of __param_name.
        __component_name: str
            Name of the component in which __param_name is located.
        __message: str
            Description of the SpecificationError.
    """
    def __init__(self, param_name: str, param_value: Any, component_name: str, message: str = "") -> None:
        self.__param_name = param_name
        self.__param_value = param_value
        self.__component_name = component_name
        self.__message = message

    def __str__(self) -> str:
        error_message = f"'{self.__param_name} = {str(self.__param_value)}' is not valid for '{self.__component_name}'."
        if self.__message:
            error_message += f" {self.__message}"
        return error_message


class RequiredArgumentError(Exception):
    """
    Exception for missing specification of MLComponent, MLLayerComponent and ClickMLProjectModel properties.

    Attributes:
        __param_name: str
            Name of the component parameter which should be specified but is not.
        __component_name: str
            Name of the component in which __param_name is located.
    """
    def __init__(self, param_name: str, component_name: str) -> None:
        self.__param_name = param_name
        self.__component_name = component_name

    def __str__(self) -> str:
        return f"Parameter '{self.__param_name}' is required for '{self.__component_name}'."


class ComponentConnectionError(Exception):
    """
    Exception for wrong connected MLComponents in Flowchart.

    Attributes:
        __component_name: str
            Name of the component where the Error occurs.
        __port_name: str
            Name of the port where Error occurs.
        __message: str
            Explanation of the Error.
    """

    def __init__(self, component_name: str, port_name: str, message: str = "") -> None:
        self.__component_name = component_name
        self.__port_name = port_name
        self.__message = message

    def __str__(self) -> str:
        return f"Wrong connection of component {self.__component_name} at connector {self.__port_name}. {self.__message}"


class InternalError(Exception):
    """
    General exception for invalid ClickMLProjectModels without knowledge about the problem.

    Attributes:
        __message: str
            Error description (if possible)
    """

    def __init__(self, message: str = "") -> None:
        self.__message = message

    def __str__(self) -> str:
        error_message = "Something unexpected went wrong with this project."
        if self.__message:
            error_message = self.__message
        return error_message
