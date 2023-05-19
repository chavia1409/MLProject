from __future__ import annotations

import copy

from typing import Union, TYPE_CHECKING

from backend.ml_components.ml_layer_component import MLLayerComponent
from common.models.component_descriptors.component_constants \
    import DEFAULT, KERAS_LAYERS_ACTIVATIONS, KERAS_LAYERS_INITIALIZERS, KERAS_LAYERS_REGULARIZERS, \
    KERAS_LAYERS_CONSTRAINTS
from common.exceptions.click_ml_exceptions import SpecificationError, RequiredArgumentError, ComponentCompositionError
from backend.component_enum import Components

if TYPE_CHECKING:
    from common.models.component_descriptors.neural_networks.keras_layers.ld_dense import DenseDescriptor


class Dense(MLLayerComponent):
    """
    Dense layer.

    Attributes:
        # parameters for Dense()
        units: Union[int, str]
            (required) dimensionality of the output space, should be int
        activation: str
            (optional) activation function
        use_bias: Union[bool, str]
            (optional) bool, whether the layer uses bias vector, should be bool
        kernel_initializer: str
            (optional) init for kernel weights matrix
        bias_initializer: str
            (optional) init for bias vector
        kernel_regularizer: str
            (optional) weight regularizer
        bias_regularizer: str
            (optional) kernel bias weight regularizer
        activity_regularizer: str
            (optional) activity weight regularizer
        kernel_constraint: str
            (optional) kernel constraint
        bias_constraint: str
            (optional) bias constraint

        # preprocessing
        output_shape: str
            code snippet that can be used for specifying the output shape for sequential model
    """

    def __init__(self, descriptor: DenseDescriptor) -> None:
        des = copy.deepcopy(descriptor)
        super().__init__(des.component_id)

        # parameters for Dense()
        self.units: Union[int, str] = des.units
        self.activation: str = des.activation
        self.use_bias: Union[bool, str] = des.use_bias
        self.kernel_initializer: str = des.kernel_initializer
        self.bias_initializer: str = des.bias_initializer
        self.kernel_regularizer: str = des.kernel_regularizer
        self.bias_regularizer: str = des.bias_regularizer
        self.activity_regularizer: str = des.activity_regularizer
        self.kernel_constraint: str = des.kernel_constraint
        self.bias_constraint: str = des.bias_constraint

        # preprocessing
        self.output_shape: str = DEFAULT

    @property
    def __parameters_dense(self) -> str:
        param_dict = {"units": self.units if self.output_shape == DEFAULT else self.output_shape,
                      "activation": self.activation, "use_bias": self.use_bias,
                      "kernel_initializer": self.kernel_initializer, "bias_initializer": self.bias_initializer,
                      "kernel_regularizer": self.kernel_regularizer, "bias_regularizer": self.bias_regularizer,
                      "activity_regularizer": self.activity_regularizer, "kernel_constraint": self.kernel_constraint,
                      "bias_constraint": self.bias_constraint}
        return self.toolkit.create_param_string(param_dict, no_repr=("units",))

    def to_code(self) -> str:
        return f"Dense({self.__parameters_dense})"

    @staticmethod
    def get_needed_imports() -> list[str]:
        return ["from keras.layers import Dense"]

    def set_output_shape(self, output_shape: str) -> bool:
        self.output_shape = output_shape
        return True

    def check_if_valid(self) -> None:
        self.__check_required_arguments()
        self.__check_domain_validity()
        #self.__check_component_composition()

    def __check_domain_validity(self) -> None:
        if not (self.units == DEFAULT or (isinstance(self.units, int) and self.units > 0)):
            raise SpecificationError("units", self.units, "SequentialModel >> " + Dense.__name__,
                                     "Must be int > 0!")
        if not (self.activation in KERAS_LAYERS_ACTIVATIONS or self.activation == DEFAULT):
            raise SpecificationError("activation", self.activation, "SequentialModel >> " + Dense.__name__,
                                     "Not a valid activation function!")
        if isinstance(self.use_bias, str) and self.use_bias != DEFAULT:
            raise SpecificationError("use_bias", self.use_bias, "SequentialModel >> " + Dense.__name__, "Must be bool!")
        if not (self.kernel_initializer in KERAS_LAYERS_INITIALIZERS or self.kernel_initializer == DEFAULT):
            raise SpecificationError("kernel_initializer", self.kernel_initializer,
                                     "SequentialModel >> " + Dense.__name__, "Initializer does not exist!")
        if not (self.bias_initializer in KERAS_LAYERS_INITIALIZERS or self.bias_initializer == DEFAULT):
            raise SpecificationError("bias_initializer", self.bias_initializer, "SequentialModel >> " + Dense.__name__,
                                     "Initializer does not exist!")
        if not (self.kernel_regularizer in KERAS_LAYERS_REGULARIZERS or self.kernel_regularizer == DEFAULT):
            raise SpecificationError("kernel_regularizer", self.kernel_regularizer,
                                     "SequentialModel >> " + Dense.__name__, "Regularizer does not exist!")
        if not (self.bias_regularizer in KERAS_LAYERS_REGULARIZERS or self.bias_regularizer == DEFAULT):
            raise SpecificationError("bias_regularizer", self.bias_regularizer, "SequentialModel >> " + Dense.__name__,
                                     "Regularizer does not exist!")
        if not (self.activity_regularizer in KERAS_LAYERS_REGULARIZERS or self.activity_regularizer == DEFAULT):
            raise SpecificationError("activity_regularizer", self.activity_regularizer,
                                     "SequentialModel >> " + Dense.__name__, "Regularizer does not exist!")
        if not (self.kernel_constraint in KERAS_LAYERS_CONSTRAINTS or self.kernel_constraint == DEFAULT):
            raise SpecificationError("kernel_constraint", self.kernel_constraint,
                                     "SequentialModel >> " + Dense.__name__, "Constraint does not exist!")
        if not (self.bias_constraint in KERAS_LAYERS_CONSTRAINTS or self.bias_constraint == DEFAULT):
            raise SpecificationError("bias_constraint", self.bias_constraint, "SequentialModel >> " + Dense.__name__,
                                     "Constraint does not exist!")

    def __check_required_arguments(self) -> None:
        if self.units == DEFAULT and self.output_shape == DEFAULT:
            raise RequiredArgumentError("units", Dense.__name__)

    def __check_component_composition(self) -> None:
        if self.units != DEFAULT and self.output_shape != DEFAULT:
            raise ComponentCompositionError(Dense.__name__, "Units should not be set if output shape is provided.")

    def type(self) -> Components:
        return Components.DENSE
