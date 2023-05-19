import uuid
from typing import Union

from backend.ml_components.neural_networks.c_sequential_model import SequentialModel
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.ml_layer_component_descriptor import MLLayerComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor


class SequentialModelDescriptor(MLComponentDescriptor):
    """
    Descriptor for SequentialModel component.

    Attributes:
        # attributes for possible predecessors and successors
        pre: PredecessorDescriptor
            (required if suc exists) input shape
        pre_2: PredecessorDescriptor
            (required if suc exists) output shape
        suc: SuccessorDescriptor
            (optional) component that uses sequential model

        # parameters for Sequential()
        name: str
            (optional) name of model
        layers: Union[list[MLLayerComponentDescriptor], str]
            (optional) keras_layers of the model, should be list

        # parameters for load_weights()
        weight_file: str
            (optional) directory of file with weights

        # parameters for compile()
        optimizer: str
            (optional) optimizer
        loss: str
            (required) loss function
        metrics: Union[list[str], str]
            (optional) metric functions, should be list[str]
    """

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        # attributes for possible predecessors and successors
        self.pre: PredecessorDescriptor = PredecessorDescriptor("input_shape")
        self.pre_2: PredecessorDescriptor = PredecessorDescriptor("output_shape")
        self.suc: SuccessorDescriptor = SuccessorDescriptor("model")

        # parameters for Sequential()
        self.name: str = DEFAULT
        self.layers: Union[list[MLLayerComponentDescriptor], str] = DEFAULT

        # parameters for load_weights()
        self.weight_file: str = DEFAULT

        # parameters for compile()
        self.optimizer: str = DEFAULT
        self.loss: str = DEFAULT
        self.metrics: Union[list[str], str] = DEFAULT

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return SequentialModel.__name__

    def restore_component(self) -> SequentialModel:
        return SequentialModel(self)
