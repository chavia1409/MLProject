import uuid
from typing import Union

from backend.ml_components.neural_networks.keras_layers.l_dropout import Dropout
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.ml_layer_component_descriptor import MLLayerComponentDescriptor


class DropoutDescriptor(MLLayerComponentDescriptor):
    """
    Descriptor for Dropout layer.

    Attributes:

        # parameters for Dropout()
        rate: Union[float, str]
            (required) fraction of input units to drop, should be float
        seed: Union[int, str]
            (optional) random seed, should be int
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        # parameters for Dropout()
        self.rate: Union[float, str] = DEFAULT
        self.seed: Union[int, str] = DEFAULT

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return Dropout.__name__

    def restore_layer(self) -> Dropout:
        return Dropout(self)
