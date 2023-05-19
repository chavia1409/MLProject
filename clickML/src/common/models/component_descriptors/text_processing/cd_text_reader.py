import uuid
from dataclasses import dataclass
from typing import Optional, Union

from backend.ml_components.text_processing.c_text_reader import TextReader
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import SuccessorDescriptor


@dataclass
class TextReaderDescriptor(MLComponentDescriptor):
    """
    Descriptor for TextReader component. Used to read text from given .txt file.

    Attributes:

        # attributes for possible predecessors and successors
        suc: SuccessorDescriptor
            (optional) component which uses the text

        # parameters for open():
        file: str
            (required) path and name of the file
        encoding: str
            (optional) encoding format
        errors: Optional[str]
            (optional) handling of decoding errors
        newline: Optional[str]
            (optional) controls universal newlines mode

        # parameters for read()
        size: Union[int, str]
            (optional) number of bytes to return, should be int
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        # attributes for possible predecessors and successors
        self.suc: SuccessorDescriptor = SuccessorDescriptor("input_text")

        # parameters for open()
        self.file: str = DEFAULT
        self.encoding: str = DEFAULT
        self.errors: Optional[str] = DEFAULT
        self.newline: Optional[str] = DEFAULT

        # parameters for read()
        self.size: Union[int, str] = DEFAULT

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return TextReader.__name__

    def restore_component(self) -> TextReader:
        return TextReader(self)
