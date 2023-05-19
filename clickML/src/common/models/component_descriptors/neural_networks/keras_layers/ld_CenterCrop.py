import uuid
from dataclasses import dataclass
from typing import Union

from backend.ml_components.neural_networks.keras_layers.l_CenterCrop import CenterCrop
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.ml_layer_component_descriptor import MLLayerComponentDescriptor


@dataclass
class CenterCropDescriptor(MLLayerComponentDescriptor):
    """
        # Attributes for the Descriptor of the Center Crop Layer

        height: Union[int, str]
            (required)  Integer, the height of the output shape

        width: Union[int, tuple[int, int], str]
            (required) Integer, the width of the output shape.
        """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        self.height: Union[int, str] = DEFAULT
        self.width: Union[int, str] = DEFAULT

    # attributes for possible predecessors and successors
    pre: Union[type(uuid), str] = DEFAULT
    suc: Union[type(uuid), str] = DEFAULT

    # required parameters for conv2D constructor

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return CenterCrop.__name__

    def restore_layer(self) -> CenterCrop:
        return CenterCrop(self)
