import uuid

from common.models.component_descriptors.neural_networks.keras_layers.ld_rescaling import RescalingDescriptor
from gui.viewmodels.nodeviewmodels.neuronalnetworks.layerviewmodelbase import LayerViewModelBase


class RescalingLayerViewModel(LayerViewModelBase):
    def __init__(self, parent, descriptor):
        super().__init__(parent, descriptor)
        self.__scale = 0
        self.__offset = 0

    @property
    def name(self):
        return 'Rescaling'

    @property
    def scale(self):
        return self.__scale
    @scale.setter
    def scale(self, value):
        if value == self.__scale:
            return
        self.__scale = value
        self._notify_property_changed('scale', str(self.__scale))

    @property
    def offset(self):
        return self.__offset
    @offset.setter
    def offset(self, value):
        if value == self.__offset:
            return
        self.__offset = value
        self._notify_property_changed('offset', str(self.__offset))

    @property
    def layer_descriptor(self):
        descriptor = RescalingDescriptor(uuid.uuid4())
        descriptor.scale = self.__scale
        descriptor.offset = self.__offset
        return descriptor