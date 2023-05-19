import os
import sys
import unittest
from unittest.mock import MagicMock, patch
import context
from gui.factories.generalfactory import GeneralFactoryBase
from gui.services.nodemanagerbase import NodeManagerBase
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import NodeViewModelBase
from gui.widgets.nodeeditor.nodecontainerwidget import NodeContainerWidget
from gui.mvvm.contextview import ContextView
from gui.services.nodemanager import NodeManager

class NodeManagerTest(unittest.TestCase):

    @patch.multiple(GeneralFactoryBase, __abstractmethods__=set())
    def __init__(self, x):
        super().__init__(x)
        self.nodes_added_to_node_editor = []
        general_factory = GeneralFactoryBase()
        general_factory.create = lambda x: ContextView()
        node_editor = MagicMock()
        node_editor.add_node = lambda value: self.nodes_added_to_node_editor.append(value)
        node_editor.remove_node = lambda value: self.nodes_added_to_node_editor.remove(value)
        self.node_editor = node_editor
        self.sut = NodeManager(general_factory, node_editor)


    def test_can_add_and_remove(self):
        #Arrange
        nodes = []
        nodes.append(NodeViewModelBase())
        nodes.append(NodeViewModelBase())
        nodes.append(NodeViewModelBase())
        nodes.append(NodeViewModelBase())
        nodes.append(NodeViewModelBase())

        #Act
        for n in nodes:
            self.sut.add_node(n)

        for n in nodes[0:3]:
            self.sut.remove_node(n)

        #Assert
        self.assertNotEqual(self.nodes_added_to_node_editor[0].context, nodes[0])
        self.assertNotEqual(self.nodes_added_to_node_editor[1].context, nodes[1])
        self.assertTrue(len(self.nodes_added_to_node_editor) == 2)
