from __future__ import annotations

import copy

from typing import Union, Optional, TYPE_CHECKING

from backend.ml_components.ml_layer_component import MLLayerComponent
from common.models.component_descriptors.component_constants \
    import DEFAULT, KERAS_LAYERS_ACTIVATIONS, KERAS_LAYERS_INITIALIZERS, KERAS_LAYERS_REGULARIZERS, \
    KERAS_LAYERS_CONSTRAINTS
from common.exceptions.click_ml_exceptions \
    import SpecificationError, RequiredArgumentError, ComponentCompositionError
from backend.component_enum import Components

if TYPE_CHECKING:
    from common.models.component_descriptors.neural_networks.keras_layers.ld_lstm import LSTMDescriptor


class LSTM(MLLayerComponent):
    """
    LSTM layer.

    Attributes:
        # parameters for LSTM()
        units: Union[int, str]
            (required) dimensionality of the output space, should be int
        activation: Optional[str]
            (optional) activation function
        recurrent_activation: Optional[str]
            (optional) activation function for recurrent step
        use_bias: Union[bool, str]
            (optional) bool, whether the layer uses bias vector, should be bool
        kernel_initializer: str
            (optional) init for kernel weights matrix
        recurrent_initializer: str
            (optional) init for recurrent_kernel weights matrix
        bias_initializer: str
            (optional) init for bias vector
        unit_forget_bias: Union[bool, str]
            (optional) if True, add 1 to bias of forget gate, should be bool
        dropout: Union[float, str]
            (optional) fraction of units to drop (input), should be float
        recurrent_dropout: Union[float, str]
            (optional) fraction of units to drop (recurrent state), should be float

        # preprocessing
        output_shape: str
            code snippet that can be used for specifying the output shape for sequential model
        return_sequences: str
            additional parameter for stacking multiple GRU and LSTM layers
    """

    def __init__(self, descriptor: LSTMDescriptor) -> None:
        des = copy.deepcopy(descriptor)
        super().__init__(des.component_id)

        # parameters for LSTM()
        self.units: Union[int, str] = des.units
        self.activation: Optional[str] = des.activation
        self.recurrent_activation: Optional[str] = des.recurrent_activation
        self.use_bias: Union[bool, str] = des.use_bias
        self.kernel_initializer: str = des.kernel_initializer
        self.recurrent_initializer: str = des.recurrent_initializer
        self.bias_initializer: str = des.bias_initializer
        self.unit_forget_bias: Union[float, str] = des.unit_forget_bias
        self.kernel_regularizer: str = des.kernel_regularizer
        self.recurrent_regularizer: str = des.recurrent_regularizer
        self.bias_regularizer: str = des.bias_regularizer
        self.activity_regularizer: str = des.activity_regularizer
        self.kernel_constraint: str = des.kernel_constraint
        self.recurrent_constraint: str = des.recurrent_constraint
        self.bias_constraint: str = des.bias_constraint
        self.dropout: Union[float, str] = des.dropout
        self.recurrent_dropout: Union[float, str] = des.recurrent_dropout

        # preprocessing
        self.output_shape: str = DEFAULT
        self.return_sequences: str = DEFAULT

    @property
    def __parameters_lstm(self) -> str:
        param_dict = {"units": self.units if self.output_shape == DEFAULT else self.output_shape,
                      "activation": self.activation, "recurrent_activation": self.recurrent_activation,
                      "use_bias": self.use_bias, "kernel_initializer": self.kernel_initializer,
                      "recurrent_initializer": self.recurrent_initializer, "bias_initializer": self.bias_initializer,
                      "unit_forget_bias": self.unit_forget_bias, "kernel_regularizer": self.kernel_regularizer,
                      "recurrent_regularizer": self.recurrent_regularizer, "bias_regularizer": self.bias_regularizer,
                      "activity_regularizer": self.activity_regularizer, "kernel_constraint": self.kernel_constraint,
                      "recurrent_constraint": self.recurrent_constraint, "bias_constraint": self.bias_constraint,
                      "dropout": self.dropout, "recurrent_dropout": self.recurrent_dropout,
                      "return_sequences": self.return_sequences}
        return self.toolkit.create_param_string(param_dict, no_repr=("units", "return_sequences"))

    def to_code(self) -> str:
        return f"LSTM({self.__parameters_lstm})"

    @staticmethod
    def get_needed_imports() -> list[str]:
        return ["from keras.layers import LSTM"]

    def set_output_shape(self, output_shape: str) -> bool:
        self.output_shape = output_shape
        return True

    def check_if_valid(self) -> None:
        self.__check_required_arguments()
        self.__check_domain_validity()
        self.__check_argument_composition()

    def __check_domain_validity(self) -> None:
        if not (self.units == DEFAULT or (isinstance(self.units, int) and self.units > 0)):
            raise SpecificationError("units", self.units, "SequentialModel >> " + LSTM.__name__, "Must be int > 0.")
        if not (self.activation in KERAS_LAYERS_ACTIVATIONS or self.activation == DEFAULT):
            raise SpecificationError("activation", self.activation, "SequentialModel >> " + LSTM.__name__,
                                     "Not a valid activation function!")
        if not (self.recurrent_activation in KERAS_LAYERS_ACTIVATIONS or self.recurrent_activation == DEFAULT):
            raise SpecificationError("recurrent_activation", self.recurrent_activation,
                                     "SequentialModel >> " + LSTM.__name__,
                                     "Not a valid recurrent activation function!")
        if isinstance(self.use_bias, str) and self.use_bias != DEFAULT:
            raise SpecificationError("use_bias", self.use_bias, "SequentialModel >> " + LSTM.__name__, "Must be bool!")
        if not (self.kernel_initializer in KERAS_LAYERS_INITIALIZERS or self.kernel_initializer == DEFAULT):
            raise SpecificationError("kernel_initializer", self.kernel_initializer,
                                     "SequentialModel >> " + LSTM.__name__, "Initializer does not exist!")
        if not (self.recurrent_initializer in KERAS_LAYERS_INITIALIZERS or self.recurrent_initializer == DEFAULT):
            raise SpecificationError("recurrent_initializer", self.recurrent_initializer,
                                     "SequentialModel >> " + LSTM.__name__, "Initializer does not exist!")
        if not (self.bias_initializer in KERAS_LAYERS_INITIALIZERS or self.bias_initializer == DEFAULT):
            raise SpecificationError("bias_initializer", self.bias_initializer, "SequentialModel >> " + LSTM.__name__,
                                     "Initializer does not exist!")
        if isinstance(self.unit_forget_bias, str) and self.unit_forget_bias != DEFAULT:
            raise SpecificationError("unit_forget_bias", self.unit_forget_bias, "SequentialModel >> " + LSTM.__name__,
                                     "Must be bool!")
        if not (self.kernel_regularizer in KERAS_LAYERS_REGULARIZERS or self.kernel_regularizer == DEFAULT):
            raise SpecificationError("kernel_regularizer", self.kernel_regularizer,
                                     "SequentialModel >> " + LSTM.__name__, "Regularizer does not exist!")
        if not (self.recurrent_regularizer in KERAS_LAYERS_REGULARIZERS or self.recurrent_regularizer == DEFAULT):
            raise SpecificationError("recurrent_regularizer", self.recurrent_regularizer,
                                     "SequentialModel >> " + LSTM.__name__, "Regularizer does not exist!")
        if not (self.bias_regularizer in KERAS_LAYERS_REGULARIZERS or self.bias_regularizer == DEFAULT):
            raise SpecificationError("bias_regularizer", self.bias_regularizer, "SequentialModel >> " + LSTM.__name__,
                                     "Regularizer does not exist!")
        if not (self.activity_regularizer in KERAS_LAYERS_REGULARIZERS or self.activity_regularizer == DEFAULT):
            raise SpecificationError("activity_regularizer", self.activity_regularizer,
                                     "SequentialModel >> " + LSTM.__name__, "Regularizer does not exist!")
        if not (self.kernel_constraint in KERAS_LAYERS_CONSTRAINTS or self.kernel_constraint == DEFAULT):
            raise SpecificationError("kernel_constraint", self.kernel_constraint, "SequentialModel >> " + LSTM.__name__,
                                     "Constraint does not exist!")
        if not (self.recurrent_constraint in KERAS_LAYERS_CONSTRAINTS or self.recurrent_constraint == DEFAULT):
            raise SpecificationError("recurrent_constraint", self.recurrent_constraint,
                                     "SequentialModel >> " + LSTM.__name__, "Constraint does not exist!")
        if not (self.bias_constraint in KERAS_LAYERS_CONSTRAINTS or self.bias_constraint == DEFAULT):
            raise SpecificationError("bias_constraint", self.bias_constraint, "SequentialModel >> " + LSTM.__name__,
                                     "Constraint does not exist!")
        if not (self.dropout == DEFAULT or 0 <= self.dropout <= 1):
            raise SpecificationError("dropout", self.dropout, "SequentialModel >> " + LSTM.__name__,
                                     "Must be float between 0 and 1!")
        if not (self.recurrent_dropout == DEFAULT or 0 <= self.recurrent_dropout <= 1):
            raise SpecificationError("recurrent_dropout", self.recurrent_dropout, "SequentialModel >> " + LSTM.__name__,
                                     "Must be float between 0 and 1!")

    def __check_required_arguments(self) -> None:
        if self.units == DEFAULT:
            raise RequiredArgumentError("units", LSTM.__name__)

    def __check_argument_composition(self) -> None:
        if self.unit_forget_bias in {True, DEFAULT} and self.bias_initializer not in {"zeros", DEFAULT}:
            raise ComponentCompositionError(LSTM.__name__,
                                            "If unit_forget_bias is True: bias.initializer must be 'zeros'.")

    def type(self) -> Components:
        return Components.LSTM
