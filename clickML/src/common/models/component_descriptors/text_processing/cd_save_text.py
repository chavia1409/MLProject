import uuid
from typing import Optional

from backend.ml_components.text_processing.c_save_text import SaveText
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor


class SaveTextDescriptor(MLComponentDescriptor):
    """
    Descriptor for SaveText component. Takes text and writes it to file.

    Attributes:
        # attributes for possible predecessors and successors
        pre: PredecessorDescriptor
            (required) component which has as output a text
        suc: SuccessorDescriptor
            (optional) component that works on text

        # parameters for open()
        file: str
            (required) file path where to write text
        encoding: str
            (optional) used encoding
        errors: Optional[str]
            (optional) error handling
        newline: Optional[str]
            (optional) controls newline mode
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        # attributes for possible predecessors and successors
        self.pre: PredecessorDescriptor = PredecessorDescriptor("text")
        self.suc: SuccessorDescriptor = SuccessorDescriptor("text")

        # parameters for open()
        self.file: str = DEFAULT
        self.encoding: str = DEFAULT
        self.errors: Optional[str] = DEFAULT
        self.newline: Optional[str] = DEFAULT

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return SaveText.__name__

    def restore_component(self) -> SaveText:
        return SaveText(self)
