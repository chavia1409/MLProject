from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor
from gui.services.nodelinkerservicebase import NodeLinkerServiceBase
from gui.viewmodels.nodeviewmodels.inputdotviewmodel import InputDotViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel


class NodeLinkerService(NodeLinkerServiceBase):

    def __init__(self, node_editor):
        self.__node_editor = node_editor
        self.__current_line = None
        self.__current_output_dot = None
        self.__connection_map = {}
        self.__connection_line_map = {}
        self.__requests_from_inputs_map = {}
        self.__requests_from_outputs_map = {}

    def start(self, output_dot: OutputDotViewModel):
        self.__current_line = self.__node_editor.start_linking(output_dot.x, output_dot.y)
        self.__current_output_dot = output_dot

    def accept(self, input_dot: InputDotViewModel):
        if self.__current_line is None:
            return
        if self.__current_output_dot is None:
            return
        output_dot = self.__current_output_dot
        self.connect(input_dot, output_dot)
        self.__current_output_dot = None

    def connect(self, input_dot: InputDotViewModel, output_dot: OutputDotViewModel):
        line = self.__node_editor.create_line(input_dot.x, input_dot.y, output_dot.x, output_dot.y)
        output_dot.connect(line, input_dot.ml_component_id, input_dot.name)
        input_dot.connect(line, output_dot.ml_component_id, output_dot.name)
        self.__connection_map[input_dot] = output_dot
        self.__connection_line_map[input_dot] = line

    def relink(self, input_dot: InputDotViewModel):
        if input_dot not in self.__connection_map:
            return
        output_dot = self.__connection_map[input_dot]
        self.remove(input_dot)
        output_dot.on_drag()

    def remove(self, input_dot: InputDotViewModel):
        if input_dot not in self.__connection_map:
            return
        output_dot = self.__connection_map[input_dot]
        output_dot.disconnect()
        input_dot.disconnect()
        self.__connection_map.pop(input_dot)

        if input_dot not in self.__connection_line_map:
            return
        line = self.__connection_line_map[input_dot]
        self.__node_editor.remove_line(line)

    def remove_by_output_dot(self, output_dot: OutputDotViewModel):
        if output_dot not in self.__connection_map.values():
            return
        key = list(self.__connection_map.keys())[list(self.__connection_map.values()).index(output_dot)]
        self.remove(key)

    def request_connection_from_input(self, input_dot: InputDotViewModel, predecessor_descriptor: PredecessorDescriptor):
        key = (predecessor_descriptor.id_prev, predecessor_descriptor.name_prev)
        if key not in self.__requests_from_outputs_map:
            self.__requests_from_inputs_map[(input_dot.ml_component_id, input_dot.name)] = input_dot
            return
        output_dot = self.__requests_from_outputs_map[key]
        self.connect(input_dot, output_dot)
        self.__requests_from_outputs_map.pop(key)


    def request_connection_from_output(self, output_dot: OutputDotViewModel, successor_descriptor: SuccessorDescriptor):
        key = (successor_descriptor.id_next, successor_descriptor.name_next)
        if key not in self.__requests_from_inputs_map:
            self.__requests_from_outputs_map[(output_dot.ml_component_id, output_dot.name)] = output_dot
            return
        input_dot = self.__requests_from_inputs_map[key]
        self.connect(input_dot, output_dot)
        self.__requests_from_inputs_map.pop(key)

    def clear_requests(self):
        self.__requests_from_inputs_map.clear()
        self.__requests_from_outputs_map.clear()

