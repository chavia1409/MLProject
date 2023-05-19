from __future__ import annotations

import copy

from backend.ml_components.ml_layer_component import MLLayerComponent
from common.models.component_descriptors.component_constants import DEFAULT
from common.exceptions.click_ml_exceptions import SpecificationError, RequiredArgumentError
from typing import Union, TYPE_CHECKING
from backend.component_enum import Components

if TYPE_CHECKING:
    from common.models.component_descriptors.neural_networks.keras_layers.ld_CenterCrop import CenterCropDescriptor


class CenterCrop(MLLayerComponent):
    def __init__(self, descriptor: CenterCropDescriptor) -> None:
        des = copy.deepcopy(descriptor)
        super().__init__(descriptor.component_id)

        self.__height: Union[int,str] = des.height
        self.__width: Union[int,str] = des.width

    @property
    def height(self) -> Union[int, str]:
        return self.__height

    @height.setter
    def height(self, value: int):
        if isinstance(value, int) and 0 < value:
            self.__height = value
        else:
            raise SpecificationError("height", value, "CenterCrop")

    @property
    def width(self) -> Union[int, str]:
        return self.__width

    @width.setter
    def width(self, value: int):
        if isinstance(value, int) and 0 < value:
            self.__width = value
        else:
            raise SpecificationError("width", value, "CenterCrop")

    @property
    def __parameters_CenterCrop(self) -> str:
        param_dict = {"height": self.height, "width": self.width}
        return self.toolkit.create_param_string(param_dict)

    def to_code(self) -> str:
        return f"CenterCrop({self.__parameters_CenterCrop})"

    @staticmethod
    def get_needed_imports() -> list[str]:
        return ["from keras.layers import CenterCrop"]

    def check_if_valid(self) -> bool:
        # checking if required arguments are set
        if self.height == DEFAULT:
            raise RequiredArgumentError("height", "CenterCrop")
        if self.width == DEFAULT:
            raise RequiredArgumentError("width", "CenterCrop")
        return True

    def type(self) -> Components:
        return Components.CENTERCROP

    def set_output_shape(self):
        pass
