from __future__ import annotations

import copy
import os
from typing import Union, TYPE_CHECKING

from common.exceptions.click_ml_exceptions import SpecificationError, RequiredArgumentError
from backend.ml_components.ml_component import MLComponent
from common.models.component_descriptors.component_constants \
    import DEFAULT, KERAS_OPTIMIZERS, KERAS_LOSSES, KERAS_METRICS
from backend.ml_components.ml_layer_component import MLLayerComponent
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from backend.ml_components.valid_connections import INPUT_SHAPE_PROVIDERS, OUTPUT_SHAPE_PROVIDERS
from backend.component_enum import Components

if TYPE_CHECKING:
    from common.models.component_descriptors.neural_networks.cd_sequential_model import SequentialModelDescriptor


class SequentialModel(MLComponent):
    """
    Component for constructing Sequential model.

    Attributes:
        # attributes for possible predecessors and successors
        pre: PredecessorDescriptor
            (optional)
        pre_2: PredecessorDescriptor
            (required if suc exists)
        suc: SuccessorDescriptor
            (optional) component that works on text

        # parameters for Sequential()
        name: str
            (optional) name of model
        layers: Union[list[MLLayerComponentDescriptor], str]
            (optional) keras_layers of the model, should be list[MLLayerComponentDescriptor]

        # parameters for load_weights()
        weight_file: str
            (optional) directory of file with weights

        # parameters for compile()
        optimizer: str
            (optional) optimizer
        loss: str
            (optional) loss function
        metrics: Union[list[str], str]
            (optional) metrics

        # preprocessing
        input_shape: str
            code snippet that can be used for specifying the input shape for sequential model
        output_shape: str
            code snippet that can be used for specifying the output shape for sequential model
    """

    def __init__(self, descriptor: SequentialModelDescriptor) -> None:
        des = copy.deepcopy(descriptor)
        super().__init__(des.component_id)

        # attributes for possible predecessors and successors
        self.pre: PredecessorDescriptor = des.pre
        self.pre_2: PredecessorDescriptor = des.pre_2
        self.suc: SuccessorDescriptor = des.suc

        # parameters for Sequential()
        self.name: str = des.name
        layers = [layer.restore_layer() for layer in des.layers] if isinstance(des.layers, list) else []
        self.layers: Union[list[MLLayerComponent], str] = layers

        # parameters for load_weights()
        self.weight_file: str = des.weight_file

        # parameters for compile()
        self.optimizer: str = des.optimizer
        self.loss: str = des.loss
        self.metrics: Union[list[str], str] = des.metrics

        # preprocessing
        self.input_shape: str = DEFAULT
        self.output_shape: str = DEFAULT

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return [self.pre, self.pre_2]

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return [self.suc]

    @property
    def values_for_successors(self) -> dict[str, str]:
        return {self.suc.name: "model"}

    @property
    def __parameters_sequential(self) -> str:
        param_dict = {"name": self.name}
        return self.toolkit.create_param_string(param_dict)

    @property
    def __parameters_compile(self) -> str:
        param_dict = {"optimizer": self.optimizer, "loss": self.loss, "metrics": self.metrics}
        return self.toolkit.create_param_string(param_dict)

    def to_code(self) -> str:
        code = "# creating sequential model\n"\
               f"{self.values_for_successors[self.suc.name]} = Sequential({self.__parameters_sequential})\n"
        if self.input_shape != DEFAULT:
            code += f"{self.values_for_successors[self.suc.name]}.add(Input(shape={self.input_shape}))\n"
        if self.layers != DEFAULT:
            for layer in self.layers:
                code += f"{self.values_for_successors[self.suc.name]}.add({(layer.to_code().strip())})\n"
        if self.weight_file != DEFAULT:
            code += f'{self.values_for_successors[self.suc.name]}.load_weights({repr(self.weight_file)})\n'
        code += f"{self.values_for_successors[self.suc.name]}.compile({self.__parameters_compile})"
        return code

    def get_needed_imports(self) -> list[str]:
        imports = ["from keras.models import Sequential"]
        if self.input_shape != DEFAULT:
            imports += ["from keras.layers import Input"]
        for layer in self.layers:
            imports += layer.get_needed_imports()
        return imports

    def check_if_valid(self) -> None:
        self.__check_neighbors()
        self.__check_required_arguments()
        for layer in self.layers:
            layer.check_if_valid()
        self.__check_domain_validity()

    def __check_domain_validity(self) -> None:
        if isinstance(self.layers, str) and self.layers != DEFAULT:
            raise SpecificationError("layers", self.layers, SequentialModel.__name__,
                                     "Must be a list of MLLayerComponentDescriptors!")
        if not self.layers:
            raise SpecificationError("layers", self.layers, SequentialModel.__name__,
                                     "Should contain at least one layer!")
        if self.weight_file != DEFAULT and not os.path.isfile(self.weight_file):
            raise SpecificationError("weight_file", self.weight_file, SequentialModel.__name__,
                                     "Not a valid file!")
        if self.optimizer != DEFAULT and self.optimizer not in KERAS_OPTIMIZERS:
            raise SpecificationError("optimizer", self.optimizer, SequentialModel.__name__,
                                     "Not an existing optimizer!")
        if self.loss != DEFAULT and self.loss not in KERAS_LOSSES:
            raise SpecificationError("loss", self.loss, SequentialModel.__name__,
                                     "Not an existing loss function!")
        if self.metrics != DEFAULT and not set(self.metrics).issubset(KERAS_METRICS):
            raise SpecificationError("metrics", self.metrics, SequentialModel.__name__,
                                     "One or more metrics are not valid!")

    def __check_neighbors(self) -> None:
        self.toolkit.check_needed_predecessors([self.pre_2], SequentialModel.__name__)
        self.toolkit.check_pre_connection_validity(self.pre, INPUT_SHAPE_PROVIDERS)
        self.toolkit.check_pre_connection_validity(self.pre_2, OUTPUT_SHAPE_PROVIDERS)

    def __check_required_arguments(self) -> None:
        if self.layers == DEFAULT:
            raise RequiredArgumentError("layers", SequentialModel.__name__)
        if self.loss == DEFAULT:
            raise RequiredArgumentError("loss", SequentialModel.__name__)

    def do_preprocessing(self) -> None:
        self.input_shape = self.toolkit.get_data_from_predecessor(self.pre)
        self.output_shape = self.toolkit.get_data_from_predecessor(self.pre_2)
        if self.output_shape != DEFAULT:
            for layer in reversed(self.layers):
                if layer.set_output_shape(self.output_shape):
                    break
        lstm_gru = [layer for layer in self.layers if layer.type() in {Components.LSTM, Components.GRU}]
        for layer in lstm_gru[:-1]:
            layer.return_sequences = "True"

    def type(self) -> Components:
        return Components.SEQUENTIAL_MODEL
