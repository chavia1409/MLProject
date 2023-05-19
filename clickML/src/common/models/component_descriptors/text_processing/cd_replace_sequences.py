import uuid
from typing import Union

from backend.ml_components.text_processing.c_replace_sequences import ReplaceSequences
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor


class ReplaceSequencesDescriptor(MLComponentDescriptor):
    """
    Descriptor for ReplaceSequences component. Takes text and replaces chosen sequences.

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
            (required) list of sequences to replace sequence at same position in __sequences_original,
            should be list[str]
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        # attributes for possible predecessors and successors
        self.pre: PredecessorDescriptor = PredecessorDescriptor("text")
        self.suc: SuccessorDescriptor = SuccessorDescriptor("text")

        # attributes for replacing
        self.sequences_original: Union[list[str], str] = DEFAULT
        self.sequences_replace: Union[list[str], str] = DEFAULT

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return ReplaceSequences.__name__

    def restore_component(self) -> ReplaceSequences:
        return ReplaceSequences(self)
