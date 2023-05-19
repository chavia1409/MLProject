from abc import ABC

from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import NodeViewModelBase


class NodeManagerBase(ABC):

    def add_node(self, node: NodeViewModelBase):
        pass

    def remove_node(self, node: NodeViewModelBase):
        pass