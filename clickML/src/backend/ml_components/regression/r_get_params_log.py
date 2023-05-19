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
    from common.models.component_descriptors.regression.rd_get_params_log import GetParamsDescriptor
    from backend.ml_components.regression.rf_helping_methods import HelpingMethods
    from backend.ml_components.regression.rl_save_logfile import SaveLogfile


# REACHED PRODUCTION STAGE
class GetParams(MLComponent):

    def type(self) -> Components:
        return Components.GET_PARAMS_LOG

    def __init__(self, descriptor: GetParamsDescriptor):
        self.pre_input = None
        desc = copy.deepcopy(descriptor)
        super().__init__(desc.component_id)

        self.pre = desc.pre
        self.suc = desc.suc

        self.deep = desc.deep

        HelpingMethods.ComponentList.append(self.type())

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return [self.pre]

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return [self.suc]

    @property
    def values_for_successors(self) -> dict[str, Any]:
        return {self.suc.input: self.pre_input}

    def to_code(self) -> str:
        code = "get_params = " + r_methods.get_params(self.pre_input, self.deep)
        code += "print(get_params)"

        SaveLogfile.logfile.append(code)

        return code

    def get_needed_imports(self) -> list[str]:
        return []

    def check_if_valid(self) -> None:
        HelpingMethods.check_desc_reg_type_validity_log()
        HelpingMethods.check_constraint(self.pre_input)

    def do_preprocessing(self) -> None:
        self.pre_input = self.toolkit.get_data_from_predecessor(self.pre)
