from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.text_processing.cd_generate_chars import GenerateCharsDescriptor
from common.models.component_descriptors.regression.rd_train_multivariate_linear_model import TrainMultivariateLinearRegressionDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel
from varname import nameof

class TrainMultivariateLinearRegressionNodeViewModel(MLComponentNodeViewModel):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 input_dot_factory: InputDotViewModelFactoryBase,
                 output_dot_factory: OutputDotViewModelFactoryBase):
        super().__init__(ml_component_descriptor)
        self.__output_dot_factory = output_dot_factory
        self.__input_dot_factory = input_dot_factory
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__test_size = self._descriptor.test_size
        if self.__test_size == DEFAULT:
            self.__test_size = 0.25
        self.__train_size = self._descriptor.train_size
        if self.__train_size == DEFAULT:
            self.__train_size = 1 - self.__test_size
        self.__random_int = self._descriptor.random_int

        self.__data_input = self.__input_dot_factory.create(self.component_id, self._descriptor.pre)
        self.__target_input = self.__input_dot_factory.create(self.component_id, self._descriptor.pre_2)
        self.__output_regression = self.__output_dot_factory.create(self.component_id, self._descriptor.suc)
        self.__output_save_csv = self.__output_dot_factory.create(self.component_id, self._descriptor.suc_2)
        self.__output_plot = self.__output_dot_factory.create(self.component_id, self._descriptor.suc_3)

    @property
    def title(self):
        return 'TrainMultivariateLinearRegression'

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
        return self.__test_size

    @test_size.setter
    def test_size(self, value):
        if value == self.__test_size:
            return
        self.__test_size = value
        self._notify_property_changed(nameof(self.__test_size), value)

    @property
    def train_size(self):
        return self.__train_size

    @train_size.setter
    def train_size(self, value):
        if value == self.__train_size:
            return
        self.__train_size = value
        self._notify_property_changed(nameof(self.__train_size), value)

    @property
    def random_int(self):
        return self.__random_int

    @random_int.setter
    def random_int(self, value):
        if value == self.__random_int:
            return
        self.__random_int = value
        self._notify_property_changed(nameof(self.__random_int), value)

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = TrainMultivariateLinearRegressionDescriptor(self.component_id)
        descriptor.pre = self.__data_input.predecessor_descriptor
        descriptor.pre_2 = self.__target_input.predecessor_descriptor
        descriptor.suc = self.__output_regression.successor_descriptor
        descriptor.suc_2 = self.__output_save_csv.successor_descriptor
        descriptor.suc_3 + self.__output_plot.successor_descriptor
        descriptor.test_size = self.__test_size
        descriptor.train_size = self.__train_size
        descriptor.random_int = self.__random_int
        return descriptor