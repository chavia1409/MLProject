from varname import nameof

from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.text_processing.cd_divide_chars_by_sentences import \
    DivideCharsBySentencesDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel


class DivideCharsBySentencesNodeViewModel(MLComponentNodeViewModel):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 input_dot_factory: InputDotViewModelFactoryBase,
                 output_dot_factory: OutputDotViewModelFactoryBase):
        super().__init__(ml_component_descriptor)
        self.__output_dot_factory = output_dot_factory
        self.__input_dot_factory = input_dot_factory
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__input_text: InputDotViewModel = self.__input_dot_factory.create(self._descriptor.component_id,
                                                                          self._descriptor.pre)
        self.__prediction_input: OutputDotViewModel = self.__output_dot_factory.create(self._descriptor.component_id,
                                                                             self._descriptor.suc)
        self.__net_input: OutputDotViewModel = self.__output_dot_factory.create(self._descriptor.component_id,
                                                                             self._descriptor.suc_2)
        self.__net_output: OutputDotViewModel = self.__output_dot_factory.create(self._descriptor.component_id,
                                                                             self._descriptor.suc_3)
        self.__input_shape: OutputDotViewModel = self.__output_dot_factory.create(self._descriptor.component_id,
                                                                             self._descriptor.suc_4)
        self.__output_shape: OutputDotViewModel = self.__output_dot_factory.create(self._descriptor.component_id,
                                                                             self._descriptor.suc_5)
        if self._descriptor.max_seq_length  == DEFAULT:
            self.__max_seq_length = 0
        else:
            self.__max_seq_length = self._descriptor.max_seq_length

    @property
    def title(self):
        return "Divide Chars By Sentence"
    @property
    def prediction_input(self):
        return self.__prediction_input

    @property
    def input_text(self):
        return self.__input_text

    @property
    def net_input(self):
        return self.__net_input

    @property
    def net_output(self):
        return self.__net_output

    @property
    def input_shape(self):
        return self.__input_shape

    @property
    def output_shape(self):
        return self.__output_shape

    @property
    def max_seq_length(self):
        return self.__max_seq_length

    @max_seq_length.setter
    def max_seq_length(self, value):
        self.__max_seq_length = value
        self._notify_property_changed(nameof(self.__max_seq_length), value)

    @prediction_input.setter
    def prediction_input(self, value):
        if value == self.prediction_input:
            return
        self.__prediction_input = value
        self._notify_property_changed(nameof(self.prediction_input), value)

    @input_text.setter
    def input_text(self, value):
        if value == self.input_text:
            return
        self.__input_text = value
        self._notify_property_changed(nameof(self.input_text), value)

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = DivideCharsBySentencesDescriptor(self.component_id)
        descriptor.pre = self.input_text.predecessor_descriptor
        descriptor.suc = self.prediction_input.successor_descriptor
        descriptor.suc_2 = self.net_input.successor_descriptor
        descriptor.suc_3 = self.net_output.successor_descriptor
        descriptor.suc_4 = self.input_shape.successor_descriptor
        descriptor.suc_5 = self.output_shape.successor_descriptor
        descriptor.max_seq_length = self.max_seq_length
        return descriptor



