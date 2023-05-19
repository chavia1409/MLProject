import uuid
from dataclasses import dataclass
from typing import Union, Optional

from backend.ml_components.neural_networks.keras_layers.l_gru import GRU
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.ml_layer_component_descriptor import MLLayerComponentDescriptor


class GRUDescriptor(MLLayerComponentDescriptor):
    """
    Descriptor for GRU layer.

    Attributes:
        # parameters for GRU()
        units: Union[int, str]
            (required, exception: this is last layer) dimensionality of the output space, should be int
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
        kernel_regularizer: str
            (optional) weight regularizer
        recurrent_regularizer: str
            (optional) recurrent weight regularizer
        bias_regularizer: str
            (optional) kernel bias weight regularizer
        activity_regularizer: str
            (optional) activity weight regularizer
        kernel_constraint: str
            (optional) kernel constraint
        recurrent_constraint: str
            (optional) recurrent constraint
        bias_constraint: str
            (optional) bias constraint
        dropout: Union[float, str]
            (optional) fraction of units to drop (input), should be float
        recurrent_dropout: Union[float, str]
            (optional) fraction of units to drop (recurrent state), should be float
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        # parameters for GRU()
        self.units: Union[int, str] = DEFAULT
        self.activation: str = DEFAULT
        self.recurrent_activation: Optional[str] = DEFAULT
        self.use_bias: Union[bool, str] = DEFAULT
        self.kernel_initializer: str = DEFAULT
        self.recurrent_initializer: str = DEFAULT
        self.bias_initializer: str = DEFAULT
        self.kernel_regularizer: str = DEFAULT
        self.recurrent_regularizer: str = DEFAULT
        self.bias_regularizer: str = DEFAULT
        self.activity_regularizer: str = DEFAULT
        self.kernel_constraint: str = DEFAULT
        self.recurrent_constraint: str = DEFAULT
        self.bias_constraint: str = DEFAULT
        self.dropout: Union[float, str] = DEFAULT
        self.recurrent_dropout: Union[float, str] = DEFAULT

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return GRU.__name__

    def restore_layer(self) -> GRU:
        return GRU(self)
