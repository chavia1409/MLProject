import uuid

from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.neural_networks.keras_layers.ld_MaxPool2D import MaxPool2DDescriptor
from gui.viewmodels.nodeviewmodels.neuronalnetworks.layerviewmodelbase import LayerViewModelBase


class MaxPool2DLayerViewModel(LayerViewModelBase):
    def __init__(self, parent, descriptor):
        super().__init__(parent, descriptor)
        self.__pool_size_one = 0
        self.__pool_size_two = 0
        self.__two_pool_size_values = False
        if isinstance(descriptor.pool_size, tuple):
            self.__two_pool_size_values = True
            self.__pool_size_one = descriptor.pool_size[0]
            self.__pool_size_two = descriptor.pool_size[1]
        if isinstance(descriptor.pool_size, int):
            self.__two_pool_size_values = False
            self.__pool_size_one = descriptor.pool_size
            self.__pool_size_two = descriptor.pool_size
    @property
    def two_pool_size_values(self):
        return self.__two_pool_size_values

    @two_pool_size_values.setter
    def two_pool_size_values(self, value):
        if value == self.__two_pool_size_values:
            return
        self.__two_pool_size_values = value
        self._notify_property_changed('two_pool_size_values', value)

    @property
    def pool_size_one(self):
        return str(self.__pool_size_one)


    @pool_size_one.setter
    def pool_size_one(self, value):
        if value == '':
            self.__pool_size_one = 0
            self._notify_property_changed('pool_size_one', str(self.__pool_size_one))
            return
        try:
            value = int(value)
        except ValueError:
            self._notify_property_changed('pool_size_one', str(self.__pool_size_one))
            return
        if value == self.__pool_size_one:
            return

        self.__pool_size_one = value
        self._notify_property_changed('pool_size_one', str(value))
        if not self.__two_pool_size_values:
            self.pool_size_two = str(value)

    @property
    def pool_size_two(self):
        return str(self.__pool_size_two)

    @pool_size_two.setter
    def pool_size_two(self, value):
        if value == '':
            self.__pool_size_two = 0
            self._notify_property_changed('pool_size_two', str(self.__pool_size_two))
            return
        try:
            value = int(value)
        except ValueError:
            self._notify_property_changed('pool_size_two', str(self.__pool_size_two))
            return
        if value == self.__pool_size_two:
            return

        self.__pool_size_two = value
        self._notify_property_changed('pool_size_two', str(value))
        if not self.__two_pool_size_values:
            self.pool_size_one = str(value)

    @property
    def name(self):
        return 'MaxPool2D'

    @property
    def layer_descriptor(self):
        descriptor = MaxPool2DDescriptor(uuid.uuid4())
        if self.__two_pool_size_values:
            descriptor.pool_size = tuple((self.__pool_size_one, self.__pool_size_two))
        else:
            descriptor.pool_size = self.__pool_size_one
        return descriptor


