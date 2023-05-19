import uuid

from backend.ml_components.regression.r_sparsify_log import Sparsify
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import SuccessorDescriptor, PredecessorDescriptor


class SparsifyDescriptor(MLComponentDescriptor):

    def __init__(self, component_id: uuid):
        self.__component_id = component_id

        self.pre = PredecessorDescriptor('Regression input')  # required
        self.suc = SuccessorDescriptor('Output')  # optional

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return Sparsify.__name__

    def restore_component(self) -> Sparsify:
        return Sparsify(self)