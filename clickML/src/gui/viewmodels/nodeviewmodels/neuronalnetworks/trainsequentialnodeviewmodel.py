from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.neural_networks.cd_train_sequential import TrainSequentialDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.mvvm.viewmodelbase import ViewModelBase
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel


class TrainSequentialNodeViewModel(MLComponentNodeViewModel):

    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 input_dot_factory: InputDotViewModelFactoryBase,
                 output_dot_factory: OutputDotViewModelFactoryBase):
        super().__init__(ml_component_descriptor)

        self.__output_dot_factory = output_dot_factory
        self.__input_dot_factory = input_dot_factory
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__training_net_input = self.__input_dot_factory.create(self.component_id, self._descriptor.pre)
        self.__training_net_output = self.__input_dot_factory.create(self.component_id, self._descriptor.pre_2)
        self.__model_input = self.__input_dot_factory.create(self.component_id, self._descriptor.pre_3)
        self.__model_output = self.__output_dot_factory.create(self.component_id, self._descriptor.suc)

        self.__batch_size_enabled = self._descriptor.batch_size is not None and self._descriptor.batch_size != DEFAULT
        self.__batch_size = 0

        if self.__batch_size_enabled:
            self.__batch_size = self._descriptor.batch_size

        self.__validation_split_enabled = self._descriptor.validation_split != DEFAULT
        self.__validation_split_percent = 50

        if self.__validation_split_enabled:
            self.__validation_split_percent = int(self._descriptor.validation_split * 100)

        self.__selected_verbose_mode = self._descriptor.verbose

        self.__epochs_enabled = self._descriptor.epochs != DEFAULT
        self.__epochs = 1
        if self.__epochs_enabled:
            self.__epochs = self._descriptor.epochs

        self.__plot_progress = self._descriptor.plot_progress
        self.__save_weights = self._descriptor.save_weights


    @property
    def training_net_input(self):
        return self.__training_net_input

    @property
    def training_net_output(self):
        return self.__training_net_output

    @property
    def model_input(self):
        return self.__model_input

    @property
    def model_output(self):
        return self.__model_output

    @model_input.setter
    def model_input(self, value):
        pass

    @property
    def batch_size_enabled(self):
        return self.__batch_size_enabled

    @batch_size_enabled.setter
    def batch_size_enabled(self, value):
        if self.__batch_size_enabled == value:
            return
        self.__batch_size_enabled = value
        self._notify_property_changed('batch_size_enabled', value)
        
    @property
    def batch_size(self):
        return str(self.__batch_size)
    
    @batch_size.setter
    def batch_size(self, value):
        if value == '':
            self.__batch_size = 0
            self._notify_property_changed('batch_size', str(0))
            return
        try:
            value = int(value)
        except ValueError:
            self._notify_property_changed('batch_size', str(self.__batch_size))
            return

        if self.__batch_size == value:
            return
        self.__batch_size = value
        self._notify_property_changed('batch_size', str(value))

    @property
    def epochs_enabled(self):
        return self.__epochs_enabled

    @epochs_enabled.setter
    def epochs_enabled(self, value):
        if self.__epochs_enabled == value:
            return
        self.__epochs_enabled = value
        self._notify_property_changed('epochs_enabled', value)

    @property
    def epochs(self):
        return str(self.__epochs)

    @epochs.setter
    def epochs(self, value):
        if value == '':
            self.__epochs = 0
            self._notify_property_changed('epochs', str(0))
            return

        try:
            value = int(value)
        except ValueError:
            self._notify_property_changed('epochs', str(self.__epochs))
            return
        if self.__epochs == value:
            return
        self.__epochs = value
        self._notify_property_changed('epochs', str(value))

    @property
    def selected_verbose_mode(self):
        return self.__selected_verbose_mode

    @selected_verbose_mode.setter
    def selected_verbose_mode(self, value):
        if self.__selected_verbose_mode == value:
            return
        self.__selected_verbose_mode = value
        self._notify_property_changed('selected_verbose_mode', value)

    @property
    def validation_split_enabled(self):
        return self.__validation_split_enabled

    @validation_split_enabled.setter
    def validation_split_enabled(self, value):
        if self.__validation_split_enabled == value:
            return
        self.__validation_split_enabled = value
        self._notify_property_changed('validation_split_enabled', value)

    @property
    def validation_split_percent(self):
        return self.__validation_split_percent

    @validation_split_percent.setter
    def validation_split_percent(self, value):
        if self.__validation_split_percent == value:
            return
        self.__validation_split_percent = value
        self._notify_property_changed('validation_split_percent', value)

    @property
    def plot_progress(self):
        return self.__plot_progress

    @plot_progress.setter
    def plot_progress(self, value):
        if self.__plot_progress == value:
            return
        self.__plot_progress = value
        self._notify_property_changed('plot_progress', value)

    @property
    def save_weights(self):
        return self.__save_weights

    @save_weights.setter
    def save_weights(self, value):
        if self.__save_weights == value:
            return
        self.__save_weights = value
        self._notify_property_changed('save_weights', value)

    @property
    def title(self):
        return 'Train Sequential Model'

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = TrainSequentialDescriptor(self.component_id)
        descriptor.pre = self.__training_net_input.predecessor_descriptor
        descriptor.pre_2 = self.__training_net_output.predecessor_descriptor
        descriptor.pre_3 = self.__model_input.predecessor_descriptor
        descriptor.suc = self.__model_output.successor_descriptor

        descriptor.batch_size = self.__batch_size
        if not self.__batch_size_enabled:
            descriptor.batch_size = DEFAULT
        descriptor.epochs = self.__epochs
        if not self.__epochs_enabled:
            descriptor.epochs = DEFAULT
        descriptor.verbose = self.__selected_verbose_mode
        descriptor.validation_split = self.__validation_split_percent / 100
        if not self.__validation_split_enabled:
            descriptor.validation_split = DEFAULT
        descriptor.plot_progress = self.__plot_progress
        descriptor.save_weights = self.__save_weights

        return descriptor

