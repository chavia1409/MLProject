"""Module for LetterCase component."""

from __future__ import annotations

import copy
from typing import TYPE_CHECKING

from common.exceptions.click_ml_exceptions import SpecificationError, RequiredArgumentError
from backend.ml_components.ml_component import MLComponent
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from backend.ml_components.valid_connections import BASIC_TEXT_PREPROCESSING_CONNECTIONS
from backend.component_enum import Components

if TYPE_CHECKING:
    from common.models.component_descriptors.text_processing.cd_letter_case import LetterCaseDescriptor


class LetterCase(MLComponent):
    """
    Component that turns the text into lower or upper case.

    Attributes:
        # attributes for possible predecessors and successors
        pre: PredecessorDescriptor
            (required) component which has as output a text
        suc: SuccessorDescriptor
            (optional) component that works on resulting text

        # attributes for choosing the letter case
        case: str
            (required) must be in {'upper', 'lower'} to decide how text should be transformed

        # preprocessing
        text: str
            name of the text variable where this component should work on
    """

    def __init__(self, descriptor: LetterCaseDescriptor) -> None:
        des = copy.deepcopy(descriptor)
        super().__init__(des.component_id)

        # attributes for possible predecessors and successors
        self.pre: PredecessorDescriptor = des.pre
        self.suc: SuccessorDescriptor = des.suc

        # attributes for choosing case
        self.case: str = des.case.lower()

        # preprocessing
        self.text: str = DEFAULT

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return [self.pre]

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return [self.suc]

    @property
    def values_for_successors(self) -> dict[str, str]:
        return {self.suc.name: self.text}

    def to_code(self) -> str:
        return f"{self.values_for_successors[self.suc.name]} = {self.text}.{self.case}()"

    def get_needed_imports(self) -> list[str]:
        return []

    def check_if_valid(self) -> None:
        self.__check_neighbors()
        self.__check_required_arguments()
        self.__check_domain_validity()

    def __check_domain_validity(self) -> None:
        if self.case not in {DEFAULT, "upper", "lower"}:
            raise SpecificationError("case", self.case, LetterCase.__name__, "Only 'upper' and 'lower is valid!")

    def __check_required_arguments(self) -> None:
        # checking if required arguments are set
        if self.case == DEFAULT:
            raise RequiredArgumentError("case", LetterCase.__name__)

    def __check_neighbors(self) -> None:
        self.toolkit.check_needed_predecessors([self.pre], LetterCase.__name__)
        self.toolkit.check_pre_connection_validity(self.pre, BASIC_TEXT_PREPROCESSING_CONNECTIONS)

    def do_preprocessing(self) -> None:
        self.text = self.toolkit.get_data_from_predecessor(self.pre)

    def type(self) -> Components:
        return Components.LETTER_CASE
