import uuid

from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.neural_networks.keras_layers.ld_dropout import DropoutDescriptor
from gui.viewmodels.nodeviewmodels.neuronalnetworks.layerviewmodelbase import LayerViewModelBase


class DropoutLayerViewModel(LayerViewModelBase):
    def __init__(self, parent, descriptor):
        super().__init__(parent, descriptor)
        self.__rate_in_percent = 0
        if descriptor.rate is not DEFAULT:
            self.__rate_in_percent = descriptor.rate * 100
        self.__seed_enabled = False
        self.__seed = 0
        if descriptor.seed != DEFAULT:
            self.__seed = descriptor.seed
            self.__seed_enabled = True
    @property
    def name(self):
        return 'Dropout'

    @property
    def rate_in_percent(self):
        return self.__rate_in_percent

    @rate_in_percent.setter
    def rate_in_percent(self, value):
        value = int(value)
        if value is self.__rate_in_percent:
            return
        self.__rate_in_percent = value
        self._notify_property_changed('rate_in_percent', value)

    @property
    def seed_enabled(self):
        return self.__seed_enabled

    @seed_enabled.setter
    def seed_enabled(self, value):
        if value is self.__seed_enabled:
            return
        self.__seed_enabled = value
        self._notify_property_changed('seed_enabled', value)

    @property
    def seed(self):
        return str(self.__seed)

    @seed.setter
    def seed(self, value):
        if value is '':
            self.__seed = 0
            self._notify_property_changed('seed', str(self.__seed))
            return
        try:
            value = int(value)
        except ValueError:
            self._notify_property_changed('seed', str(self.__seed))
            return
        if value is self.__seed:
            return
        self.__seed = value
        self._notify_property_changed('seed', str(self.__seed))

    @property
    def layer_descriptor(self):
        descriptor = DropoutDescriptor(uuid.uuid4())
        descriptor.rate = self.rate_in_percent / 100
        if self.__seed_enabled:
            descriptor.seed = self.__seed
        return descriptor

