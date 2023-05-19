from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.text_processing.cd_generate_chars import GenerateCharsDescriptor
from common.models.component_descriptors.regression.rd_adapter import adapterDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel
from varname import nameof

class AdapterNodeViewModel(MLComponentNodeViewModel):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 input_dot_factory: InputDotViewModelFactoryBase,
                 output_dot_factory: OutputDotViewModelFactoryBase):
        super().__init__(ml_component_descriptor)
        self.__output_dot_factory = output_dot_factory
        self.__input_dot_factory = input_dot_factory
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__input = self.__input_dot_factory.create(self.component_id, self._descriptor.pre)
        self.__double_1 = self.__output_dot_factory.create(self.component_id, self._descriptor.suc)
        self.__double_2 = self.__output_dot_factory.create(self.component_id, self._descriptor.suc_2)

    @property
    def title(self):
        return 'Adapter'

    @property
    def input(self):
        return self.__input

    @property
    def double_1(self):
        return self.__double_1

    @property
    def double_1(self):
        return self.__double_1

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = adapterDescriptor(self.component_id)
        descriptor.pre = self.__input.predecessor_descriptor
        descriptor.suc = self.__double_1.successor_descriptor
        descriptor.suc = self.__double_2.successor_descriptor
        return descriptor