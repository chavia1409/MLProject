from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.regression.rd_save_logfile import SaveLogfileDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.services.filepickersevicebase import FilePickerServiceBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel
from gui.mvvm.command import Command


class SaveLogfileNodeViewModel(MLComponentNodeViewModel):

    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 input_dot_factory: InputDotViewModelFactoryBase,
                 file_picker: FilePickerServiceBase):
        super().__init__(ml_component_descriptor)
        self.__input_dot_factory = input_dot_factory
        self.__file_picker = file_picker
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__input: InputDotViewModel = self.__input_dot_factory.create(self._descriptor.component_id, self._descriptor.pre)
        self.__filePath = self._descriptor.filePath
        if self.__filePath == DEFAULT:
            self.__filePath = ''

    @property
    def title(self):
        return 'SaveLogfile'

    @property
    def input(self):
        return self.__input

    @property
    def filePath(self):
        return self.__filePath

    @filePath.setter
    def filePath(self, value):
        if value == self.__filePath:
            return
        self.__filePath = value
        self._notify_property_changed('filePath', value)

    def select_path(self):
        filePath = self.__file_picker.save_file_name(filters = ['*.txt'])
        if filePath == None:
            return
        self.filePath = filePath

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = SaveLogfileDescriptor(self.component_id)
        descriptor.pre = self.input.predecessor_descriptor
        if self.__filePath.isspace():
            descriptor.filePath = DEFAULT
        else:
            descriptor.filePath = self.__filePath
        return descriptor
