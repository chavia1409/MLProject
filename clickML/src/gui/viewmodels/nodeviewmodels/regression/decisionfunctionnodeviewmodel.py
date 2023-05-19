from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.text_processing.cd_generate_chars import GenerateCharsDescriptor
from common.models.component_descriptors.regression.rd_decision_function_log import DecisionFunctionDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel
from varname import nameof

class DecisionFunctionNodeViewModel(MLComponentNodeViewModel):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 input_dot_factory: InputDotViewModelFactoryBase,
                 output_dot_factory: OutputDotViewModelFactoryBase):
        super().__init__(ml_component_descriptor)
        self.__output_dot_factory = output_dot_factory
        self.__input_dot_factory = input_dot_factory
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__print = self._descriptor.print

        self.__regression_input = self.__input_dot_factory.create(self.component_id, self._descriptor.pre)
        self.__output =self.__output_dot_factory.create(self.component_id, self._descriptor.suc)

    @property
    def title(self):
        return 'DecisionFunction'

    @property
    def regression_input(self):
        return self.__regression_input

    @property
    def output(self):
        return self.__output

    @property
    def print(self):
        return self.__print

    @print.setter
    def print(self, value):
        if value == self.__print:
            return
        self.__print = value
        self._notify_property_changed('print', value)

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = DecisionFunctionDescriptor(self.component_id)
        descriptor.pre = self.__regression_input.predecessor_descriptor
        descriptor.suc = self.__output.successor_descriptor
        descriptor.print = self.__print
        return descriptor