import uuid

from common.models.component_descriptors.neural_networks.keras_layers.ld_CenterCrop import CenterCropDescriptor
from gui.viewmodels.nodeviewmodels.neuronalnetworks.layerviewmodelbase import LayerViewModelBase


class CenterCropLayerViewModel(LayerViewModelBase):
    def __init__(self, parent, descriptor):
        super().__init__(parent, descriptor)
        self.__width  = 0
        self.__height = 0

    @property
    def name(self):
        return 'Center Crop'

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if value == self.__height:
            return
        self.__height = value
        self._notify_property_changed('height', str(self.__height))

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if value == self.__width:
            return
        self.__width = value
        self._notify_property_changed('width', str(self.__width))

    @property
    def layer_descriptor(self):
        descriptor = CenterCropDescriptor(uuid.uuid4())
        descriptor.height = self.__height
        descriptor.width= self.__width

        return descriptor
