"""Module for ReplaceSequences component."""
from __future__ import annotations

import copy
from typing import Union, TYPE_CHECKING

from common.exceptions.click_ml_exceptions \
    import SpecificationError, RequiredArgumentError, ComponentCompositionError
from backend.ml_components.ml_component import MLComponent
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from backend.ml_components.valid_connections import BASIC_TEXT_PREPROCESSING_CONNECTIONS
from backend.component_enum import Components

if TYPE_CHECKING:
    from common.models.component_descriptors.text_processing.cd_replace_sequences import ReplaceSequencesDescriptor


class ReplaceSequences(MLComponent):
    """
    Component that replaces free selectable symbols from the text.

    Attributes:
        # attributes for possible predecessors and successors
        pre: PredecessorDescriptor
            (required) component which has as output a text
        suc: SuccessorDescriptor
            (optional) component that works on replaced text

        # attributes for replacing
        sequences_original: Union[list[str], str]
            (required) list of sequences that have to be replaced, should be list[str]
        sequences_replace: Union[list[str], str]
            (required) list of sequences to replace sequence at same position in __sequences_original

        # preprocessing
        text: str
            name of the text variable where this component should work on
    """

    def __init__(self, descriptor: ReplaceSequencesDescriptor) -> None:
        des = copy.deepcopy(descriptor)
        super().__init__(des.component_id)

        # attributes for possible predecessors and successors
        self.pre: PredecessorDescriptor = des.pre
        self.suc: SuccessorDescriptor = des.suc

        # attributes for replacing
        self.sequences_original: Union[list[str], str] = des.sequences_original
        self.sequences_replace: Union[list[str], str] = des.sequences_replace

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
        if len(self.sequences_original) > 1:
            code = f"original = {self.sequences_original}\n" \
                   f"replace = {self.sequences_replace}\n" \
                   f"for seq_o, seq_r in zip(original, replace):\n" \
                   f"\t{self.values_for_successors[self.suc.name]} = {self.text}.replace(seq_o, seq_r)"
        else:
            code = f"{self.values_for_successors[self.suc.name]} = {self.text}.replace(" \
                   f"{repr(self.sequences_original[0])}, {repr(self.sequences_replace[0])})"
        return "# replacing sequences\n" + code

    def get_needed_imports(self) -> list[str]:
        return []

    def check_if_valid(self) -> None:
        self.__check_neighbors()
        self.__check_required_arguments()
        self.__check_domain_validity()
        self.__check_argument_composition()

    def __check_domain_validity(self) -> None:
        if isinstance(self.sequences_original, str) and self.sequences_original != DEFAULT:
            raise SpecificationError("sequences_original", self.sequences_original, ReplaceSequences.__name__,
                                     "Must be list with strings inside!")
        if not self.sequences_original:
            raise SpecificationError("sequences_original", self.sequences_original, ReplaceSequences.__name__,
                                     "Must have at least one sequence to replace!")
        if isinstance(self.sequences_replace, str) and self.sequences_replace != DEFAULT:
            raise SpecificationError("sequences_replace", self.sequences_replace, ReplaceSequences.__name__,
                                     "Must be list with strings inside!")
        if not self.sequences_original:
            raise SpecificationError("sequences_replace", self.sequences_original, ReplaceSequences.__name__,
                                     "Must have at least one sequence to replace!")

    def __check_required_arguments(self) -> None:
        # checking if required arguments are set
        if self.sequences_original == DEFAULT:
            raise RequiredArgumentError("sequences_original", "ReplaceSequences")
        if self.sequences_replace == DEFAULT:
            raise RequiredArgumentError("sequences_replace", "ReplaceSequences")

    def __check_argument_composition(self) -> None:
        # checking if composition of arguments is valid
        if len(self.sequences_original) != len(self.sequences_replace):
            raise ComponentCompositionError("ReplaceSequences", "Parameters 'sequences_original' and "
                                                                "'sequences_replace' must have the same length.")

    def __check_neighbors(self) -> None:
        self.toolkit.check_needed_predecessors([self.pre], ReplaceSequences.__name__)
        self.toolkit.check_pre_connection_validity(self.pre, BASIC_TEXT_PREPROCESSING_CONNECTIONS)

    def do_preprocessing(self) -> None:
        self.text = self.toolkit.get_data_from_predecessor(self.pre)

    def type(self) -> Components:
        return Components.REPLACE_SEQUENCES
