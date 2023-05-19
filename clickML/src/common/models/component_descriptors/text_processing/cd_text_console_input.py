import uuid

from backend.ml_components.text_processing.c_text_console_input import TextConsoleInput
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import SuccessorDescriptor


class TextConsoleInputDescriptor(MLComponentDescriptor):
    """
    Descriptor for TextConsoleInput component. Used to read text from console input.

    Attributes:
        # attributes for possible predecessors and successors
        suc: SuccessorDescriptor
            (optional) component which uses the text
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        # attributes for possible predecessors and successors
        self.suc: SuccessorDescriptor = SuccessorDescriptor("input_text")

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return TextConsoleInput.__name__

    def restore_component(self) -> TextConsoleInput:
        return TextConsoleInput(self)
