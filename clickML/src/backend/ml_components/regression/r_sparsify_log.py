# Collaborators: Julian Klitzke \\

from __future__ import annotations

import copy
from typing import TYPE_CHECKING, Any

from backend.component_enum import Components
from backend.ml_components.regression.rf_methods import r_methods
from backend.ml_components.ml_component import MLComponent
from common.models.pre_suc_descriptors import SuccessorDescriptor, PredecessorDescriptor
from common.exceptions.click_ml_exceptions import RequiredArgumentError, InternalError

if TYPE_CHECKING:
    from common.models.component_descriptors.regression.rd_sparsify_log import SparsifyDescriptor
    from backend.ml_components.regression.rf_helping_methods import HelpingMethods


# REACHED PRODUCTION STAGE
class Sparsify(MLComponent):

    def __init__(self, descriptor: SparsifyDescriptor):
        self.pre_input = None
        desc = copy.deepcopy(descriptor)
        super().__init__(desc.component_id)

        self.pre = desc.pre
        self.suc = desc.suc

        HelpingMethods.ComponentList.append(self.type())

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return [self.pre]

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return [self.suc]

    @property
    def values_for_successors(self) -> dict[str, Any]:
        return{self.suc.name: self.pre_input}

    def to_code(self) -> str:
        return r_methods.sparsify(self.pre_input, "X")

    def get_needed_imports(self) -> list[str]:
        return[]

    def check_if_valid(self) -> None:
        HelpingMethods.check_desc_reg_type_validity()
        if not HelpingMethods.check_constraint(self.pre_input):
            raise InternalError(f"{Sparsify.__name__}: missing regression model ")

    def do_preprocessing(self) -> None:
        self.pre_input = self.toolkit.get_data_from_predecessor(self.pre)

    def type(self) -> Components:
        return Components.SPARSIFY
