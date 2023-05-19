import uuid
from dataclasses import dataclass
from typing import Union

from backend.ml_components.neural_networks.keras_layers.l_CenterCrop import CenterCrop
from backend.ml_components.neural_networks.keras_layers.l_rescaling import RescalingLayer
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.ml_layer_component_descriptor import MLLayerComponentDescriptor

@dataclass

class RescalingDescriptor(MLLayerComponentDescriptor):
    """
            # Attributes for the Descriptor of the Resizing

            scale: Union[float, str]
                (required)  Integer, the height of the output shape

            offset: Union[float, str]
                (required) Integer, the width of the output shape.
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        self.scale: Union[float, str] = DEFAULT
        self.offset: Union[float, str] = DEFAULT

    pre: Union[type(uuid), str] = DEFAULT
    suc: Union[type(uuid), str] = DEFAULT

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return RescalingLayer.__name__

    def restore_layer(self) -> CenterCrop:
        return RescalingLayer(self)