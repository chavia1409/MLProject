"""Module for DeleteSequences component."""

from __future__ import annotations

import copy
from typing import Union, TYPE_CHECKING

from common.exceptions.click_ml_exceptions import SpecificationError, RequiredArgumentError
from backend.ml_components.ml_component import MLComponent
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from backend.ml_components.valid_connections import BASIC_TEXT_PREPROCESSING_CONNECTIONS
from backend.component_enum import Components

if TYPE_CHECKING:
    from common.models.component_descriptors.text_processing.cd_delete_sequences import DeleteSequencesDescriptor


class DeleteSequences(MLComponent):
    """
    Component that deletes free selectable sequences from the text.

    Attributes:
        # attributes for possible predecessors and successors
        pre: PredecessorDescriptor
            component which has as output a text
        suc: SuccessorDescriptor
            component that works on text

        # attributes for deletion
        sequences: Union[list[str], str]
            (required) list of sequences that have to be deleted, should be list[str]

        # preprocessing
        text: str
            name of the text variable where this component should work on
    """

    def __init__(self, descriptor: DeleteSequencesDescriptor) -> None:
        des = copy.deepcopy(descriptor)
        super().__init__(des.component_id)

        # attributes for possible predecessors and successors
        self.pre: PredecessorDescriptor = des.pre
        self.suc: SuccessorDescriptor = des.suc

        # sequences that have to be deleted
        self.sequences: Union[list[str], str] = des.sequences

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
        if len(self.sequences) > 1:
            code = f"for seq in {self.sequences}:\n"\
                   f"\t{self.text} = {self.text}.replace(seq, '')\n"
        else:
            code = f"{self.text} = {self.text}.replace({repr(self.sequences[0])}, '')"
        return "# delete sequences from text \n" + code

    def get_needed_imports(self) -> list[str]:
        return []

    def check_if_valid(self) -> None:
        self.__check_neighbors()
        self.__check_required_arguments()
        self.__check_domain_validity()

    def __check_domain_validity(self) -> None:
        if isinstance(self.sequences, str) and self.sequences != DEFAULT:
            raise SpecificationError("sequences", self.sequences, DeleteSequences.__name__,
                                     "Must be list with strings inside!")

    def __check_required_arguments(self) -> None:
        if self.sequences == DEFAULT:
            raise RequiredArgumentError("sequences", DeleteSequences.__name__)

    def __check_neighbors(self) -> None:
        self.toolkit.check_needed_predecessors([self.pre], DeleteSequences.__name__)
        self.toolkit.check_pre_connection_validity(self.pre, BASIC_TEXT_PREPROCESSING_CONNECTIONS)

    def do_preprocessing(self) -> None:
        self.text = self.toolkit.get_data_from_predecessor(self.pre)

    def type(self) -> Components:
        return Components.DELETE_SEQUENCES
