from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.text_processing.cd_generate_chars import GenerateCharsDescriptor
from common.models.component_descriptors.text_processing.cd_generate_words import GenerateWordsDescriptor
from common.models.component_descriptors.text_processing.cd_letter_case import LetterCaseDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel
from varname import nameof


class GenerateWordsNodeViewModel(MLComponentNodeViewModel):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 input_dot_factory: InputDotViewModelFactoryBase,
                 output_dot_factory: OutputDotViewModelFactoryBase):
        super().__init__(ml_component_descriptor)
        self.__output_dot_factory = output_dot_factory
        self.__input_dot_factory = input_dot_factory
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__init_words_mode = self._descriptor.init_words_mode
        if self._descriptor.number_of_words == DEFAULT:
            self.__number_of_words = 0
        else:
            self.__number_of_words = self._descriptor.number_of_words

        self.__model_input = self.__input_dot_factory.create(self.component_id, self._descriptor.pre)
        self.__init_words_input = self.__input_dot_factory.create(self.component_id, self._descriptor.pre_2)
        self.__generated_text_output = self.__output_dot_factory.create(self.component_id, self._descriptor.suc)

    @property
    def title(self):
        return 'Generate Words'

    @property
    def model_iput(self):
        return self.__model_input

    @property
    def init_words_input(self):
        return self.__init_words_input

    @property
    def generate_text_output(self):
        return self.__generated_text_output

    @property
    def init_words_mode(self):
        return self.__init_words_mode

    @init_words_mode.setter
    def init_words_mode(self, value):
        if value == self.__init_words_mode:
            return
        self.__init_words_mode = value
        self._notify_property_changed('init_words_mode', value)

    @property
    def number_of_words(self):
        return self.__number_of_words

    @number_of_words.setter
    def number_of_words(self, value):
        value = int(value)
        if value < 0:
            self.__number_of_words = 0
            self._notify_property_changed('number_of_words', 0)
            return
        if value == self.__number_of_words:
            return
        self.__number_of_words = value
        self._notify_property_changed('number_of_words', value)
        
    @property
    def ml_component_descriptor(self):
        descriptor = GenerateWordsDescriptor(self.component_id)
        descriptor.pre = self.__model_input.predecessor_descriptor
        descriptor.pre_2 = self.__init_words_input.predecessor_descriptor
        descriptor.suc = self.__generated_text_output.successor_descriptor
        descriptor.number_of_words = self.__number_of_words
        descriptor.init_words_mode = self.__init_words_mode
        return descriptor
