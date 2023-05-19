from backend.ml_components.regression.r_predict_lin_log import pred_type
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.text_processing.cd_generate_chars import GenerateCharsDescriptor
from common.models.component_descriptors.regression.rd_predict_lin_log import PredictDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel

class PredictNodeViewModel(MLComponentNodeViewModel):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 input_dot_factory: InputDotViewModelFactoryBase,
                 output_dot_factory: OutputDotViewModelFactoryBase):
        super().__init__(ml_component_descriptor)
        self.__output_dot_factory = output_dot_factory
        self.__input_dot_factory = input_dot_factory
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__from_column = self._descriptor.from_column
        if self.__from_column == DEFAULT or self.__from_column == None:
            self.__from_column = 0
        self.__to_column = self._descriptor.to_column
        if self.__to_column == DEFAULT or self.__to_column == None:
            self.__to_column = 0
        self.__from_row = self._descriptor.from_row
        if self.__from_row == DEFAULT or self.__from_row == None:
            self.__from_row = 0
        self.__to_row = self._descriptor.to_row
        if self.__to_row == DEFAULT or self.__to_row == None:
            self.__to_row = 0

        self.__prediction_type = self._descriptor.prediction_type

        self.__model_input = self.__input_dot_factory.create(self.component_id, self._descriptor.pre)
        self.__output_regression = self.__output_dot_factory.create(self.component_id, self._descriptor.suc)
        self.__output_save_csv = self.__output_dot_factory.create(self.component_id, self._descriptor.suc_2)
        self.__output_plot = self.__output_dot_factory.create(self.component_id, self._descriptor.suc_3)

    @property
    def title(self):
        return 'Prediction'

    @property
    def model_input(self):
        return self.__model_input

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
    def prediction_type(self):
        return self.__prediction_type.name

    @prediction_type.setter
    def prediction_type(self, value):
        try:
            value = pred_type[value]
        except ValueError:
            self._notify_property_changed('prediction_type', self.__prediction_type.name)
            return
        if value == self.__prediction_type:
            return
        self.__prediction_type = value
        self._notify_property_changed('prediction_type', value.name)

    @property
    def from_column(self):
        return str(self.__from_column)

    @from_column.setter
    def from_column(self, value):
        if value == '':
            self.__from_column = 0
            self._notify_property_changed('from_column', str(self.__from_column))
            return
        try:
            value = int(value)
        except ValueError:
            self._notify_property_changed('from_column', str(self.__from_column))
            return
        if value == self.__from_column:
            return
        self.__from_column = value
        self._notify_property_changed('from_column', str(value))

    @property
    def to_column(self):
        return str(self.__to_column)

    @to_column.setter
    def to_column(self, value):
        if value == '':
            self.__to_column = 0
            self._notify_property_changed('to_column', str(self.__to_column))
            return
        try:
            value = int(value)
        except ValueError:
            self._notify_property_changed('to_column', str(self.__to_column))
            return
        if value == self.__to_column:
            return
        self.__to_column = value
        self._notify_property_changed('to_column', str(value))

    @property
    def from_row(self):
        return str(self.__from_row)

    @from_row.setter
    def from_row(self, value):
        if value == '':
            self.__from_row = 0
            self._notify_property_changed('from_row', str(self.__from_row))
            return
        try:
            value = int(value)
        except ValueError:
            self._notify_property_changed('from_row', str(self.__from_row))
            return
        if value == self.__from_row:
            return
        self.__from_row = value
        self._notify_property_changed('from_row', str(value))

    @property
    def to_row(self):
        return str(self.__to_row)

    @to_row.setter
    def to_row(self, value):
        if value == '':
            self.__to_row = 0
            self._notify_property_changed('to_row', str(self.__to_row))
            return
        try:
            value = int(value)
        except ValueError:
            self._notify_property_changed('to_row', str(self.__to_row))
            return
        if value == self.__to_row:
            return
        self.__to_row = value
        self._notify_property_changed('to_row', str(value))

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = PredictDescriptor(self.component_id)
        descriptor.pre = self.__model_input.predecessor_descriptor
        descriptor.suc = self.__output_regression.successor_descriptor
        descriptor.suc_2 = self.__output_save_csv.successor_descriptor
        descriptor.suc_3 = self.__output_plot.successor_descriptor
        descriptor.prediction_type = self.__prediction_type
        descriptor.from_column = self.__from_column
        descriptor.to_column = self.__to_column
        descriptor.from_row = self.__from_row
        descriptor.to_row = self.__to_row
        return descriptor