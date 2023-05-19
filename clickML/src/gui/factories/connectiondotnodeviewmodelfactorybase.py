import uuid
from abc import ABC, abstractmethod
from typing import Callable

from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel


class InputDotViewModelFactoryBase(ABC):

    @abstractmethod
    def create(self, ml_component_id: uuid, predecessor_descriptor: PredecessorDescriptor, **kwargs) -> InputDotViewModel:
        pass


class OutputDotViewModelFactoryBase(ABC):

    @abstractmethod
    def create(self, ml_component_id: uuid, successor_descriptor: SuccessorDescriptor, **kwargs) -> OutputDotViewModel:
        pass
