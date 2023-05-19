import uuid

from backend.ml_components.regression.r_get_params_log import GetParams
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import SuccessorDescriptor, PredecessorDescriptor


class GetParamsDescriptor(MLComponentDescriptor):

    def __init__(self, component_id: uuid):
        self.__component_id = component_id

        self.pre = PredecessorDescriptor('Regression input')  # required
        self.suc = SuccessorDescriptor('Output')  # optional

        self.deep = True  # optional, maybe build as an 'opt-out' functionality (Default: True)

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return GetParams.__name__

    def restore_component(self) -> GetParams:
        return GetParams(self)
