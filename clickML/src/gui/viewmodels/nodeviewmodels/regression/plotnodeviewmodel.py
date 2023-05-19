from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.text_processing.cd_generate_chars import GenerateCharsDescriptor
from common.models.component_descriptors.regression.rd_plot_ling_log import plotDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from varname import nameof

class PlotNodeViewModel(MLComponentNodeViewModel):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 input_dot_factory: InputDotViewModelFactoryBase):
        super().__init__(ml_component_descriptor)
        self.__input_dot_factory = input_dot_factory
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__plot_input = self.__input_dot_factory.create(self.component_id, self._descriptor.pre)
        self.__raw_input = self.__input_dot_factory.create(self.component_id, self._descriptor.pre_2)

    @property
    def title(self):
        return 'Plot'

    @property
    def plot_input(self):
        return self.__plot_input

    @property
    def raw_input(self):
        return self.__raw_input

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = plotDescriptor(self.component_id)
        descriptor.pre = self.__plot_input.predecessor_descriptor
        descriptor.pre_2 = self.__raw_input.predecessor_descriptor
        return descriptor