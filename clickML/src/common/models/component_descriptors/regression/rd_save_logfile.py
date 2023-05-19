import uuid

from backend.ml_components.regression.rl_save_logfile import SaveLogfile
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import SuccessorDescriptor, PredecessorDescriptor
from common.models.component_descriptors.component_constants import DEFAULT


class SaveLogfileDescriptor(MLComponentDescriptor):

    def __init__(self, component_id: uuid):
        self.__component_id = component_id

        self.pre = PredecessorDescriptor("(Adapter) Input")  # required
        """ required - Module can be used in between regression by using the adapter module 
        beforehand or at the end of the regression"""

        self.filePath = DEFAULT  # required: file path to saving location

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return SaveLogfile.__name__

    def restore_component(self) -> SaveLogfile:
        return SaveLogfile(self)
