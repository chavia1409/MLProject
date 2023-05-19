# Collaborators: Julian Klitzke \\

from __future__ import annotations

import copy
from typing import TYPE_CHECKING, Any

from backend.component_enum import Components
from backend.ml_components.ml_component import MLComponent
from common.models.pre_suc_descriptors import SuccessorDescriptor, PredecessorDescriptor
from common.exceptions.click_ml_exceptions import RequiredArgumentError

if TYPE_CHECKING:
    from common.models.component_descriptors.regression.rd_decision_function_log import DecisionFunctionDescriptor
    from backend.code_generation_components.concrete_tools.regression_type_validator import HelpingMethods
    from backend.ml_components.regression.rl_save_logfile import SaveLogfile


class DecisionFunction(MLComponent):

    def __init__(self, descriptor: DecisionFunctionDescriptor) -> None:
        desc = copy.deepcopy(descriptor)
        super().__init__(desc.component_id)

        self.pre = desc.pre
        self.suc = desc.suc

        self.print = desc.print
        self.pre_input = None

        HelpingMethods.ComponentList.append(self.type())

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return[self.pre]

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return[self.suc]

    @property
    def values_for_successors(self) -> dict[str, Any]:
        return{self.suc.name: self.pre_input}

    def to_code(self) -> str:
        pass

    def get_needed_imports(self) -> list[str]:
        return[]

    def check_if_valid(self) -> None:
        self.pred_check()

    def do_preprocessing(self) -> None:
        self.pre_input = self.toolkit.get_data_from_predecessor(self.pre)

    def pred_check(self):
        if HelpingMethods.check_desc_reg_type_validity():
            raise RequiredArgumentError("Fit Method", DecisionFunction.__name__)

        # TODO

    def type(self) -> Components:
        return Components.DECISION_FUNCTION_LOG


