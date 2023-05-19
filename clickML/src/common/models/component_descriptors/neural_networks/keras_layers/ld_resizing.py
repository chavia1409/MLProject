import uuid
from dataclasses import dataclass
from typing import Union

from keras.layers import Resizing

from backend.ml_components.neural_networks.keras_layers.l_resizing import ResizingLayer
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.ml_layer_component_descriptor import MLLayerComponentDescriptor

@dataclass
class ResizingDescriptor(MLLayerComponentDescriptor):
    """
           # Attributes for the Descriptor of the Resizing

           height: Union[int, str]
               (required)  Integer, the height of the output shape

           width: Union[int, str]
               (required) Integer, the width of the output shape.

           interpolation: str
                defaults to "bilinear"

           crop_to_aspect_ration: Union[bool, str]
                defaults to False. If True, resize the images without aspect ratio distortion
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        self.height: Union[int, str] = DEFAULT
        self.width: Union[int, str] = DEFAULT
        self.interpolation: str = DEFAULT
        self.crop_to_aspect_ratio: Union[bool, str] = DEFAULT

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return Resizing.__name__

    def restore_layer(self) -> Resizing:
        return Resizing(self)