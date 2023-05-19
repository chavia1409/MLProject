from varname import nameof

from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.text_processing.cd_text_reader import TextReaderDescriptor

from common.models.mlcomponentdescriptor import MLComponentDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.services.filepickersevicebase import FilePickerServiceBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel
from gui.mvvm.command import Command

class TextReaderNodeViewModel(MLComponentNodeViewModel):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 input_dot_factory: InputDotViewModelFactoryBase,
                 output_dot_factory: OutputDotViewModelFactoryBase, file_picker:FilePickerServiceBase):
        super().__init__(ml_component_descriptor)
        self.__output_dot_factory = output_dot_factory
        self.__input_dot_factory = input_dot_factory
        self._set_descriptor_values()
        self.__file_picker = file_picker


    def _set_descriptor_values(self):
        self.__output: OutputDotViewModel = self.__output_dot_factory.create(self._descriptor.component_id,
                                                                             self._descriptor.suc)
        self.__file = self._descriptor.file
        self.__encoding = self._descriptor.encoding
        self.__errors = self._descriptor.errors
        self.__newline = self._descriptor.newline
        if self.__file == DEFAULT:
            self.__file = ''

    @property
    def title(self):
        return "Text Reader"

    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, value):
        self.__output=value
        self._notify_property_changed("output", value)

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, value):
        self.__file = value
        self._notify_property_changed("file", value)

    @property
    def encoding(self):
        return self.__encoding

    @encoding.setter
    def encoding(self, value):
        if value == self.__encoding:
            return
        self.__encoding = value
        self._notify_property_changed('encoding', value)

    @property
    def errors(self):
        return self.__errors

    @errors.setter
    def errors(self, value):
        if value == self.__errors:
            return
        self.__errors = value
        self._notify_property_changed('errors', value)

    @property
    def newline(self):
        return self.__newline

    @newline.setter
    def newline(self, value):
        if value == self.__newline:
            return
        self.__newline = value
        self._notify_property_changed('newline', value)

    @property
    def select_command(self):
        return Command(self.select)

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = TextReaderDescriptor(self.component_id)
        descriptor.suc = self.output.successor_descriptor
        if self.__file.isspace():
            descriptor.file = DEFAULT
        else:
            descriptor.file = self.__file
        descriptor.encoding = self.encoding
        descriptor.newline = self.newline
        if self.newline == 'None':
            descriptor.newline = None
        return descriptor

    def select(self, args):
        path = self.__file_picker.pick_file_name(filters=['*.txt'])
        if path == None:
            return
        self.file = path