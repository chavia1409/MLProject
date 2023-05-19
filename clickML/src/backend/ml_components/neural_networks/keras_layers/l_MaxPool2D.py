from __future__ import annotations

import copy

from backend.ml_components.ml_layer_component import MLLayerComponent
from common.exceptions.click_ml_exceptions import SpecificationError, RequiredArgumentError
from common.models.component_descriptors.component_constants import DEFAULT
from typing import Union, TYPE_CHECKING
from backend.component_enum import Components

if TYPE_CHECKING:
    from common.models.component_descriptors.neural_networks.keras_layers.ld_MaxPool2D import MaxPool2DDescriptor


class MaxPool2DLayerComponent(MLLayerComponent):
    def __init__(self, descriptor: MaxPool2DDescriptor) -> None:
        descriptor = copy.deepcopy(descriptor)
        super().__init__(descriptor.component_id)

        # parameters for MaxPool2D()
        self.__pool_size = descriptor.pool_size  # required
        self.__strides = descriptor.strides  # optional
        self.__padding = descriptor.padding  # required
        self.__data_format = descriptor.data_format  # optional evtl channels_last

    # getter und setter
    @property
    def pool_size(self) -> Union[tuple[int, int], int]:
        return self.__pool_size

    @pool_size.setter
    def pool_size(self, value: Union[int, tuple[int, int]]):
        if isinstance(value, Union[int, tuple]):
            if value > 0:
                self.__pool_size = value
            else:
                raise SpecificationError("Value has to be >0")
        elif value == DEFAULT:
            self.__pool_size = (2, 2)
        else:
            raise SpecificationError("Input not valid for 'pool_size'")

    @property
    def strides(self) -> Union[tuple[int, int], int, DEFAULT]:
        return self.__strides

    @strides.setter
    def strides(self, value: Union[int, tuple[int, int], DEFAULT]):
        if isinstance(value, Union[int, tuple, DEFAULT]):
            if isinstance(value, DEFAULT):
                self.__strides = self.__pool_size
            elif value > 0:
                self.__strides = value
            else:
                raise SpecificationError("Value has to be > 0 or None")

        else:
            raise SpecificationError("Input not valid for 'strides'")

    @property
    def padding(self) -> str:
        return self.__padding

    @padding.setter
    def padding(self, value: Union[str, DEFAULT]):
        if value == "valid" or "same":
            self.__padding = value
        elif value == DEFAULT:
            self.__padding = 'valid'
        else:
            raise SpecificationError("Input not valid for 'padding', must be 'valid' or 'same'")

    @property
    def data_format(self) -> str:
        return self.__data_format

    @data_format.setter
    def data_format(self, value: str):
        if value == "channel_last" or "channel_first":
            self.__data_format = value
        else:
            raise SpecificationError("Input not valid for 'padding', must be 'channel_last' or 'channel_first'")

    @staticmethod
    def get_needed_imports() -> list[str]:
        return ["from keras.layers import MaxPool2D"]

    @property
    def parameters_MaxPool2D(self) -> str:
        param_dict = {}
        if self.pool_size != DEFAULT:
            param_dict.update({"pool_size": self.__pool_size})
        if self.padding != DEFAULT:
            param_dict.update({"padding": self.__padding})
        if self.strides != DEFAULT:
            param_dict.update({"strides": self.__strides})
        if self.data_format != DEFAULT:
            param_dict.update({"data_format": self.__data_format})
        return self.toolkit.create_param_string(param_dict)

    def to_code(self) -> str:
        return f"MaxPool2D({self.parameters_MaxPool2D})"

    def check_if_valid(self) -> bool:
        return True

    def type(self) -> Components:
        return Components.MAXPOOL2D

    def set_output_shape(self, output_shape: str) -> bool:
        return False
