import uuid
from typing import Union

from backend.ml_components.text_processing.c_divide_chars_by_sentences import DivideCharsBySentences
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor


class DivideCharsBySentencesDescriptor(MLComponentDescriptor):
    """
    Descriptor for DivideCharsBySentences component.

    Attributes:
        # attributes for possible predecessors and successors
        pre: PredecessorDescriptor
            (required) component which has as output a text
        suc: SuccessorDescriptor
            (optional) component that works on single net input for prediction
        suc_2: SuccessorDescriptor
            (optional) component that works on net input data
        suc_3: SuccessorDescriptor
            (optional) component that works on desired net output data
        suc_4: SuccessorDescriptor
            (optional) component that needs net input shape
        suc_5: SuccessorDescriptor
            (optional) component that needs net output shape

        # options
        max_seq_length: Union[int, str]
            (optional) number of characters in each sequence, should be int
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        # attributes for possible predecessors and successors
        self.pre: PredecessorDescriptor = PredecessorDescriptor("input_text")
        self.suc: SuccessorDescriptor = SuccessorDescriptor("prediction_input")
        self.suc_2: SuccessorDescriptor = SuccessorDescriptor("net_input")
        self.suc_3: SuccessorDescriptor = SuccessorDescriptor("net_output")
        self.suc_4: SuccessorDescriptor = SuccessorDescriptor("input_shape")
        self.suc_5: SuccessorDescriptor = SuccessorDescriptor("output_shape")

        self.max_seq_length: Union[int, str] = DEFAULT

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return DivideCharsBySentences.__name__

    def restore_component(self) -> DivideCharsBySentences:
        return DivideCharsBySentences(self)
