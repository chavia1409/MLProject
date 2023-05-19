from __future__ import annotations

import copy

from backend.ml_components.ml_layer_component import MLLayerComponent
from common.models.component_descriptors.component_constants import DEFAULT
from common.exceptions.click_ml_exceptions import SpecificationError, RequiredArgumentError
from typing import Union, TYPE_CHECKING
from backend.component_enum import Components

if TYPE_CHECKING:
    from common.models.component_descriptors.neural_networks.keras_layers.ld_rescaling import RescalingDescriptor


class RescalingLayer(MLLayerComponent):
    def __init__(self, descriptor: RescalingDescriptor) -> None:
        des = copy.deepcopy(descriptor)
        super().__init__(descriptor.component_id)

        self.__scale: Union[float,str] = des.scale
        self.__offset: Union[float,str] = des.offset

    @property
    def scale(self) -> Union[float,str]:
        return self.__scale

    @scale.setter
    def scale(self, value: float):
        if isinstance(value, float) and 0.0 < value:
            self.__scale = value
        else:
            raise SpecificationError("scale", value, "RescalingLayer")

    @property
    def offset(self) -> Union[float,str]:
        return self.__offset

    @offset.setter
    def offset(self, value: float):
        if isinstance(value, float) and 0.0 < value:
            self.__offset = value
        else:
            raise SpecificationError("offset", value, "RescalingLayer")

    @property
    def __parameters_rescaling(self) -> str:
        param_dict = {"scale": self.scale, "offset": self.offset}
        return self.toolkit.create_param_string(param_dict)

    def to_code(self) -> str:
        return f"Rescaling({self.__parameters_rescaling})"

    @staticmethod
    def get_needed_imports() -> list[str]:
        return ["from keras.layers import Rescaling"]

    def check_if_valid(self) -> bool:
        # checking if required arguments are set
        """if self.scale == DEFAULT:
            raise RequiredArgumentError("scale", "Rescaling")
        if self.offset == DEFAULT:
            raise RequiredArgumentError("offset", "Rescaling")"""
        return True

    def type(self) -> Components:
        return Components.RESCALING

    def set_output_shape(self, output_shape: str) -> bool:
        return False
