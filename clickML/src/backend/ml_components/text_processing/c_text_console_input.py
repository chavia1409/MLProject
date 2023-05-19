"""Module for TextConsoleInput component."""

from __future__ import annotations

import copy
from typing import TYPE_CHECKING

from backend.ml_components.ml_component import MLComponent
from common.models.pre_suc_descriptors import SuccessorDescriptor, PredecessorDescriptor
from backend.component_enum import Components

if TYPE_CHECKING:
    from common.models.component_descriptors.text_processing.cd_text_console_input import TextConsoleInputDescriptor


class TextConsoleInput(MLComponent):
    """
    Component that reads text from console.

    Attributes:

        # attributes for possible predecessors and successors
        suc: SuccessorDescriptor
            (optional) reference on following component the works on read text
    """

    def __init__(self, descriptor: TextConsoleInputDescriptor) -> None:
        des = copy.deepcopy(descriptor)
        super().__init__(des.component_id)

        # attributes for possible predecessors and successors
        self.suc: SuccessorDescriptor = des.suc

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return []

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return [self.suc]

    @property
    def values_for_successors(self) -> dict[str, str]:
        return {self.suc.name: "text"}

    def to_code(self) -> str:
        code = "# reading text from console input\n"\
               f"{self.values_for_successors[self.suc.name]} = input(" + repr("Put in text here:\n") + ")"
        return code

    def get_needed_imports(self) -> list[str]:
        return []

    def check_if_valid(self) -> None:
        pass

    def do_preprocessing(self) -> None:
        pass

    def type(self) -> Components:
        return Components.TEXT_CONSOLE_INPUT
