import uuid
from typing import Union

from backend.ml_components.text_processing.c_print_text import PrintText
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor


class PrintTextDescriptor(MLComponentDescriptor):
    """
    Descriptor for PrintText component. Takes text and prints it to console.

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
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        # attributes for possible predecessors and successors
        self.pre: PredecessorDescriptor = PredecessorDescriptor("text")
        self.suc: SuccessorDescriptor = SuccessorDescriptor("text")

        # attributes for replacing
        self.number_of_chars: Union[int, str] = DEFAULT

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return PrintText.__name__

    def restore_component(self) -> PrintText:
        return PrintText(self)
