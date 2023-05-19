from common.models.component_descriptors.component_constants import DEFAULT
# from common.models.component_descriptors.csv_processing.cd_csv_to_array import ReadCSVDescriptor
from common.models.component_descriptors.csv_processing.cd_save_array_csv import SaveToArrayOrCsvDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import OutputDotViewModelFactoryBase, \
    InputDotViewModelFactoryBase
from gui.services.filepickersevicebase import FilePickerServiceBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel


class SaveToArrayOrCsvNodeViewModel(MLComponentNodeViewModel):
    __input: InputDotViewModel = None
    __output: OutputDotViewModel = None

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
        self.__input: InputDotViewModel = self.__input_dot_factory.create(self._descriptor.component_id,
                                                                             self._descriptor.pre)
        self.__output: OutputDotViewModel = self.__output_dot_factory.create(self._descriptor.component_id,
                                                                             self._descriptor.suc)
        self.__targetFilePath = self._descriptor.targetFilePath
        if self.__targetFilePath == DEFAULT:
            self.__targetFilePath = ''
        self.__ArrayOrCsv = self._descriptor.ArrayOrCsv
        self.__indexing = self._descriptor.indexing



    @property
    def output(self):
        return self.__output

    @property
    def input(self):
        return self.__input

    @property
    def ArrayOrCsv(self):
        return self.__ArrayOrCsv

    @ArrayOrCsv.setter
    def ArrayOrCsv(self, value):
        if value == self.__ArrayOrCsv:
            return
        self.__ArrayOrCsv = value
        self._notify_property_changed('ArrayOrCsv', value)

    @property
    def targetFilePath(self):
        return self.__targetFilePath

    @targetFilePath.setter
    def targetFilePath(self, value):
        if value == self.__targetFilePath:
            return
        self.__targetFilePath = value
        self._notify_property_changed('targetFilePath', value)

    def select_path(self):
        targetFilePath = self.__file_picker.save_file_name(filters=['*.csv'])
        if targetFilePath == None:
            return
        self.targetFilePath = targetFilePath

    @property
    def indexing(self):
        return self.__indexing

    @indexing.setter
    def indexing(self, value):
        if value == self.__indexing:
            return
        self.__indexing = value
        self._notify_property_changed('indexing', value)

    @property
    def title(self):
        return 'Save to Array Or Csv'

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = SaveToArrayOrCsvDescriptor(self.component_id)
        descriptor.suc = self.output.successor_descriptor
        descriptor.pre = self.input.predecessor_descriptor
        if self.__ArrayOrCsv == 'None':
            descriptor.ArrayOrCsv = DEFAULT
        else:
            descriptor.ArrayOrCsv = self.__ArrayOrCsv
        descriptor.indexing = self.__indexing
        if self.__targetFilePath.isspace():
            descriptor.targetFilePath = DEFAULT
        else:
            descriptor.targetFilePath = self.__targetFilePath
        return descriptor