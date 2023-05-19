import uuid

from common.models.component_descriptors.component_constants import DEFAULT
from common.models.pre_suc_descriptors import SuccessorDescriptor, PredecessorDescriptor
from gui.mvvm.viewmodelbase import ViewModelBase
from varname import nameof


class InputDotViewModel(ViewModelBase):

    def __init__(self, ml_component_id, predecessor_descriptor: PredecessorDescriptor, connect_callback, disconnect_callback, node_linker_service):
        super().__init__()
        self.__ml_component_id = ml_component_id
        self.__name = predecessor_descriptor.name
        self.__name_connected_to = predecessor_descriptor.name_prev
        self.__ml_component_id_connected_to = predecessor_descriptor.id_prev
        self.__connect_callback = connect_callback
        self.__disconnect_callback = disconnect_callback
        self.__node_linker_service = node_linker_service
        self.__is_connected = False
        self.__connection_line = None
        self.__x = 0
        self.__y = 0
        if predecessor_descriptor.id_prev != DEFAULT:
            node_linker_service.request_connection_from_input(self, predecessor_descriptor)

    @property
    def predecessor_descriptor(self):
        descriptor = PredecessorDescriptor(self.__name)
        descriptor.name_prev = self.__name_connected_to
        descriptor.id_prev = self.__ml_component_id_connected_to
        return descriptor

    @property
    def ml_component_id(self):
        return self.__ml_component_id

    @property
    def name(self):
        return self.__name

    @property
    def x(self):
        if self.__connection_line is not None:
            return self.__connection_line.x2
        return 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value is self.__x:
            return
        if self.__connection_line is not None:
            self.__connection_line.x2 = value
        self.__x = value
        self._notify_property_changed('x', value)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value is self.__y:
            return
        self.__y = value
        if self.__connection_line is not None:
            self.__connection_line.y2 = value
        self._notify_property_changed('y', value)

    @property
    def drop_command(self):
        return self.on_drop

    def on_drop(self):
        if self.is_connected:
            self.__node_linker_service.remove(self)
        self.__node_linker_service.accept(self)


    @property
    def drag_command(self):
        return self.on_drag

    def on_drag(self):
        if not self.is_connected:
            return
        self.__node_linker_service.relink(self)

    @property
    def is_connected(self):
        return self.__is_connected

    def connect(self, connection_line, connected_to_ml_component_id:uuid, name_connected_to):
        self.__name_connected_to = name_connected_to
        self.__ml_component_id_connected_to = connected_to_ml_component_id
        self.__connection_line = connection_line
        connection_line.x2 = self.x
        connection_line.y2 = self.y
        self.__is_connected = True
        if self.__connect_callback is not None:
            self.__connect_callback(connected_to_ml_component_id)

    def disconnect(self):
        self.__name_connected_to = DEFAULT
        self.__connection_line = None
        self.__ml_component_id_connected_to = DEFAULT
        self.__connection_line = None
        self.__is_connected = False
        if self.__disconnect_callback is not None:
            self.__disconnect_callback()
