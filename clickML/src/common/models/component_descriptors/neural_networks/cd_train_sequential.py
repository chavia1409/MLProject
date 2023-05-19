import uuid
from typing import Union

from backend.ml_components.neural_networks.c_train_sequential import TrainSequential
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor


class TrainSequentialDescriptor(MLComponentDescriptor):
    """
    Descriptor for TrainSequential component.

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

    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        # attributes for possible predecessors and successors
        self.pre: PredecessorDescriptor = PredecessorDescriptor("training_net_input")
        self.pre_2: PredecessorDescriptor = PredecessorDescriptor("training_net_output")
        self.pre_3: PredecessorDescriptor = PredecessorDescriptor("model_to_train")
        self.suc: SuccessorDescriptor = SuccessorDescriptor("model")

        # parameters for fit()
        self.batch_size: Union[int, None, str] = DEFAULT
        self.epochs: Union[int, str] = DEFAULT
        self.verbose: Union[str, int] = DEFAULT
        self.validation_split: Union[float, str] = DEFAULT

        self.plot_progress: bool = False
        self.save_weights: bool = False

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return TrainSequential.__name__

    def restore_component(self) -> TrainSequential:
        return TrainSequential(self)
