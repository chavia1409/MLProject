from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.csv_processing.cd_csv_to_array import ReadCSVDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import OutputDotViewModelFactoryBase
from gui.services.filepickersevicebase import FilePickerServiceBase
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel


class CsvToArrayNodeViewModel(MLComponentNodeViewModel):

    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 output_dot_factory: OutputDotViewModelFactoryBase,
                 file_picker: FilePickerServiceBase):
        super().__init__(ml_component_descriptor)
        self.__output_dot_factory = output_dot_factory
        self.__file_picker = file_picker
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__output: OutputDotViewModel = self.__output_dot_factory.create(self._descriptor.component_id,
                                                                             self._descriptor.suc)
        self.__csvFilePath = self._descriptor.csvFilePath
        if self.__csvFilePath == DEFAULT:
            self.__csvFilePath = ''



    @property
    def output(self):
        return self.__output

    @property
    def csvFilePath(self):
        return self.__csvFilePath

    @csvFilePath.setter
    def csvFilePath(self, value):
        if value == self.__csvFilePath:
            return
        self.__csvFilePath = value
        self._notify_property_changed('csvFilePath', value)

    def select_path(self):
        csvFilePath = self.__file_picker.pick_file_name(filters=['*.csv'])
        if csvFilePath == None:
            return
        self.csvFilePath = csvFilePath

    @property
    def title(self):
        return 'Csv To Array'

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = ReadCSVDescriptor(self.component_id)
        descriptor.suc = self.output.successor_descriptor
        if self.__csvFilePath.isspace():
            descriptor.csvFilePath = DEFAULT
        else:
            descriptor.csvFilePath = self.__csvFilePath
        return descriptor