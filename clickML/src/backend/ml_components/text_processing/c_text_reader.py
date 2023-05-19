"""Module for TextReader component."""

from __future__ import annotations

import codecs
import copy
import os
from typing import Union, Optional, TYPE_CHECKING

from common.exceptions.click_ml_exceptions import SpecificationError, RequiredArgumentError
from backend.ml_components.ml_component import MLComponent
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.pre_suc_descriptors import SuccessorDescriptor, PredecessorDescriptor
from backend.component_enum import Components

if TYPE_CHECKING:
    from common.models.component_descriptors.text_processing.cd_text_reader import TextReaderDescriptor


class TextReader(MLComponent):
    """
    Component that reads text from a given source file.

    Attributes:

        # attributes for possible predecessors and successors
        suc: SuccessorDescriptor
            (optional) reference on following component that works on read text

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

    def __init__(self, descriptor: TextReaderDescriptor) -> None:
        des = copy.deepcopy(descriptor)
        super().__init__(des.component_id)

        # attributes for possible predecessors and successors
        self.suc: SuccessorDescriptor = des.suc

        # parameters for open()
        self.file: str = des.file
        self.encoding: str = des.encoding
        self.errors: Optional[str] = des.errors
        self.newline: Optional[str] = des.newline

        # parameters for read()
        self.size: Union[int, str] = des.size

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return []

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return [self.suc]

    @property
    def values_for_successors(self) -> dict[str, str]:
        return {self.suc.name: "text"}

    @property
    def __parameters_open(self) -> str:
        param_dict = {"file": self.file, "encoding": self.encoding, "errors": self.errors, "newline": self.newline}
        return self.toolkit.create_param_string(param_dict)

    @property
    def __parameters_read(self) -> str:
        param_dict = {"size": self.size}
        return self.toolkit.create_param_string(param_dict)

    def to_code(self) -> str:
        code = "# reading text from source file\n"\
               f"with open({self.__parameters_open}) as file:\n" \
               f"\t{self.values_for_successors[self.suc.name]} = file.read({self.__parameters_read})"
        return code

    def get_needed_imports(self) -> list[str]:
        return []

    def check_if_valid(self) -> None:
        self.__check_required_arguments()
        self.__check_domain_validity()

    def __check_domain_validity(self) -> None:
        if self.file != DEFAULT and not(os.path.isfile(self.file) and self.file.endswith(".txt")):
            raise SpecificationError("file", self.file, TextReader.__name__, "Not an existing .txt file!")
        if not(self.encoding == DEFAULT or codecs.lookup(self.encoding)):
            raise SpecificationError("encoding", self.encoding, TextReader.__name__, "Not a valid encoding format!")
        if not(self.errors in {DEFAULT, None} or codecs.lookup_error(self.errors)):
            raise SpecificationError("errors", self.errors, TextReader.__name__, "Not a valid error handling!")
        if self.newline not in {DEFAULT, None, "", "\n", "\r", "\r\n"}:
            raise SpecificationError("newline", self.newline, TextReader.__name__, "Not a valid newlines mode!")
        if (isinstance(self.size, str) and self.size != DEFAULT) or (isinstance(self.size, int) and self.size < -1):
            raise SpecificationError("size", self.size, TextReader.__name__, "Not a valid size >= -1!")

    def __check_required_arguments(self) -> None:
        # checking if required arguments are set
        if self.file == DEFAULT:
            raise RequiredArgumentError("file", TextReader.__name__)

    def do_preprocessing(self) -> None:
        pass

    def type(self) -> Components:
        return Components.TEXT_READER
