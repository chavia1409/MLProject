from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.text_processing.cd_generate_chars import GenerateCharsDescriptor
from common.models.component_descriptors.text_processing.cd_letter_case import LetterCaseDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel
from varname import nameof


class GenerateCharsNodeViewModel(MLComponentNodeViewModel):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 input_dot_factory: InputDotViewModelFactoryBase,
                 output_dot_factory: OutputDotViewModelFactoryBase):
        super().__init__(ml_component_descriptor)
        self.__output_dot_factory = output_dot_factory
        self.__input_dot_factory = input_dot_factory
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__init_chars_mode = self._descriptor.init_chars_mode
        if self._descriptor.number_of_chars == DEFAULT:
            self.__number_of_chars = 0
        else:
            self.__number_of_chars = self._descriptor.number_of_chars

        self.__model_input = self.__input_dot_factory.create(self.component_id, self._descriptor.pre)
        self.__init_chars_input = self.__input_dot_factory.create(self.component_id, self._descriptor.pre_2)
        self.__generated_text_output = self.__output_dot_factory.create(self.component_id, self._descriptor.suc)

    @property
    def title(self):
        return 'Generate Chars'

    @property
    def model_iput(self):
        return self.__model_input

    @property
    def init_chars_input(self):
        return self.__init_chars_input

    @property
    def generate_text_output(self):
        return self.__generated_text_output

    @property
    def init_chars_mode(self):
        return self.__init_chars_mode

    @init_chars_mode.setter
    def init_chars_mode(self, value):
        if value == self.__init_chars_mode:
            return
        self.__init_chars_mode = value
        self._notify_property_changed('init_chars_mode', value)

    @property
    def number_of_chars(self):
        return self.__number_of_chars

    @number_of_chars.setter
    def number_of_chars(self, value):
        value = int(value)
        if value < 0:
            self.__number_of_chars = 0
            self._notify_property_changed('number_of_chars', 0)
            return
        if value == self.__number_of_chars:
            return
        self.__number_of_chars = value
        self._notify_property_changed('number_of_chars', value)
        
    @property
    def ml_component_descriptor(self):
        descriptor = GenerateCharsDescriptor(self.component_id)
        descriptor.pre = self.__model_input.predecessor_descriptor
        descriptor.pre_2 = self.__init_chars_input.predecessor_descriptor
        descriptor.suc = self.__generated_text_output.successor_descriptor
        descriptor.number_of_chars = self.__number_of_chars
        descriptor.init_chars_mode = self.__init_chars_mode
        return descriptor
