from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.text_processing.cd_print_text import PrintTextDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel


class PrintTextNodeViewModel(MLComponentNodeViewModel):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 input_dot_factory: InputDotViewModelFactoryBase,
                 output_dot_factory: OutputDotViewModelFactoryBase):
        super().__init__(ml_component_descriptor)
        self.__input_dot_factory = input_dot_factory
        self.__output_dot_factory = output_dot_factory
        self._set_descriptor_values()


    def _set_descriptor_values(self):
        self.__input: InputDotViewModel = self.__input_dot_factory.create(self._descriptor.component_id,
                                                                          self._descriptor.pre)
        self.__output: OutputDotViewModel = self.__output_dot_factory.create(self._descriptor.component_id,
                                                                             self._descriptor.suc)
        self.__number_of_chars_enabled = True
        self.__number_of_chars = self._descriptor.number_of_chars
        if self._descriptor.number_of_chars == DEFAULT:
            self.__number_of_chars_enabled = False
            self.__number_of_chars = 1

    @property
    def number_of_chars_enabled(self):
        return self.__number_of_chars_enabled

    @number_of_chars_enabled.setter
    def number_of_chars_enabled(self, value):
        if self.__number_of_chars_enabled == value:
            return
        self.__number_of_chars_enabled = value
        self._notify_property_changed('number_of_chars_enabled', value)

    @property
    def number_of_chars(self):
        return self.__number_of_chars

    @number_of_chars.setter
    def number_of_chars(self, value):
        if self.__number_of_chars == value:
            return
        self.__number_of_chars = value
        self._notify_property_changed('number_of_chars', value)


    @property
    def title(self):
        return 'Print Text'

    @property
    def input(self):
        return self.__input

    @property
    def output(self):
        return self.__output

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = PrintTextDescriptor(self.component_id)
        descriptor.suc = self.output.successor_descriptor
        descriptor.pre = self.input.predecessor_descriptor
        descriptor.number_of_chars = self.__number_of_chars
        if not self.__number_of_chars_enabled:
            descriptor.number_of_chars = DEFAULT
        return descriptor


