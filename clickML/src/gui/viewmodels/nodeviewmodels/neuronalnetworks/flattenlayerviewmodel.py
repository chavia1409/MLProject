import uuid

from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.neural_networks.keras_layers.ld_flatten import FlattenDescriptor
from gui.viewmodels.nodeviewmodels.neuronalnetworks.layerviewmodelbase import LayerViewModelBase


class FlattenLayerViewModel(LayerViewModelBase):
    def __init__(self, parent, descriptor):
        super().__init__(parent, descriptor)
        self.__data_format_enabled = descriptor.data_format == DEFAULT
        self.__data_format = "channel_last"
        if self.__data_format_enabled:
            self.__data_format = descriptor.data_format

    @property
    def name(self):
        return 'Flatten'

    @property
    def data_format_enabled(self):
        return self.__data_format_enabled
    
    @data_format_enabled.setter
    def data_format_enabled(self, value):
        if value == self.__data_format_enabled:
            return
        self.__data_format_enabled = value
        self._notify_property_changed('data_format_enabled', value)

    @property
    def data_format(self):
        return self.__data_format

    @data_format.setter
    def data_format(self, value):
        if value == self.__data_format:
            return
        self.__data_format = value
        self._notify_property_changed('data_format', value)

    @property
    def layer_descriptor(self):
        descriptor = FlattenDescriptor(uuid.uuid4())
        if self.__data_format_enabled:
            descriptor.data_format = self.__data_format
        return descriptor