import uuid

from backend.ml_components.text_processing.c_letter_case import LetterCase
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor


class LetterCaseDescriptor(MLComponentDescriptor):
    """
    Descriptor for LetterCase component. Turns text into upper or lower case.

    Attributes:
        # attributes for possible predecessors and successors
        pre: PredecessorDescriptor
            (required) component which has as output a text
        suc: SuccessorDescriptor
            (optional) component that works on text

        # attributes for replacing
        case: str
            (required) upper or lower case
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        # attributes for possible predecessors and successors
        self.pre: PredecessorDescriptor = PredecessorDescriptor("text")
        self.suc: SuccessorDescriptor = SuccessorDescriptor("cased_text")

        # attributes for choosing case
        self.case: str = DEFAULT

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return LetterCase.__name__

    def restore_component(self) -> LetterCase:
        return LetterCase(self)
