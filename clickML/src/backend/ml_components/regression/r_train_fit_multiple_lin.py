from typing import Union, TYPE_CHECKING, Any
import copy
from backend.ml_components.ml_component import MLComponent
from backend.component_enum import Components
from backend.ml_components.regression.rf_methods import r_methods
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor

if TYPE_CHECKING:
    from common.models.component_descriptors.regression.rd_train_multiple_linear_model import \
        TrainMultipleLinearRegressionDescriptor
    from backend.ml_components.regression.rf_helping_methods import HelpingMethods


class Train_Fit_Multiple_Linear(MLComponent):
    def __init__(self, descriptor: TrainMultipleLinearRegressionDescriptor) -> None:
        desc = copy.deepcopy(descriptor)
        super().__init__(desc.component_id)

        self.pre = desc.pre
        self.pre_2 = desc.pre_2
        self.suc = desc.suc
        self.suc_2 = desc.suc_2
        self.suc_3 = desc.suc_3

        self.independentValues = desc.independentValues
        self.dependentValue = desc.dependentValue
        self.test_size = desc.test_size
        self.train_size = desc.train_size
        self.random = desc.random

    def get_needed_imports(self) -> list[str]:
        return HelpingMethods.get_needed_imports("linear")

    def to_code(self) -> str:
        code = ""
        code += "X = csvName[" + self.dependentValue + "] \n"
        code += "Y = csvName[" + self.independentValues + "] \n"
        code += "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=" + self.test_size + ",train_size=" \
                + self.train_size + ",random_state=" + self.random + ") \n"
        code += r_methods.fit("lg", "X_train", "y_train") + "\n"

        return code

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return [self.pre, self.pre_2]

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return [self.suc, self.suc_2, self.suc_3]

    def type(self) -> Components:
        return Components.TRAIN_FIT_MULTIPLE_LINEAR

    def do_preprocessing(self) -> None:
        pass

    def check_if_valid(self) -> None:
        pass

    def values_for_successors(self) -> dict[str, Any]:
        pass
