import uuid
from dataclasses import dataclass
from typing import Union

from backend.ml_components.ml_layer_component import MLLayerComponent
from backend.ml_components.neural_networks.keras_layers.l_MaxPool2D import MaxPool2DLayerComponent
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.ml_layer_component_descriptor import MLLayerComponentDescriptor

@dataclass
class MaxPool2DDescriptor(MLLayerComponentDescriptor):
    """
    # Attributes for the Descriptor of the MaxPooling 2D Layer

    pool_size: Union[int, tuple[int, int]
        (required) integer or tuple of 2 integers, window size over which to take the maximum.
        (2, 2) will take the max value over a 2x2 pooling window.
        If only one integer is specified, the same window length will be used for both dimensions

    strides: Union[int, tuple[int, int], None
        (optional) integer, tuple of 2 integers, or None.
        Specifies how far the pooling window moves for each pooling step.
        If None, it will default to pool_size

    padding: Union["valid", "same"]
        (required)One of "valid" or "same" (case-insensitive).
        "valid" means no padding. "same" results in padding evenly to the left/right
        or up/down of the input such that output has the same height/width dimension as the input.

    data_format: Union["channel_last", "channel_first"]
        (optional) A string, one of channels_last (default) or channels_first.
        The ordering of the dimensions in the inputs. It defaults to "channels_last".
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id
        # required parameters for MaxPool2D
        self.pool_size: Union[int, tuple[int, int]] = DEFAULT
        self.padding: Union["valid", "same"] = DEFAULT

        # optional parameters for MaxPool2D
        self.strides: Union[int, tuple[int, int], None] = DEFAULT
        self.data_format: Union["channel_last", "channel_first"] = DEFAULT

    # attributes for pre- and successor
    pre: Union[type(uuid), str] = DEFAULT
    suc: Union[type(uuid), str] = DEFAULT


    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return MaxPool2DLayerComponent.__name__

    def restore_layer(self) -> MLLayerComponent:
        return MaxPool2DLayerComponent(self)