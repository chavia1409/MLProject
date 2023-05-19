from gui.factories.generalfactory import GeneralFactory
from gui.services.nodemanagerbase import NodeManagerBase
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import NodeViewModelBase
from gui.widgets.nodeeditor.nodecontainerwidget import NodeContainerWidget


class NodeManager(NodeManagerBase):

    def __init__(self, general_factory: GeneralFactory, node_editor):
        self.__general_factory = general_factory
        self.__node_editor = node_editor
        self.__node_container_map = {}

    def add_node(self, node: NodeViewModelBase):
        if node in self.__node_container_map:
            return
        node_container = self.__general_factory.create(NodeContainerWidget)
        node_container.context = node
        self.__node_container_map[node] = node_container
        self.__node_editor.add_node(node_container)

    def remove_node(self, node: NodeViewModelBase):
        if node not in self.__node_container_map:
            return
        node_container = self.__node_container_map[node]
        self.__node_editor.remove_node(node_container)
