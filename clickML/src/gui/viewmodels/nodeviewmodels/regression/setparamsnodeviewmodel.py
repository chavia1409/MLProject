from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.text_processing.cd_generate_chars import GenerateCharsDescriptor
from common.models.component_descriptors.regression.rd_set_params_log import SetParamsDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel

class SetParamsNodeViewModel(MLComponentNodeViewModel):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 input_dot_factory: InputDotViewModelFactoryBase,
                 output_dot_factory: OutputDotViewModelFactoryBase):
        super().__init__(ml_component_descriptor)
        self.__output_dot_factory = output_dot_factory
        self.__input_dot_factory = input_dot_factory
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__setterArgument = self._descriptor.setterArgument

        self.__regression_input = self.__input_dot_factory.create(self.component_id, self._descriptor.pre)
        self.__output =self.__output_dot_factory.create(self.component_id, self._descriptor.suc)

    @property
    def title(self):
        return 'SetParams'

    @property
    def regression_input(self):
        return self.__regression_input

    @property
    def output(self):
        return self.__output

    @property
    def setterArgument(self):
        return self.__setterArgument

    @setterArgument.setter
    def setterArgument(self, value):
        if value == self.__setterArgument:
            return
        self.__setterArgument = value
        self._notify_property_changed('setterArgument', value)

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = SetParamsDescriptor(self.component_id)
        descriptor.pre = self.__regression_input.predecessor_descriptor
        descriptor.suc = self.__output.successor_descriptor
        descriptor.setterArgument = self.__setterArgument
        return descriptor