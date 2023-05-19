import uuid
from dataclasses import dataclass
from typing import Union

from backend.ml_components.ml_layer_component import MLLayerComponent
from backend.ml_components.neural_networks.keras_layers.l_flatten import Flatten
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.ml_layer_component_descriptor import MLLayerComponentDescriptor


@dataclass
class FlattenDescriptor(MLLayerComponentDescriptor):
    """
    Attributes for the Flatten Layer Descriptor

    data_format: Union["channel_last", "channel_first"]
        (optional) A string, one of channels_last (default) or channels_first.
        The ordering of the dimensions in the inputs. It defaults to "channels_last".

    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        self.data_format: Union["channel_last", "channel_first"] = DEFAULT

    # attributes for pre- and successor
    pre: Union[type(uuid), str] = DEFAULT
    suc: Union[type(uuid), str] = DEFAULT

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return Flatten.__name__

    def restore_layer(self) -> MLLayerComponent:
        return Flatten(self)
