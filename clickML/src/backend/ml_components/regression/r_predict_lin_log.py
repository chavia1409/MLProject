# Collaborators: Julian Klitzke \\

from __future__ import annotations

import copy
from typing import TYPE_CHECKING

from backend.component_enum import Components
from common.models.component_descriptors.component_constants import DEFAULT
from backend.ml_components.regression.rf_methods import r_methods
from common.exceptions.click_ml_exceptions import SpecificationError
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from backend.ml_components.ml_component import MLComponent
from enum import Enum

if TYPE_CHECKING:
    from common.models.component_descriptors.regression.rd_predict_lin_log import PredictDescriptor
    from backend.ml_components.regression.rf_helping_methods import HelpingMethods


# REACHED PRODUCTION STAGE
class Predict(MLComponent):

    def type(self) -> Components:
        return Components.PREDICT_LIN_LOG

    def __init__(self, descriptor: PredictDescriptor) -> None:
        self.pre_input = None

        desc = copy.deepcopy(descriptor)
        super().__init__(desc.component_id)

        self.pre = desc.pre
        self.suc = desc.suc

        self.from_column = desc.from_column
        self.to_column = desc.to_column
        self.from_row = desc.from_row
        self.to_row = desc.to_row
        self.prediction_type = desc.prediction_type

        self.lin_log: str = DEFAULT  # TODO
        self.constraint = f"pdt_{HelpingMethods.check_return_use_validity(Components.PREDICT_LIN_LOG)}"

        HelpingMethods.ConstraintList.append(self.constraint)
        HelpingMethods.ComponentList.append(self.type())

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return [self.pre]

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return [self.suc]

    @property
    def values_for_successors(self) -> dict[str, str]:
        return {self.suc.name: self.lin_log}

    def to_code(self) -> str:
        return self.get_prediction_type()

    def get_needed_imports(self) -> list[str]:
        return []

    def check_if_valid(self) -> None:
        self.constraint_check()
        HelpingMethods.check_desc_reg_type_validity()
        HelpingMethods.check_constraint(self.pre_input)

    def do_preprocessing(self) -> None:
        self.pre_input: list[str] = self.toolkit.get_data_from_predecessor(self.pre)

        self.pre_input.pop()

    def get_prediction_type(self) -> str:

        if self.lin_log == "predict_log" & self.prediction_type == pred_type.pred_proba:
            return r_methods.predict_proba(self.constraint, self.pre_input, "X")

        if self.lin_log == "predict_log" & self.prediction_type == pred_type.pred_log_proba:
            return r_methods.predict_log_proba(self.constraint, self.pre_input, "X")

        return r_methods.predict(self.constraint, self.pre_input, "X")

    def constraint_check(self) -> None:
        if not (isinstance(self.prediction_type, pred_type)):
            raise SpecificationError("prediction_type", self.prediction_type, PredictDescriptor.__name__,
                                     "is not a valid prediction type")
        if not (isinstance((self.from_row, self.to_row, self.from_column, self.to_column),
                           str)) and self.from_row < self.to_row and self.from_column < self.to_column:
            raise SpecificationError("Predict values", [self.from_row, self.to_row, self.from_column, self.to_column],
                                     Predict.__name__, "Values are not valid")


class pred_type(Enum):
    pred = "predict"
    pred_proba = "predict_proba"
    pred_log_proba = "predict_log_proba"
