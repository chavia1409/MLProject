from __future__ import annotations

import copy
from typing import TYPE_CHECKING, Any

from backend.component_enum import Components
from backend.ml_components.ml_component import MLComponent
from common.models.pre_suc_descriptors import SuccessorDescriptor, PredecessorDescriptor

if TYPE_CHECKING:
    from common.models.component_descriptors.regression.rd_adapter import adapterDescriptor
    from backend.ml_components.regression.rf_helping_methods import HelpingMethods


# ENTERED FINAL STAGE
class adapter(MLComponent):

    def __init__(self, descriptor: adapterDescriptor):
        self.pre_input = None
        desc = copy.deepcopy(descriptor)
        super().__init__(desc.component_id)

        self.pre = desc.pre
        self.suc = desc.suc
        self.suc_2 = desc.suc_2

        self.name = self.pre.name_prev

        HelpingMethods.ComponentList.append(self.type())

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return [self.pre]

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return [self.suc, self.suc_2]

    @property
    def values_for_successors(self) -> dict[str, Any]:
        return {self.suc.input: self.pre_input, self.suc_2.input: self.pre_input}

    # TODO: to_code for adapter
    def to_code(self) -> str:
        return ""

    def get_needed_imports(self) -> list[str]:
        return []  # no additional imports required

    def check_if_valid(self) -> None:
        self.pred_check()

    def do_preprocessing(self) -> None:
        self.pre_input = self.toolkit.get_data_from_predecessor(self.pre)

    def pred_check(self) -> None:
        None
        # Not required, as will be done in any connected module that is not an adapter

    def type(self) -> Components:
        return Components.ADAPTER

    @staticmethod
    def component_type():
        return adapter.name
