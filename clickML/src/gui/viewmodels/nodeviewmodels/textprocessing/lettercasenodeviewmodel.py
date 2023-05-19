from common.models.component_descriptors.text_processing.cd_letter_case import LetterCaseDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel
from varname import nameof


class LetterCaseViewModel(MLComponentNodeViewModel):

    __input: InputDotViewModel = None
    __output: OutputDotViewModel = None

    def __init__(self, descriptor: MLComponentDescriptor, input_dot_factory: InputDotViewModelFactoryBase,
                 output_dot_factory: OutputDotViewModelFactoryBase):
        super().__init__(descriptor)
        self.__output_dot_factory = output_dot_factory
        self.__input_dot_factory = input_dot_factory
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__is_lower_case = self._descriptor.case == 'lower'
        self.__is_upper_case = self._descriptor.case == 'upper'
        if not self.__is_lower_case and not self.__is_upper_case:
            self.__is_lower_case = True

        self.__input = self.__input_dot_factory.create(self._descriptor.component_id, self._descriptor.pre)
        self.__output = self.__output_dot_factory.create(self._descriptor.component_id, self._descriptor.suc)

    @property
    def title(self):
        return 'Letter Case'

    @property
    def output(self):
        return self.__output

    @property
    def input(self):
        return self.__input

    @property
    def is_lower_case(self):
        return self.__is_lower_case

    @is_lower_case.setter
    def is_lower_case(self, value):
        if value == self.__is_lower_case:
            return
        self.__is_lower_case = value
        self.__is_upper_case = not value
        self._notify_property_changed(nameof(self.is_lower_case), value)
        self._notify_property_changed(nameof(self.is_upper_case), not value)

    @property
    def is_upper_case(self):
        return self.__is_upper_case

    @is_upper_case.setter
    def is_upper_case(self, value):
        if value == self.__is_upper_case:
            return
        self.__is_upper_case = value
        self.__is_lower_case = not value
        self._notify_property_changed(nameof(self.__is_upper_case), value)
        self._notify_property_changed(nameof(self.is_lower_case), not value)

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = LetterCaseDescriptor(self.component_id)
        if self.is_upper_case:
            descriptor.case = 'upper'
        if self.is_lower_case:
            descriptor.case = 'lower'
        descriptor.pre = self.input.predecessor_descriptor
        descriptor.suc = self.output.successor_descriptor
        return descriptor
