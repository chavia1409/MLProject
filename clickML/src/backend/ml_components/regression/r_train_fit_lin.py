# Collaborators: Julian Klitzke \\

from __future__ import annotations

import copy
from typing import TYPE_CHECKING, Any

from backend.component_enum import Components
from backend.ml_components.ml_component import MLComponent
from backend.ml_components.regression.rf_methods import r_methods
from common.exceptions.click_ml_exceptions import SpecificationError, ComponentCompositionError
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor

if TYPE_CHECKING:
    from common.models.component_descriptors.regression.rd_train_fit_lin import Train_Fit_Lin_Descriptor
    from backend.ml_components.regression.rf_helping_methods import HelpingMethods


# REACHED PRODUCTION STAGE
class Train_Fit_Linear(MLComponent):

    def __init__(self, descriptor: Train_Fit_Lin_Descriptor) -> None:
        desc = copy.deepcopy(descriptor)
        super().__init__(desc.component_id)

        self.pre = desc.pre
        self.pre_2 = desc.pre_2
        self.suc = desc.suc
        self.suc_2 = desc.suc_2
        self.suc_3 = desc.suc_3

        self.test_size = desc.test_size
        self.train_size = desc.train_size
        self.random = desc.random
        self.shuffle = desc.shuffle

        self.X_Plot_value = desc.X_Plot_value
        self.Y_Plot_value = desc.Y_Plot_value

        self.preData = None
        self.pre_2Data = None

        self.regression_model = "lg_" + HelpingMethods.check_return_use_validity(Train_Fit_Linear.type())

        HelpingMethods.ComponentList.append(self.type())  # saves component call in list for later validation
        HelpingMethods.ConstraintList.append(self.regression_model)  # saves trained model to list for validation

    def get_needed_imports(self) -> list[str]:
        return HelpingMethods.get_needed_imports("linear")

    def to_code(self) -> str:
        code = "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=" + self.test_size + ",train_size=" \
               + self.train_size + ",random_state=" + self.random + ", shuffle=" + self.shuffle + ") \n"

        code += r_methods.fit(self.regression_model, self.X_Plot_value, self.Y_Plot_value) + "\n"

        return code

    # TODO
    def check_if_valid(self) -> None:
        self.attribute_validity_check()

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return [self.pre, self.pre_2]

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return [self.suc, self.suc_2, self.suc_3]

    def values_for_successors(self) -> dict[str, Any]:
        return {self.suc.name: list[self.type, self.regression_model],
                self.suc_2.name: list[self.regression_model],
                self.suc_3.name: list[self.type(), self.X_Plot_value, self.Y_Plot_value, self.regression_model]}

    def do_preprocessing(self) -> None:
        self.preData = self.toolkit.get_data_from_predecessor(self.pre)
        self.pre_2Data = self.toolkit.get_data_from_predecessor(self.pre_2)

    def attribute_validity_check(self) -> None:
        if not 0.1 <= self.test_size <= 1.0:
            raise SpecificationError("test_size", self.test_size, Train_Fit_Linear.__name__,
                                     "Value must be between 0.1 and 1.0")
        if not 0.1 <= self.train_size <= 1.0:
            raise SpecificationError("train_size", self.train_size, Train_Fit_Linear.__name__,
                                     "Value must be between 0.1 and 1.0")
        if self.test_size + self.train_size != 1.0:
            raise ComponentCompositionError(Train_Fit_Linear.__name__,
                                            "Train and Test value size does not add up to 100%")
        if not (isinstance(self.Y_Plot_value, str)):
            raise SpecificationError("Y_Plot_value", self.Y_Plot_value, Train_Fit_Linear.__name__,
                                     "Must be a String type")
        if not (isinstance(self.X_Plot_value, str)):
            raise SpecificationError("X_Plot_value", self.X_Plot_value, Train_Fit_Linear.__name__,
                                     "Must be a String type")

    def type(self) -> Components:
        return Components.TRAIN_FIT_LINEAR
