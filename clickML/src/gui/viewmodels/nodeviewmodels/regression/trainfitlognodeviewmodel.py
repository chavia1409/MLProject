from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.text_processing.cd_generate_chars import GenerateCharsDescriptor
from common.models.component_descriptors.regression.rd_train_fit_log import Train_Fit_Log_Descriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel

class TrainFitLogNodeViewModel(MLComponentNodeViewModel):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 input_dot_factory: InputDotViewModelFactoryBase,
                 output_dot_factory: OutputDotViewModelFactoryBase):
        super().__init__(ml_component_descriptor)
        self.__output_dot_factory = output_dot_factory
        self.__input_dot_factory = input_dot_factory
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__test_size = self._descriptor.test_size
        if self.__test_size == DEFAULT or self.__test_size == None:
            self.__test_size = 30
        self.__train_size = self._descriptor.train_size
        if self.__train_size == DEFAULT or self.__train_size == None:
            self.__train_size = 70
        self.__random = self._descriptor.random
        if self.__random == DEFAULT or self.__random == None:
            self.__random = 42
        if self._descriptor.shuffle is None or self._descriptor.shuffle is DEFAULT:
            self.__shuffle = False
        else:
            self.__shuffle = self._descriptor.shuffle
        self.__X_Plot_value = self._descriptor.X_Plot_value
        self.__Y_Plot_value = self._descriptor.Y_Plot_value

        self.__data_input = self.__input_dot_factory.create(self.component_id, self._descriptor.pre)
        self.__target_input = self.__input_dot_factory.create(self.component_id, self._descriptor.pre_2)
        self.__output_regression = self.__output_dot_factory.create(self.component_id, self._descriptor.suc)
        self.__output_save_csv = self.__output_dot_factory.create(self.component_id, self._descriptor.suc_2)
        self.__output_plot = self.__output_dot_factory.create(self.component_id, self._descriptor.suc_3)

    @property
    def title(self):
        return 'Training FitLog'

    @property
    def data_input(self):
        return self.__data_input

    @property
    def target_input(self):
        return self.__target_input

    @property
    def output_regression(self):
        return self.__output_regression

    @property
    def output_save_csv(self):
        return self.__output_save_csv

    @property
    def output_plot(self):
        return self.__output_plot

    @property
    def test_size(self):
        return str(self.__test_size)

    @test_size.setter
    def test_size(self, value):
        if value == '':
            self.__test_size = 0
            self._notify_property_changed('test_size', str(self.__test_size))
            return
        try:
            value = int(value)
        except ValueError:
            self._notify_property_changed('test_size', str(self.__test_size))
            return
        if value > 100 or value < 0:
            value = self.__test_size
            self._notify_property_changed('test_size', str(self.__test_size))
        if value == self.__test_size:
            return
        self.__test_size = value
        self._notify_property_changed('test_size', str(value))

    @property
    def train_size(self):
        return str(self.__train_size)

    @train_size.setter
    def train_size(self, value):
        if value == '':
            self.__train_size = 0
            self._notify_property_changed('train_size', str(self.__train_size))
            return
        try:
            value = int(value)
        except ValueError:
            self._notify_property_changed('train_size', str(self.__train_size))
            return
        if value > 100 or value < 0:
            value = self.__train_size
            self._notify_property_changed('train_size', str(self.__train_size))
        if value == self.__train_size:
            return
        self.__train_size = value
        self._notify_property_changed('train_size', str(value))

    @property
    def random(self):
        return str(self.__random)

    @random.setter
    def random(self, value):
        if value == '':
            self.__random = 0
            self._notify_property_changed('random', str(self.__random))
            return
        try:
            value = int(value)
        except ValueError:
            self._notify_property_changed('random', str(self.__random))
            return
        if value == self.__random:
            return
        self.__random = value
        self._notify_property_changed('random', str(value))

    @property
    def shuffle(self):
        return self.__shuffle

    @shuffle.setter
    def shuffle(self, value):
        if value == self.__shuffle:
            return
        self.__shuffle = value
        self._notify_property_changed('shuffle', value)

    @property
    def X_Plot_value(self):
        return self.__X_Plot_value

    @X_Plot_value.setter
    def X_Plot_value(self, value):
        if value == self.__X_Plot_value:
            return
        self.__X_Plot_value = value
        self._notify_property_changed('X_Plot_value', value)

    @property
    def Y_Plot_value(self):
        return self.__Y_Plot_value

    @Y_Plot_value.setter
    def Y_Plot_value(self, value):
        if value == self.__Y_Plot_value:
            return
        self.__Y_Plot_value = value
        self._notify_property_changed('Y_Plot_value', value)

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = Train_Fit_Log_Descriptor(self.component_id)
        descriptor.pre = self.__data_input.predecessor_descriptor
        descriptor.pre_2 = self.__target_input.predecessor_descriptor
        descriptor.suc = self.__output_regression.successor_descriptor
        descriptor.suc_2 = self.__output_save_csv.successor_descriptor
        descriptor.suc_3 = self.__output_plot.successor_descriptor
        descriptor.test_size = self.__test_size
        descriptor.train_size = self.__train_size
        descriptor.random = self.__random
        descriptor.shuffle = self.__shuffle
        descriptor.X_Plot_value = self.__X_Plot_value
        descriptor.Y_Plot_value = self.__Y_Plot_value
        return descriptor