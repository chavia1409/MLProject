import uuid

from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.neural_networks.keras_layers.ld_lstm import LSTMDescriptor
from gui.viewmodels.nodeviewmodels.neuronalnetworks.layerviewmodelbase import LayerViewModelBase


class LSTMLayerViewModel(LayerViewModelBase):
    def __init__(self, parent, descriptor):
        super().__init__(parent, descriptor)
        self.__units = 1
        if descriptor.units != DEFAULT:
            self.__units = descriptor.units
        self.__activation = ''

    @property
    def name(self):
        return 'LSTM'

    @property
    def layer_descriptor(self):
        descriptor = LSTMDescriptor(uuid.uuid4())
        descriptor.units = self.__units
        return descriptor

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