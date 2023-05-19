from __future__ import annotations

import codecs
import copy
import os
from typing import Optional, TYPE_CHECKING

from common.exceptions.click_ml_exceptions import SpecificationError, RequiredArgumentError
from backend.ml_components.ml_component import MLComponent
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from backend.ml_components.valid_connections import BASIC_TEXT_PREPROCESSING_CONNECTIONS
from backend.component_enum import Components

if TYPE_CHECKING:
    from common.models.component_descriptors.text_processing.cd_save_text import SaveTextDescriptor


class SaveText(MLComponent):
    """
    Component that saves text to file.

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
            (optional) controls universal newline mode

        # preprocessing
        text: str
            name of the text variable where this component should work on
    """

    def __init__(self, descriptor: SaveTextDescriptor):
        des = copy.deepcopy(descriptor)
        super().__init__(des.component_id)

        # attributes for possible predecessors and successors
        self.pre: PredecessorDescriptor = des.pre
        self.suc: SuccessorDescriptor = des.suc

        # parameters for open()
        self.file: str = des.file
        self.encoding: str = des.encoding
        self.errors: Optional[str] = des.errors
        self.newline: Optional[str] = des.newline

        # preprocessing
        self.text: str = DEFAULT

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return [self.pre]

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return [self.suc]

    @property
    def values_for_successors(self) -> dict[str, str]:
        return {self.suc.name: self.text}

    @property
    def __parameters_open(self) -> str:
        param_dict = {"file": self.file, "mode": "w", "encoding": self.encoding, "errors": self.errors,
                      "newline": self.newline}
        return self.toolkit.create_param_string(param_dict)

    def to_code(self) -> str:
        code = f"# writes {self.text} to given source file\n"\
               f"with open({self.__parameters_open}) as file:\n" \
               f"\tfile.write({self.text})"
        return code

    def get_needed_imports(self) -> list[str]:
        return []

    def check_if_valid(self) -> None:
        self.__check_neighbors()
        self.__check_required_arguments()
        self.__check_domain_validity()

    def __check_domain_validity(self) -> None:
        if self.file != DEFAULT and not(os.path.isdir(os.path.dirname(self.file)) and self.file.endswith(".txt")):
            raise SpecificationError("file", self.file, SaveText.__name__, "Not a .txt file in existing directory!")
        if not(self.encoding == DEFAULT or codecs.lookup(self.encoding)):
            raise SpecificationError("encoding", self.encoding, SaveText.__name__, "Not a valid encoding format!")
        if not(self.errors in {DEFAULT, None} or codecs.lookup_error(self.errors)):
            raise SpecificationError("errors", self.errors, SaveText.__name__, "Not a valid error handling!")
        if self.newline not in {DEFAULT, None, "", "\n", "\r", "\r\n"}:
            raise SpecificationError("newline", self.newline, SaveText.__name__, "Not a valid newlines mode!")

    def __check_required_arguments(self) -> None:
        if self.file == DEFAULT:
            raise RequiredArgumentError("file", SaveText.__name__)

    def __check_neighbors(self) -> None:
        self.toolkit.check_needed_predecessors([self.pre], SaveText.__name__)
        self.toolkit.check_pre_connection_validity(self.pre, BASIC_TEXT_PREPROCESSING_CONNECTIONS)

    def do_preprocessing(self) -> None:
        self.text = self.toolkit.get_data_from_predecessor(self.pre)

    def type(self) -> Components:
        return Components.SAVE_TEXT
