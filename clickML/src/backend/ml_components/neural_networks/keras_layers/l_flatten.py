from __future__ import annotations

import copy

from backend.component_enum import Components
from backend.ml_components.ml_layer_component import MLLayerComponent
from common.models.component_descriptors.component_constants import DEFAULT
from common.exceptions.click_ml_exceptions import SpecificationError, RequiredArgumentError, ComponentCompositionError
from typing import Union, TYPE_CHECKING



if TYPE_CHECKING:
    from common.models.component_descriptors.neural_networks.keras_layers.ld_flatten import FlattenDescriptor

class Flatten(MLLayerComponent):
    def __init__(self, descriptor: FlattenDescriptor) -> None:
        des = copy.deepcopy(descriptor)
        super().__init__(descriptor.component_id)

        # parameters for Flatten()
        self.__data_format: str = DEFAULT   #optional

    @property
    def data_format(self) -> str:
        return self.__data_format

    @data_format.setter
    def data_format(self, value: str):
        if value == "channel_last" or "channel_first":
            self.__data_format = value
        else:
            raise SpecificationError("Input not valid for 'data_format', must be 'channel_last' or 'channel_first'")

    def check_if_valid(self) -> bool:
        if self.data_format == "channel_last" or "channel_first":
            return True

    @staticmethod
    def get_needed_imports() -> list[str]:
        return ["from keras.layers import Flatten"]

    @property
    def __parameters_flatten(self) -> str:
        param_dict = {"data_format": self.__data_format}
        return self.toolkit.create_param_string(param_dict)

    def to_code(self) -> str:
        return f"Flatten({self.__parameters_flatten})"

    def type(self) -> Components:
        return Components.FLATTEN

    def set_output_shape(self, output_shape: str) -> bool:
        return False
