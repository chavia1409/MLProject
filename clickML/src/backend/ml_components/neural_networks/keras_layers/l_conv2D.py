from __future__ import annotations

import copy

from backend.ml_components.ml_layer_component import MLLayerComponent
from common.models.component_descriptors.component_constants import DEFAULT
from common.exceptions.click_ml_exceptions import SpecificationError, RequiredArgumentError
from common.models.component_descriptors.component_constants import KERAS_LAYERS_ACTIVATIONS
from backend.component_enum import Components

from typing import Union, TYPE_CHECKING, Any
import tensorflow as tf
import keras
from keras import activations

if TYPE_CHECKING:
    from common.models.component_descriptors.neural_networks.keras_layers.ld_conv2D import conv2D_Descriptor

"constructor mit Beschreibung der Parameter"


class conv2D_Layer(MLLayerComponent):
    def __init__(self, descriptor: conv2D_Descriptor) -> None:
        descriptor = copy.deepcopy(descriptor)
        super().__init__(descriptor.component_id)

        # params for conv2D_Layer()
        self.filters = descriptor.filters
        self.kernel_size = descriptor.kernel_size
        self.activation = descriptor.activation
        self.input_shape = descriptor.input_shape
        self.padding = descriptor.padding
        self.strides = descriptor.strides
        self.dilation_rate = descriptor.dilation_rate
        self.data_format = descriptor.data_format
        self.groups = descriptor.groups

    "getter & setter für die params"

    @property
    def filters(self) -> Union[int, str]:
        return self.__filters

    @filters.setter
    def filters(self, value: int):
        if isinstance(value, int) and 0 < value:
            self.__filters = value
        else:
            raise SpecificationError("filters", value, "conv2D")

    @property
    def kernel_size(self) -> Union[int, tuple[int, int], str]:
        return self.__kernel_size

    @kernel_size.setter
    def kernel_size(self, value: Union[int, tuple[int, int]]):
        if isinstance(value, int) or isinstance(value, tuple):
            self.__kernel_size = value
        else:
            raise SpecificationError("kernel_size", value, "conv2D")

    @property
    def activation(self) -> Union[keras.activations, str]:
        return self.__activation

    @activation.setter
    def activation(self, value: Union[keras.activations,DEFAULT]):
        if value in KERAS_LAYERS_ACTIVATIONS:
            self.__activation = value
        elif value == DEFAULT:
            self.__activation = value
        else:
            raise SpecificationError("activation", value, "conv2D")

    @property
    def input_shape(self) -> Union[tf.Tensor, str]:
        return self.__input_shape

    @input_shape.setter
    def input_shape(self, value: Union[tf.Tensor, DEFAULT]):
        if isinstance(value, tf.Tensor):
            self.__input_shape = value
        elif value == DEFAULT:
            self.__input_shape = value
        else:
            raise SpecificationError("input_shape", value, "conv2D")

    @property
    def padding(self) -> str:
        return self.__padding

    @padding.setter
    def padding(self, value: Union[str,DEFAULT]):
        if value == "valid" or "same":
            self.__padding = value
        elif value == DEFAULT:
            self.__padding = value
        else:
            raise SpecificationError("padding", value, "conv2D")

    @property
    def strides(self) -> Union[int, tuple[int, int], str]:
        return self.__strides

    @strides.setter
    def strides(self, value: Union[int, list[int, int], DEFAULT]):
        if isinstance(value, int) or isinstance(value, tuple):
            if value != 1 and self.dilation_rate != 1:
                raise SpecificationError("strides", value, "conv2D")
            else:
                self.__strides = value
        elif value == DEFAULT:
            self.__strides = value
        else:
            raise SpecificationError("strides", value, "conv2D")

    @property
    def dilation_rate(self) -> Union[int, tuple[int, int], str]:
        return self.__dilation_rate

    @dilation_rate.setter
    def dilation_rate(self, value: Union[int, tuple[int, int], DEFAULT]):
        if isinstance(value, int) or isinstance(value, tuple):
            if value != 1 and self.strides != 1:
                raise SpecificationError("dilation_rate", value, "conv2D")
            else:
                self.__dilation_rate = value
        elif value == DEFAULT:
            self.__dilation_rate = value
        else:
            raise SpecificationError("dilation_rate", value, "conv2D")

    @property
    def data_format(self) -> str:
        return self.__data_format

    @data_format.setter
    def data_format(self, value: Union[str, DEFAULT]):
        if value == "channel_first" or "channel_last":
            self.__data_format = value
        elif value == DEFAULT:
            self.__data_format = value
        else:
            raise SpecificationError("data_format", value, "conv2D")

    @property
    def groups(self) -> Union[int, str]:
        return self.__groups

    @groups.setter
    def groups(self, value: Union[int, DEFAULT]):
        if isinstance(value, int) and value > 0:
            self.__groups = value
        elif value == DEFAULT:
            self.__groups = value
        else:
            raise SpecificationError("groups", value, "conv2D")

    @staticmethod
    def get_needed_imports() -> list[str]:
        return ["from keras.layers import Conv2D"]

    @property
    def parameters_conv2D(self) -> str:
        param_dict = self.check_param()
        return self.toolkit.create_param_string(param_dict)

    def check_param(self) -> dict[str, Any]:
        param_dict = {"filters": self.filters, "kernel_size": self.kernel_size}
        if self.activation != DEFAULT:
            param_dict.update({"activation": self.activation})
        if self.input_shape != DEFAULT:
            param_dict.update({"input_shape": self.input_shape})
        if self.padding != DEFAULT:
            param_dict.update({"padding": self.padding})
        if self.strides != DEFAULT:
            param_dict.update({"strides": self.strides})
        if self.dilation_rate != DEFAULT:
            param_dict.update({"dilation_rate": self.dilation_rate})
        if self.data_format != DEFAULT:
            param_dict.update({"data_format": self.data_format})
        if self.groups != DEFAULT:
            param_dict.update({"groups": self.groups})
        return param_dict

    def to_code(self) -> str:
        return f"Conv2D({self.parameters_conv2D})"

    def check_if_valid(self) -> bool:
        if self.filters == DEFAULT:
            raise RequiredArgumentError("filters", "conv2D")
        elif self.kernel_size == DEFAULT:
            raise RequiredArgumentError("kernel_size", "conv2D")
        else:
            return True

    def type(self) -> Components:
        return Components.CONV2D

    def set_output_shape(self, output_shape: str) -> bool:
        return False
