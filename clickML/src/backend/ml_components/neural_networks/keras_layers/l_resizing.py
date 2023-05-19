from __future__ import annotations

import copy


from backend.ml_components.ml_layer_component import MLLayerComponent
from common.models.component_descriptors.component_constants import DEFAULT
from common.exceptions.click_ml_exceptions import SpecificationError, RequiredArgumentError, ComponentCompositionError
from common.models.component_descriptors.component_constants import KERAS_LAYERS_POL
from typing import Union, TYPE_CHECKING
import uuid
from backend.component_enum import Components

if TYPE_CHECKING:
    from common.models.component_descriptors.neural_networks.keras_layers.ld_resizing import ResizingDescriptor


class ResizingLayer(MLLayerComponent):
    def __init__(self, descriptor: ResizingDescriptor) -> None:
        des = copy.deepcopy(descriptor)
        super().__init__(descriptor.component_id)

        self.__height: Union[int,str] = des.height
        self.__width: Union[int,str] = des.width
        self.__interpolation: str = des.interpolation
        self.__crop_to_aspect_ratio: Union[bool, str] = des.crop_to_aspect_ratio

    @property
    def height(self) -> Union[int,str]:
        return self.__height

    @height.setter
    def height(self, value: int):
        if isinstance(value, int) and 0 < value:
            self.__height = value
        else:
            raise SpecificationError("height", value, "resizing")

    @property
    def width(self) -> Union[int,str]:
        return self.__width

    @width.setter
    def width(self, value: int):
        if isinstance(value, int) and 0 < value:
            self.__width = value
        else:
            raise SpecificationError("width", value, "resizing")

    @property
    def interpolation(self) -> str:
        return self.__interpolation

    @interpolation.setter
    def interpolation(self, value: str):
        if value in KERAS_LAYERS_POL:
            self.__interpolation = value
        else:
            raise SpecificationError("interpolation", value, "resizing")

    @property
    def crop_to_aspect_ratio(self) -> bool:
        return self.__crop_to_aspect_ratio

    @crop_to_aspect_ratio.setter
    def crop_to_aspect_ratio(self, value: bool) -> None:
        if isinstance(value, bool):
            self.__crop_to_aspect_ratio = value
        else:
            raise SpecificationError("crop_to_aspect_ratio", value, "resizing")

    @property
    def __parameters_resizing(self) -> str:
        param_dict = {"height": self.height, "width": self.width}
        if self.interpolation != DEFAULT:
            param_dict.update({"interpolation": self.interpolation})
        if self.crop_to_aspect_ratio != DEFAULT:
            param_dict.update({"crop_to_aspect_ratio": self.crop_to_aspect_ratio})
        return self.toolkit.create_param_string(param_dict)

    def to_code(self) -> str:
        return f"resizing({self.__parameters_resizing})"

    @staticmethod
    def get_needed_imports() -> list[str]:
        return ["from keras.layers import Resizing"]

    def check_if_valid(self) -> bool:
        # checking if required arguments are set
        if self.height == DEFAULT:
            raise RequiredArgumentError("height", "resizing")
        if self.width == DEFAULT:
            raise RequiredArgumentError("width", "resizing")
        return True

    def type(self) -> Components:
        return Components.RESIZING

    def set_output_shape(self, output_shape: str) -> bool:
        return False
