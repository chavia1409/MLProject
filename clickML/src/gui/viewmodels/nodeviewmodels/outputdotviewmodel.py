import uuid

from common.models.component_descriptors.component_constants import DEFAULT
from common.models.pre_suc_descriptors import SuccessorDescriptor
from gui.mvvm.viewmodelbase import ViewModelBase
from varname import nameof


class OutputDotViewModel(ViewModelBase):

    def __init__(self, ml_component_id, successor_descriptor: SuccessorDescriptor, connect_callback, disconnect_callback, node_linker_service):
        super().__init__()
        self.__ml_component_id = ml_component_id
        self.__name = successor_descriptor.name
        self.__ml_component_id_connected_to = successor_descriptor.id_next
        self.__connect_callback = connect_callback
        self.__name_connected_to = successor_descriptor.name_next
        self.__disconnect_callback = disconnect_callback
        self.__node_linker_service = node_linker_service
        self.__is_connected = False
        self.__connection_line = None
        self.__x = 0
        self.__y = 0
        if successor_descriptor.id_next != DEFAULT:
            node_linker_service.request_connection_from_output(self, successor_descriptor)

    @property
    def name(self):
        return self.__name

    @property
    def successor_descriptor(self):
        descriptor = SuccessorDescriptor(self.__name)
        descriptor.name_next = self.__name_connected_to
        descriptor.id_next = self.__ml_component_id_connected_to
        return descriptor

    @property
    def ml_component_id(self):
        return self.__ml_component_id

    @property
    def drag_command(self):
        return self.on_drag

    def on_drag(self):
        if self.__is_connected:
            self.__node_linker_service.remove_by_output_dot(self)
        self.__node_linker_service.start(self)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value is self.__x:
            return
        if self.__connection_line is not None:
            self.__connection_line.x1 = value
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
            self.__connection_line.y1 = value
        self._notify_property_changed('y', value)

    @property
    def is_connected(self):
        return self.__is_connected

    def connect(self, connection_line, connected_to_ml_component_id:uuid, name_connected_to):
        self.__name_connected_to = name_connected_to
        self.__ml_component_id_connected_to = connected_to_ml_component_id
        self.__connection_line = connection_line
        connection_line.x1 = self.x
        connection_line.y1 = self.y
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
