import uuid
from dataclasses import dataclass
from typing import Union

from backend.ml_components.neural_networks.keras_layers.l_conv2D import conv2D_Layer
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.ml_layer_component_descriptor import MLLayerComponentDescriptor


import tensorflow as tf
import keras
from keras import activations

@dataclass
class conv2D_Descriptor(MLLayerComponentDescriptor):
    """
    # Attributes for the Descriptor of the Convolutional 2D Layer

    filters: Union[int, str]
        (required) integer, the dimensionality of the output space

    kernel_size: Union[int, tuple[int, int], str]
        (required) an integer or tuple/list of 2 integers, specifying the height and width of the 2D convolution window. Can be a single integer to specify the same value for all spatial dimensions.

    activation: Union[keras.activations, str]
        (optional) an activation function to use

    input_shape: Union[tf.Tensor, str]
        (optional) defines the input_shape, 4+D tensor, shape depending on data_format

    padding: str
        (optional) can be "valid" or "same". "same" and strides = 1 results in an output_size = input_size and padds the blank spaces with zeroes

    strides: Union[int, tuple[int, int], str]
        (optional) an integer or tuple/list of 2 integers, specifying the strides of the convolution along the height and width. Can be a single integer to specify the same value for all spatial dimensions

    dilation_rate: Union[int, tuple[int, int], str]
        (optional) an integer or tuple/list of 2 integers, specifying the dilation rate to use for dilated convolution. Can be a single integer to specify the same value for all spatial dimensions.

    data_format: str
        (optional) a string, one of channels_last (default) or channels_first. The ordering of the dimensions in the inputs. channels_last corresponds to inputs with shape (batch_size, height, width, channels) while channels_first corresponds to inputs with shape (batch_size, channels, height, width).

    groups: Union[int, str]
        (optional) a positive integer specifying the number of groups in which the input is split along the channel axis. Each group is convolved separately with filters / groups filters. The output is the concatenation of all the groups results along the channel axis.
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id
        # required parameters for conv2D constructor
        self.filters: Union[int, str] = DEFAULT
        self.kernel_size: Union[int, tuple[
            int, int], str] = DEFAULT

        # optional parameters for conv2D constructor
        self.activation: Union[keras.activations, str] = DEFAULT
        self.input_shape: Union[tf.Tensor, str] = DEFAULT
        self.padding: str = DEFAULT
        self.strides: Union[int, tuple[int, int], str] = DEFAULT
        self.dilation_rate: Union[int, tuple[int, int], str] = DEFAULT
        self.data_format: str = DEFAULT
        self.groups: Union[int, str] = DEFAULT

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return conv2D_Layer.__name__

    def restore_layer(self) -> conv2D_Layer:
        return conv2D_Layer(self)
