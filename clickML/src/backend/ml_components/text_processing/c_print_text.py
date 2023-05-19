from __future__ import annotations

import copy
from typing import Union, TYPE_CHECKING

from common.exceptions.click_ml_exceptions import SpecificationError
from backend.ml_components.ml_component import MLComponent
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from backend.ml_components.valid_connections import BASIC_TEXT_PREPROCESSING_CONNECTIONS
from backend.component_enum import Components

if TYPE_CHECKING:
    from common.models.component_descriptors.text_processing.cd_print_text import PrintTextDescriptor


class PrintText(MLComponent):
    """
    Component that replaces free selectable symbols from the text.

    Attributes:
        # attributes for possible predecessors and successors
        pre: PredecessorDescriptor
            (required) component which has as output a text
        suc: SuccessorDescriptor
            (optional) component that works on text

        # options what to print
        number_of_chars: Union[int, str]
            (optional) number of chars to print out, starting from beginning (if not specified the complete
            text will be printed), should be int

        # preprocessing
        text: str
            name of the text variable where this component should work on
    """

    def __init__(self, descriptor: PrintTextDescriptor) -> None:
        des = copy.deepcopy(descriptor)
        super().__init__(des.component_id)

        # attributes for possible predecessors and successors
        self.pre: PredecessorDescriptor = des.pre
        self.suc: SuccessorDescriptor = des.suc

        # options what to print
        self.number_of_chars: Union[int, str] = des.number_of_chars

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
        if self.number_of_chars == DEFAULT:
            return f'print({self.text})'
        else:
            return f'print({self.text}[:{self.number_of_chars}])'

    def get_needed_imports(self) -> list[str]:
        return []

    def check_if_valid(self) -> None:
        self.__check_neighbors()
        self.__check_domain_validity()

    def __check_domain_validity(self) -> None:
        if ((isinstance(self.number_of_chars, str) and self.number_of_chars != DEFAULT) or
                (isinstance(self.number_of_chars, int) and self.number_of_chars <= 0)):
            raise SpecificationError("number_of_chars", self.number_of_chars, PrintText.__name__,
                                     "'number_of_chars' must be int > 0!")

    def __check_neighbors(self) -> None:
        self.toolkit.check_needed_predecessors([self.pre], PrintText.__name__)
        self.toolkit.check_pre_connection_validity(self.pre, BASIC_TEXT_PREPROCESSING_CONNECTIONS)

    def do_preprocessing(self) -> None:
        self.text = self.toolkit.get_data_from_predecessor(self.pre)

    def type(self) -> Components:
        return Components.PRINT_TEXT
