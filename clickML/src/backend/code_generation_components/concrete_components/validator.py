from __future__ import annotations

from typing import Callable, TYPE_CHECKING

from backend.code_generation_components.abstract_components.project_validator import ProjectValidator
from backend.code_generation_components.abstract_tools.project_general_validator import ProjectGeneralValidator
from backend.code_generation_components.abstract_tools.project_type_validator import ProjectTypeValidator
from backend.ml_components.ml_component import MLComponent

if TYPE_CHECKING:
    from backend.code_generation_components.abstract_tools.project_type_categorizer import ProjectTypeCategorizer
    from backend.component_enum import Categories


class Validator(ProjectValidator):
    """class for checking if project status is valid"""

    def __init__(self, general_validator: ProjectGeneralValidator, type_categorizer: ProjectTypeCategorizer,
                 type_validator_dict: dict[Categories, Callable[[], ProjectTypeValidator]]) -> None:
        self.__general_validator = general_validator
        self.__type_categorizer = type_categorizer
        self.__type_validator_dict = type_validator_dict

    def check_if_valid(self, components: list[MLComponent]) -> None:
        """does nothing if project model is valid, raises exception otherwise"""

        # checking general requirements
        self.__general_validator.check_if_valid(components)

        # computing category of the project (e.g. regression, image classification)
        project_category = self.__type_categorizer.get_category(components)

        # creating ProjectTypeValidator
        type_validator = self.__type_validator_dict[project_category]()

        # checking project category specific requirements
        type_validator.check_if_valid(components)
