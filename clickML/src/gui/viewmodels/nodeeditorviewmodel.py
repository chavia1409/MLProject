import uuid

from common.models.component_descriptors.text_processing.cd_letter_case import LetterCaseDescriptor
from common.models.component_descriptors.text_processing.cd_text_console_input import TextConsoleInputDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.mlcomponentdesignerdescriptor import MLComponentDesignerDescriptor
from gui.factories.mlcomponentnodeviewmodelfactorybase import MLComponentNodeViewModelFactoryBase
from gui.mvvm.viewmodelbase import ViewModelBase
from gui.services.nodemanagerbase import NodeManagerBase
from gui.mvvm.command import Command
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import NodeViewModelBase
from .helper import get_input_dots, get_output_dots
from ..services.nodelinkerservicebase import NodeLinkerServiceBase



class NodeEditorViewModel(ViewModelBase):

    def __init__(self, mlcomponent_nodeviewmodel_factory: MLComponentNodeViewModelFactoryBase, node_manager: NodeManagerBase, node_linker_service: NodeLinkerServiceBase):
        super().__init__()
        self.__node_manager = node_manager
        self.__mlcomponent_nodeviewmodel_factory = mlcomponent_nodeviewmodel_factory
        self.__node_linker_service = node_linker_service
        self.__nodes = []

    def create_from_descriptors(self, component_descriptors: list[MLComponentDescriptor], designer_descriptors: list[MLComponentDesignerDescriptor]):
        self.clear()
        for (c, d) in list(map(lambda c: (c, next((d for d in designer_descriptors if d.component_id == c.component_id), MLComponentDesignerDescriptor(c.component_id, 0, 0))), component_descriptors)):
            self.add_node_by_descriptors(c, d)
        self.__node_linker_service.clear_requests()

    def generate_descriptors(self) -> list[MLComponentDescriptor]:
        descriptors = []
        for node in self.__nodes:
            descriptors.append(node.ml_component_descriptor)
        return descriptors

    def generate_designer_descriptors(self) -> list[MLComponentDesignerDescriptor]:
        descriptors = []
        for node in self.__nodes:
            descriptors.append(node.ml_component_designer_descriptor)
        return descriptors

    def clear(self):
        for node in self.__nodes.copy():
            self.delete_node(node)
        self.__nodes.clear()

    @property
    def delete_node_command(self):
        return Command(self.delete_node)

    def delete_node(self, node):
        if not isinstance(node, NodeViewModelBase):
            return
        for input_dot in get_input_dots(node):
            self.__node_linker_service.remove(input_dot)
        for output_dot in get_output_dots(node):
            self.__node_linker_service.remove_by_output_dot(output_dot)
        self.__node_manager.remove_node(node)
        self.__nodes.remove(node)

    @property
    def add_node_command(self):
        return Command(self.add_node)

    def add_node(self, component_type: str, x, y):
        nodeViewModel = self.__mlcomponent_nodeviewmodel_factory.create(component_type)
        nodeViewModel.ml_component_designer_descriptor = MLComponentDesignerDescriptor(nodeViewModel.component_id, x, y)
        self.__node_manager.add_node(nodeViewModel)
        self.__nodes.append(nodeViewModel)

    def add_node_by_descriptors(self, descriptor: MLComponentDescriptor, designer: MLComponentDesignerDescriptor):
        node_view_model = self.__mlcomponent_nodeviewmodel_factory.create_by_descriptor(descriptor)
        node_view_model.ml_component_designer_descriptor = designer
        self.__nodes.append(node_view_model)
        self.__node_manager.add_node(node_view_model)
