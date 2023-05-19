import uuid
from typing import Union

from backend.ml_components.text_processing.c_delete_sequences import DeleteSequences
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor


class DeleteSequencesDescriptor(MLComponentDescriptor):
    """
    Descriptor for DeleteSequences component.

    Attributes:
        # attributes for possible predecessors and successors
        pre: PredecessorDescriptor
            (required) component which has as output a text
        suc: SuccessorDescriptor
            (optional) component that works on text

        # attributes for replacing
        sequences: Union[list[str], str]
            (required) list of sequences that have to be deleted, should be list[str]
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        # attributes for possible predecessors and successors
        self.pre: PredecessorDescriptor = PredecessorDescriptor("text")
        self.suc: SuccessorDescriptor = SuccessorDescriptor("deleted_text")

        # attributes for replacing
        self.sequences: Union[list[str], str] = DEFAULT

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return DeleteSequences.__name__

    def restore_component(self) -> DeleteSequences:
        return DeleteSequences(self)
