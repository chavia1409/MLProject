import uuid

from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.neural_networks.keras_layers.ld_conv2D import conv2D_Descriptor
from gui.viewmodels.nodeviewmodels.neuronalnetworks.layerviewmodelbase import LayerViewModelBase


class Conv2DLayerViewModel(LayerViewModelBase):
    def __init__(self, parent, descriptor):
        super().__init__(parent, descriptor)
        self.__filters = 0
        if descriptor.filters is not DEFAULT:
            self.__filters = descriptor.filters
        self.__two_kernel_size_values = isinstance(descriptor.kernel_size, tuple)
        self.__kernel_size_one = 0
        self.__kernel_size_two = 0
        if self.__two_kernel_size_values:
            self.__kernel_size_one = descriptor.kernel_size[0]
            self.__kernel_size_two = descriptor.kernel_size[1]
        if isinstance(descriptor.kernel_size, int):
            self.__kernel_size_one = descriptor.kernel_size
            self.__kernel_size_two = descriptor.kernel_size

    @property
    def filters(self):
        return str(self.__filters)

    @filters.setter
    def filters(self, value):
        if value == '':
            self.__filters = 0
            self._notify_property_changed('filters', str(self.__filters))
            return
        try:
            value = int(value)
        except ValueError:
            self._notify_property_changed('filters', str(self.__filters))
            return
        if value == self.__filters:
            return
        self.__filters = value
        self._notify_property_changed('filters', str(value))

    @property
    def two_kernel_size_values(self):
        return self.__two_kernel_size_values

    @two_kernel_size_values.setter
    def two_kernel_size_values(self, value):
        if value == self.__two_kernel_size_values:
            return
        self.__two_kernel_size_values = value
        self._notify_property_changed('two_kernel_size_values', value)

    @property
    def kernel_size_one(self):
        return str(self.__kernel_size_one)


    @kernel_size_one.setter
    def kernel_size_one(self, value):
        if value == '':
            self.__kernel_size_one = 0
            self._notify_property_changed('kernel_size_one', str(self.__kernel_size_one))
            return
        try:
            value = int(value)
        except ValueError:
            self._notify_property_changed('kernel_size_one', str(self.__kernel_size_one))
            return
        if value == self.__kernel_size_one:
            return

        self.__kernel_size_one = value
        self._notify_property_changed('kernel_size_one', str(value))
        if not self.__two_kernel_size_values:
            self.kernel_size_two = str(value)

    @property
    def kernel_size_two(self):
        return str(self.__kernel_size_two)

    @kernel_size_two.setter
    def kernel_size_two(self, value):
        if value == '':
            self.__kernel_size_two = 0
            self._notify_property_changed('kernel_size_two', str(self.__kernel_size_two))
            return
        try:
            value = int(value)
        except ValueError:
            self._notify_property_changed('kernel_size_two', str(self.__kernel_size_two))
            return
        if value == self.__kernel_size_two:
            return

        self.__kernel_size_two = value
        self._notify_property_changed('kernel_size_two', str(value))
        if not self.__two_kernel_size_values:
            self.kernel_size_one = str(value)

    @property
    def name(self):
        return 'Conv2D'

    @property
    def layer_descriptor(self):
        descriptor = conv2D_Descriptor(uuid.uuid4())
        descriptor.filters = self.__filters
        if self.__two_kernel_size_values:
            descriptor.kernel_size = tuple((self.__kernel_size_one, self.__kernel_size_two))
        else:
            descriptor.kernel_size = self.__kernel_size_one
        return descriptor