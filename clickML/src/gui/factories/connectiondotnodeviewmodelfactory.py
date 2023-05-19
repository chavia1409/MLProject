import uuid
from varname import nameof

from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import InputDotViewModelFactoryBase, \
    OutputDotViewModelFactoryBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel


class InputDotViewModelFactory(InputDotViewModelFactoryBase):
    # connect_callback: Callable[[uuid], None],
    #                disconnect_callback: Callable[[], None]

    def __init__(self, node_linker_service):
        self.__node_linker_service = node_linker_service

    def create(self, ml_component_id: uuid, predecessor_descriptor: PredecessorDescriptor, **kwargs) -> InputDotViewModel:
        connect_callback = None
        if 'connect_callback' in kwargs:
            connect_callback = kwargs[nameof(connect_callback)]

        disconnect_callback = None
        if 'disconnect_callback' in kwargs:
            disconnect_callback = kwargs[nameof(disconnect_callback)]

        return InputDotViewModel(ml_component_id, predecessor_descriptor, connect_callback, disconnect_callback, self.__node_linker_service)


class OutputDotViewModelFactory(OutputDotViewModelFactoryBase):

    def __init__(self, node_linker_service):
        self.__node_linker_service = node_linker_service

    def create(self, ml_component_id: uuid, successor_descriptor: SuccessorDescriptor, **kwargs) -> OutputDotViewModel:
        connect_callback = None
        if 'connect_callback' in kwargs:
            connect_callback = kwargs[nameof(connect_callback)]

        disconnect_callback = None
        if 'disconnect_callback' in kwargs:
            disconnect_callback = kwargs[nameof(disconnect_callback)]

        return OutputDotViewModel(ml_component_id, successor_descriptor, connect_callback, disconnect_callback, self.__node_linker_service)
