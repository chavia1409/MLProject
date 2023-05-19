import uuid

from backend.ml_components.regression.r_decision_function_log import DecisionFunction
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import SuccessorDescriptor, PredecessorDescriptor


class DecisionFunctionDescriptor(MLComponentDescriptor):

    def __init__(self, component_id: uuid):
        self.__component_id = component_id

        self.pre = PredecessorDescriptor('Regression Input')  # required
        self.suc = SuccessorDescriptor('Output')  # optional

        self.print: bool = False  # optional

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return DecisionFunction.__name__

    def restore_component(self) -> DecisionFunction:
        return DecisionFunction(self)
