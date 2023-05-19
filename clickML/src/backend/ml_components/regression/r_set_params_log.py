# Collaborators: Julian Klitzke \\

from __future__ import annotations

import copy
from typing import TYPE_CHECKING, Any

from backend.component_enum import Components
from backend.ml_components.regression.rf_methods import r_methods
from backend.ml_components.ml_component import MLComponent
from common.models.pre_suc_descriptors import SuccessorDescriptor, PredecessorDescriptor
from common.exceptions.click_ml_exceptions import RequiredArgumentError

if TYPE_CHECKING:
    from common.models.component_descriptors.regression.rd_set_params_log import SetParamsDescriptor
    from backend.ml_components.regression.rf_helping_methods import HelpingMethods


class SetParams(MLComponent):

    def __init__(self, descriptor: SetParamsDescriptor):
        self.pre_input = None
        desc = copy.deepcopy(descriptor)
        super().__init__(desc.component_id)

        self.pre = desc.pre
        self.suc = desc.suc

        self.setterArgument = desc.setterArgument

        HelpingMethods.ComponentList.append(self.type())

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return [self.pre]

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return [self.suc]

    @property
    def values_for_successors(self) -> dict[str, Any]:
        return {self.suc.name: self.pre_input}  # TODO check wether any more values might be required

    def to_code(self) -> str:
        return r_methods.set

    def get_needed_imports(self) -> list[str]:
        return []

    def check_if_valid(self) -> None:
        self.desc_check()
        # TODO

    def do_preprocessing(self) -> None:
        self.pre_input = self.toolkit.get_data_from_predecessor(self.pre)

    # TODO
    def desc_check(self) -> bool:
        if HelpingMethods.check_desc_reg_type_validity():
            raise RequiredArgumentError.__init__("Fit Method", SetParams.__name__)

    def type(self) -> Components:
        """returns type from Components Enum"""
        pass
