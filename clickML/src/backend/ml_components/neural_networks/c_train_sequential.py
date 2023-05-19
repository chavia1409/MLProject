from __future__ import annotations

import copy
from typing import Union, TYPE_CHECKING

from backend.component_enum import Components
from backend.ml_components.ml_component import MLComponent
from backend.ml_components.valid_connections import NET_INPUT_PROVIDERS, NET_OUTPUT_PROVIDERS, MODEL_PROVIDERS
from common.exceptions.click_ml_exceptions import SpecificationError, ComponentCompositionError
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor

if TYPE_CHECKING:
    from common.models.component_descriptors.neural_networks.cd_train_sequential import TrainSequentialDescriptor


class TrainSequential(MLComponent):
    """
    Component for training Sequential model.

    Attributes:
        # attributes for possible predecessors and successors
        pre: PredecessorDescriptor
            (required) training net input
        pre_2: PredecessorDescriptor
            (required) training net output
        pre_3: PredecessorDescriptor
            (required) model which should be trained
        suc: SuccessorDescriptor
            (optional) component that works on text

        # parameters for fit()
        batch_size: Union[int, None, str]
            (optional) Number of samples per gradient update, should be int or None
        epochs: Union[int, str]
            (optional) Number of epochs to train the model, should be int
        verbose: Union[str, int]
            (optional) verbosity modes
        validation_split: Union[float, str]
            (optional) float between 0 and 1 to divide in training and validation data, should be float

        plot_progress: bool
            (optional) decision whether progress of training should be plotted or not; default is False
        save_weights: bool
            (optional) decision whether weights for model should be saved to same directory like skript
    """

    def __init__(self, descriptor: TrainSequentialDescriptor) -> None:
        des = copy.deepcopy(descriptor)
        super().__init__(des.component_id)

        # attributes for possible predecessors and successors
        self.pre: PredecessorDescriptor = des.pre
        self.pre_2: PredecessorDescriptor = des.pre_2
        self.pre_3: PredecessorDescriptor = des.pre_3
        self.suc: SuccessorDescriptor = des.suc

        # parameters for fit()
        self.batch_size: Union[int, None, str] = des.batch_size
        self.epochs: Union[int, str] = des.epochs
        self.verbose: Union[int, str] = des.verbose
        self.validation_split: Union[float, str] = des.validation_split

        # options
        self.plot_progress: bool = des.plot_progress
        self.save_weights: bool = des.save_weights

        # preprocessing
        self.net_input: str = DEFAULT
        self.net_output: str = DEFAULT
        self.model: str = DEFAULT
        self.validation_data: str = DEFAULT

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return [self.pre, self.pre_2, self.pre_3]

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return [self.suc]

    @property
    def values_for_successors(self) -> dict[str, str]:
        return {self.suc.name: self.model}

    @property
    def __parameters_fit(self) -> str:
        callbacks = "[checkpoint]" if self.save_weights else DEFAULT
        net_output = self.net_output if self.net_output != "DATASET" else DEFAULT
        param_dict = {"x": self.net_input, "y": net_output, "batch_size": self.batch_size, "epochs": self.epochs,
                      "verbose": self.verbose, "validation_split": self.validation_split,
                      "validation_data": self.validation_data, "callbacks": callbacks}
        return self.toolkit.create_param_string(param_dict, no_repr=("x", "y", "callbacks", "validation_data"))

    def to_code(self) -> str:
        code = "# training sequential model\n"
        checkpoint = "cp_filepath = 'epoch_{epoch:02d}-loss_{loss:.2f}.hdf5'\n" \
                     "checkpoint = ModelCheckpoint(cp_filepath, monitor='loss', verbose=1, save_best_only=True)\n\n"
        code += "history = " if self.plot_progress else ""
        code += f"{self.model}.fit({self.__parameters_fit})"
        plotting = "\n\n# plotting history with all specified metrics\n"\
                   "pd.DataFrame(history.history).plot()\n" \
                   "plt.show()"
        code = code + plotting if self.plot_progress else code
        code = checkpoint + code if self.save_weights else code
        return code

    def get_needed_imports(self) -> list[str]:
        imports = ["from keras.models import Sequential"]
        if self.plot_progress:
            imports += ["from matplotlib import pyplot as plt", "import pandas as pd"]
        if self.save_weights:
            imports += ["from keras.callbacks import ModelCheckpoint"]
        return imports

    def check_if_valid(self) -> None:
        self.__check_neighbors()
        self.__check_domain_validity()
        self.__check_argument_composition()

    def __check_domain_validity(self) -> None:
        if not (isinstance(self.batch_size, int) or self.batch_size in {None, DEFAULT}):
            raise SpecificationError("batch_size", self.batch_size, TrainSequential.__name__, "Must be int or None!")
        if not (isinstance(self.epochs, int) or self.epochs == DEFAULT):
            raise SpecificationError("epochs", self.epochs, TrainSequential.__name__, "Must be int!")
        if self.verbose not in {DEFAULT, "auto", 0, 1, 2}:
            raise SpecificationError("verbose", self.verbose, TrainSequential.__name__, "Not a valid mode for verbose!")

    def __check_neighbors(self) -> None:
        self.toolkit.check_needed_predecessors([self.pre, self.pre_2, self.pre_3], TrainSequential.__name__)
        self.toolkit.check_pre_connection_validity(self.pre, NET_INPUT_PROVIDERS)
        self.toolkit.check_pre_connection_validity(self.pre_2, NET_OUTPUT_PROVIDERS)
        self.toolkit.check_pre_connection_validity(self.pre_3, MODEL_PROVIDERS)

    def __check_argument_composition(self) -> None:
        if self.validation_data == "validation_data" and self.validation_split != DEFAULT:
            raise ComponentCompositionError(TrainSequential.__name__, "'validation_split' should not be specified if"
                                                                      "model will be trained on a tensorflow dataset!")
        if self.validation_data == "validation_data" and self.batch_size != DEFAULT:
            raise ComponentCompositionError(TrainSequential.__name__, "'batch_size' should not be specified if"
                                                                      "model will be trained on a tensorflow dataset!")

    def do_preprocessing(self) -> None:
        self.net_input = self.toolkit.get_data_from_predecessor(self.pre)
        self.net_output = self.toolkit.get_data_from_predecessor(self.pre_2)
        self.model = self.toolkit.get_data_from_predecessor(self.pre_3)
        if self.net_output == "validation_data":
            self.validation_data = self.net_output
            self.net_output = DEFAULT

    def type(self) -> Components:
        return Components.TRAIN_SEQUENTIAL
