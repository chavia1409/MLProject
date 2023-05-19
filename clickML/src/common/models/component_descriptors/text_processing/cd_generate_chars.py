import uuid
from typing import Union

from backend.ml_components.text_processing.c_generate_chars import GenerateChars
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor


class GenerateCharsDescriptor(MLComponentDescriptor):
    """
    Descriptor for GenerateChars component.

    Attributes:
        # attributes for possible predecessors and successors
        pre: PredecessorDescriptor
            (required) component that provides model for text generation
        pre_2: PredecessorDescriptor
            (required) component that provides the initialization input for text generation
        suc: SuccessorDescriptor
            (optional) component that works on new generated text

        init_chars_mode: str
            (required) first net input to init text generation, should be 'first', 'last' or 'random';
                only words from text on which net ist trained are valid
        number_of_chars: Union[int, str]
            (required) len of the generated text measured in amount of chars (excluding init_chars), should be int
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        # attributes for possible predecessors and successors
        self.pre: PredecessorDescriptor = PredecessorDescriptor("model")
        self.pre_2: PredecessorDescriptor = PredecessorDescriptor("init_chars")
        self.suc: SuccessorDescriptor = SuccessorDescriptor("generated_text")

        self.init_chars_mode: str = DEFAULT
        self.number_of_chars: Union[int, str] = DEFAULT

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return GenerateChars.__name__

    def restore_component(self) -> GenerateChars:
        return GenerateChars(self)
