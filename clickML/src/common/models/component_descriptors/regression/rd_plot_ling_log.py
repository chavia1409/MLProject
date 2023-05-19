import uuid

from backend.ml_components.regression.r_plot_lin_log import Plotter
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import SuccessorDescriptor, PredecessorDescriptor
from common.models.component_descriptors.component_constants import DEFAULT


class plotDescriptor(MLComponentDescriptor):

    def __init__(self, component_id: uuid):
        self.__component_id = component_id

        self.pre = PredecessorDescriptor('Plot input')  # required - plot input
        self.pre_2 = PredecessorDescriptor('[Optional] Y value for raw csv-arrays')  # optional

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return Plotter.__name__

    def restore_component(self) -> Plotter:
        return Plotter(self)
