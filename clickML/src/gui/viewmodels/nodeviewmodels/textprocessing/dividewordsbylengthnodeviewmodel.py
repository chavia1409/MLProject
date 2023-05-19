from varname import nameof

from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.text_processing.cd_divide_words_by_length import DivideWordsByLengthDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.services.filepickersevicebase import FilePickerServiceBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel


class DivideWordsByLengthNodeViewModel(MLComponentNodeViewModel):

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
        if self._descriptor.seq_length == DEFAULT:
            self.__seq_length = 0
        else:
            self.__seq_length = self._descriptor.seq_length

    @property
    def title(self):
        return "Divide Words By Length"
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
    def seq_length(self):
        return self.__seq_length

    @prediction_input.setter
    def prediction_input(self, value):
        if value == self.prediction_input:
            return
        self.__prediction_input = value
        self._notify_property_changed(nameof(self.__prediction_input), value)

    @input_text.setter
    def input_text(self, value):
        if value == self.input_text:
            return
        self.__input_text = value
        self._notify_property_changed(nameof(self.__input_text), value)

    @seq_length.setter
    def seq_length(self, value):
        if value < 0:
            return
        self.__seq_length = value
        self._notify_property_changed(nameof(self.__seq_length), value)

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = DivideWordsByLengthDescriptor(self.component_id)
        descriptor.pre = self.input_text.predecessor_descriptor
        descriptor.suc = self.prediction_input.successor_descriptor
        descriptor.suc_2 = self.net_input.successor_descriptor
        descriptor.suc_3 = self.net_output.successor_descriptor
        descriptor.suc_4 = self.input_shape.successor_descriptor
        descriptor.suc_5 = self.output_shape.successor_descriptor
        descriptor.seq_length = self.seq_length
        return descriptor
