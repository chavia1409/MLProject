import uuid
from typing import Union

from backend.ml_components.neural_networks.keras_layers.l_dense import Dense
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.ml_layer_component_descriptor import MLLayerComponentDescriptor


class DenseDescriptor(MLLayerComponentDescriptor):
    """
    Descriptor for Dense layer.

    Attributes:

        # parameters for Dense()
            units: Union[int, str]
                (required, exception: this is last layer) dimensionality of the output space, should be int
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
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        # parameters for Dense()
        self.units: Union[int, str] = DEFAULT
        self.activation: str = DEFAULT
        self.use_bias: Union[bool, str] = DEFAULT
        self.kernel_initializer: str = DEFAULT
        self.bias_initializer: str = DEFAULT
        self.kernel_regularizer: str = DEFAULT
        self.bias_regularizer: str = DEFAULT
        self.activity_regularizer: str = DEFAULT
        self.kernel_constraint: str = DEFAULT
        self.bias_constraint: str = DEFAULT

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return Dense.__name__

    def restore_layer(self) -> Dense:
        return Dense(self)
