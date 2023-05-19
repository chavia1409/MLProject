from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.text_processing.cd_save_text import SaveTextDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, OutputDotViewModelFactoryBase
from gui.services.filepickersevicebase import FilePickerServiceBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel
from varname import nameof

class SaveTextNodeViewModel(MLComponentNodeViewModel):

    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                input_dot_factory: InputDotViewModelFactoryBase,
                output_dot_factory: OutputDotViewModelFactoryBase,
                file_picker: FilePickerServiceBase):
        super().__init__(ml_component_descriptor)
        self.__input_dot_factory = input_dot_factory
        self.__output_dot_factory = output_dot_factory
        self.__file_picker = file_picker
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__input: InputDotViewModel = self.__input_dot_factory.create(self._descriptor.component_id, self._descriptor.pre)
        self.__output: OutputDotViewModel = self.__output_dot_factory.create(self._descriptor.component_id, self._descriptor.suc)
        self.__path = self._descriptor.file
        if self.__path == DEFAULT:
            self.__path = ''
        self.__encoding = self._descriptor.encoding
        self.__errors = self._descriptor.errors
        self.__newline = self._descriptor.newline

    @property
    def input(self):
        return self.__input
    
    @property
    def output(self):
        return self.__output

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        if value == self.__path:
            return
        self.__path = value
        self._notify_property_changed('path', value)

    def select_path(self):
        path = self.__file_picker.save_file_name(filters = ['*.txt'])
        if path is None:
            return
        self.path = path

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
    def title(self):
        return 'Save Text'

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = SaveTextDescriptor(self.component_id)
        descriptor.suc = self.output.successor_descriptor
        descriptor.pre = self.input.predecessor_descriptor
        if self.__path.isspace():
            descriptor.file = DEFAULT
        else:
            descriptor.file = self.__path
        descriptor.encoding = self.encoding
        descriptor.newline = self.newline
        if self.newline == 'None':
            descriptor.newline = None
        return descriptor