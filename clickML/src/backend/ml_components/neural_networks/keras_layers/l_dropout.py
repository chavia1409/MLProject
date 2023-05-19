from __future__ import annotations

import copy

from typing import Union, TYPE_CHECKING

from backend.ml_components.ml_layer_component import MLLayerComponent
from common.models.component_descriptors.component_constants import DEFAULT
from common.exceptions.click_ml_exceptions import SpecificationError, RequiredArgumentError
from backend.component_enum import Components

if TYPE_CHECKING:
    from common.models.component_descriptors.neural_networks.keras_layers.ld_dropout import DropoutDescriptor


class Dropout(MLLayerComponent):
    """
    Dropout layer.

    Attributes:

        # parameters for Dropout()
        rate: Union[float, str]
            (required) fraction of input units to drop, should be float
        seed: Union[int, str]
            (optional) random seed, should be int
    """

    def __init__(self, descriptor: DropoutDescriptor) -> None:
        des = copy.deepcopy(descriptor)
        super().__init__(des.component_id)

        # parameters for Dropout()
        self.rate: Union[float, str] = des.rate
        self.seed: Union[int, str] = des.seed

    @property
    def __parameters_dropout(self) -> str:
        param_dict = {"rate": self.rate, "seed": self.seed}
        return self.toolkit.create_param_string(param_dict)

    def to_code(self) -> str:
        return f"Dropout({self.__parameters_dropout})"

    @staticmethod
    def get_needed_imports() -> list[str]:
        return ["from keras.layers import Dropout"]

    def check_if_valid(self) -> None:
        self.__check_required_arguments()
        self.__check_domain_validity()

    def __check_domain_validity(self) -> None:
        if not (self.rate != DEFAULT or 0 <= self.rate <= 1):
            raise SpecificationError("rate", self.rate, "SequentialModel >> " + Dropout.__name__,
                                     "Must be float between 0 and 1!")
        if isinstance(self.seed, str) and self.seed != DEFAULT:
            raise SpecificationError("seed", self.seed, "SequentialModel >> " + Dropout.__name__, "Must be int!")

    def __check_required_arguments(self) -> None:
        if self.rate == DEFAULT:
            raise RequiredArgumentError("rate", Dropout.__name__)

    def set_output_shape(self, output_shape: str) -> bool:
        return False

    def type(self) -> Components:
        return Components.DROPOUT
