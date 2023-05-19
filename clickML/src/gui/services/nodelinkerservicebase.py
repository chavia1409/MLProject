from abc import ABC, abstractmethod

from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel


class NodeLinkerServiceBase(ABC):

    @abstractmethod
    def start(self, output_dot: OutputDotViewModel):
        pass

    @abstractmethod
    def accept(self, input_dot: InputDotViewModel):
        pass

    @abstractmethod
    def relink(self, line):
        pass

    @abstractmethod
    def connect(self, input_dot: InputDotViewModel, output_dot: OutputDotViewModel):
        pass

    @abstractmethod
    def remove(self, input_dot: InputDotViewModel):
        pass

    @abstractmethod
    def remove_by_output_dot(self, output_dot: OutputDotViewModel):
        pass

    @abstractmethod
    def request_connection_from_input(self, input_dot: InputDotViewModel,
                                      predecessor_descriptor: PredecessorDescriptor):
        pass

    @abstractmethod
    def request_connection_from_output(self, output_dot: OutputDotViewModel, successor_descriptor: SuccessorDescriptor):
        pass

    @abstractmethod
    def clear_requests(self):
        pass