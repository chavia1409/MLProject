import uuid

from backend.ml_components.regression.r_set_params_log import SetParams
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import SuccessorDescriptor, PredecessorDescriptor
from common.models.component_descriptors.component_constants import DEFAULT


class SetParamsDescriptor(MLComponentDescriptor):

    def __init__(self, component_id: uuid):
        self.__component_id = component_id

        self.pre = PredecessorDescriptor('Regression input')  # required
        self.suc = SuccessorDescriptor('Output')  # optional

        self.setterArgument: str = DEFAULT  # optional, maybe build as an 'opt-out' functionality (Default: True)

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return SetParams.__name__

    def restore_component(self) -> SetParams:
        return SetParams(self)