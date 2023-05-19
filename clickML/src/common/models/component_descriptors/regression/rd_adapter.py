import uuid

from backend.ml_components.regression.r_adapter import adapter
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import SuccessorDescriptor, PredecessorDescriptor


class adapterDescriptor(MLComponentDescriptor):
    """
    Explanation: This gives the user kind of a "multi plug", making 2 data outputs out of 1 output
    of any module
    """

    def __init__(self, component_id: uuid):
        self.__component_id = component_id

        self.pre = PredecessorDescriptor('Regression module input')  # required
        self.suc = SuccessorDescriptor('Output 1')  # required
        self.suc_2 = SuccessorDescriptor('Output 2')  # required

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return adapter.component_type()

    def restore_component(self) -> adapter:
        return adapter(self)
