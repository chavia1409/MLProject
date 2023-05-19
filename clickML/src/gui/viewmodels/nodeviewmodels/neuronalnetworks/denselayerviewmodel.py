import uuid

from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.neural_networks.keras_layers.ld_dense import DenseDescriptor
from gui.viewmodels.nodeviewmodels.neuronalnetworks.layerviewmodelbase import LayerViewModelBase


class DenseLayerViewModel(LayerViewModelBase):

    def __init__(self, parent, descriptor):
        super().__init__(parent, descriptor)
        self.__units = 1
        if descriptor.units is not DEFAULT:
            self.__units = descriptor.units
        self.__activation = ''
        self.__activation_enabled = False
        if descriptor.activation != DEFAULT:
            self.__activation = descriptor.activation
            self.__activation_enabled = True

    @property
    def name(self):
        return 'Dense'

    @property
    def units(self):
        return str(self.__units)

    @units.setter
    def units(self, value):
        if value == '':
            self.__units = 0
            self._notify_property_changed('units', str(self.__units))
            return
        try:
            value = int(value)
        except ValueError:
            self._notify_property_changed('units', str(self.__units))
            return
        if value < 0:
            self.__units = 0
            self._notify_property_changed('units', str(self.__units))
            return
        if value is self.__units:
            return
        self.__units = value
        self._notify_property_changed('units', str(self.__units))

    @property
    def activation_enabled(self):
        return self.__activation_enabled

    @activation_enabled.setter
    def activation_enabled(self, value):
        if value is self.__activation_enabled:
            return
        self.__activation_enabled = value
        self._notify_property_changed('activation_enabled', value)

    @property
    def activation(self):
        return self.__activation

    @activation.setter
    def activation(self, value):
        if value is self.__activation:
            return
        self.__activation = value
        self._notify_property_changed('activation', value)


    @property
    def layer_descriptor(self):
        descriptor = DenseDescriptor(uuid.uuid4())
        descriptor.units = self.__units
        if self.__activation_enabled:
            descriptor.activation = self.__activation
        return descriptor