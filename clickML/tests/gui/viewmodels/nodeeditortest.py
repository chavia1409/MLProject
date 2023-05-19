import unittest
import uuid
import context
from unittest.mock import MagicMock, patch
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.mlcomponentdesignerdescriptor import MLComponentDesignerDescriptor
from gui.viewmodels.nodeeditorviewmodel import NodeEditorViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import NodeViewModelBase, MLComponentNodeViewModel

class NodeEditorTest(unittest.TestCase):


    def __init__(self, x):
        super().__init__(x)
        self.vm_map = {}
        self.nodes_added_to_node_manager = []
        self.mlcomponent_nodeviewmodel_factory = MagicMock()
        self.mlcomponent_nodeviewmodel_factory.create_by_descriptor = self.create_mock
        self.node_manager = MagicMock()
        self.node_manager.add_node = lambda node: self.nodes_added_to_node_manager.append(node)
        self.node_manager.remove_node = lambda value: self.nodes_added_to_node_manager.remove(value)
        self.node_linker_service = MagicMock()
        self.sut = NodeEditorViewModel(self.mlcomponent_nodeviewmodel_factory, self.node_manager, self.node_linker_service)


    def create_mock(self, descriptor):
        mock = MockedNodeViewModel(descriptor)
        self.vm_map[descriptor.component_id] = mock
        return mock



    def test_create_from_descriptors(self):
        #Arrange
        d1_id = uuid.uuid4()
        d1 = ADescriptor(d1_id)
        d1.value_a = 'd1'
        dd1 = MLComponentDesignerDescriptor(d1_id, 420, 30)

        d2_id = uuid.uuid4()
        d2 = BDescriptor(d2_id)
        d2.value_a = 'd2'
        dd2 = MLComponentDesignerDescriptor(d2_id, 431, 65)

        d3_id = uuid.uuid4()
        d3 = ADescriptor(d3_id)
        d3.value_a = 'd3'
        dd3 = MLComponentDesignerDescriptor(d3_id, 22, 4)

        d4_id = uuid.uuid4()
        d4 = CDescriptor(d4_id)
        dd4 = MLComponentDesignerDescriptor(d4_id, 0, 0)

        d5_id = uuid.uuid4()
        d5 = BDescriptor(d5_id)
        dd5 = MLComponentDesignerDescriptor(d5_id, 10000, 0)

        d6_id = uuid.uuid4()
        d6 = BDescriptor(d6_id)
        dd6 = MLComponentDesignerDescriptor(d6_id, 0, 1000)

        descriptors = [d3, d4, d5, d6]

        designers = [dd3, dd6, dd4, dd5]

        #Act
        self.sut.add_node_by_descriptors(d1, dd1)
        self.sut.add_node_by_descriptors(d2, dd2)
        self.sut.create_from_descriptors(descriptors, designers)

        #Assert
        id_in_node_editor = list(map(lambda value: value.component_id, self.nodes_added_to_node_manager))
        self.assertNotIn(d1_id, id_in_node_editor)
        self.assertNotIn(d2_id, id_in_node_editor)
        self.assertIn(d3_id, id_in_node_editor)
        self.assertIn(d4_id, id_in_node_editor)
        self.assertIn(d5_id, id_in_node_editor)
        self.assertIn(d6_id, id_in_node_editor)

    def test_generate_descriptors(self):
        #Arrange
        d1_id = uuid.uuid4()
        d1 = ADescriptor(d1_id)
        d1.value_a = 420
        d1.value_b = 'Hello'
        d1.value_c = 241
        dd1 = MLComponentDesignerDescriptor(d1_id, 420, 30)

        d2_id = uuid.uuid4()
        d2 = BDescriptor(d2_id)
        d2.value_a = 'd2'
        d2.value_b = uuid.uuid4()
        dd2 = MLComponentDesignerDescriptor(d2_id, 431, 65)

        d3_id = uuid.uuid4()
        d3 = ADescriptor(d3_id)
        d3.value_a = 'd3'
        d3.value_b = ['a', 'b', 'c']
        d3.value_c = 28367
        dd3 = MLComponentDesignerDescriptor(d3_id, 22, 4)

        descriptors = [d1, d2, d3]

        designers = [dd1, dd2, dd3]
        #Act
        self.sut.create_from_descriptors(descriptors, designers)
        generated_descriptors = self.sut.generate_descriptors()
        #Assert
        self.assertIn(d1, generated_descriptors)
        self.assertIn(d2, generated_descriptors)
        self.assertIn(d3, generated_descriptors)

class ADescriptor(MLComponentDescriptor):
    def __init__(self, component_id):
        self.value_a = None
        self.value_b = None
        self.value_c = None
        self.__component_id = component_id

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return 'ADescriptor'

    def restore_component(self):
        pass

class BDescriptor(MLComponentDescriptor):
    def __init__(self, component_id):
        self.value_a = None
        self.value_b = None
        self.__component_id = component_id

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return 'BDescriptor'

    def restore_component(self):
        pass

class CDescriptor(MLComponentDescriptor):
    def __init__(self, component_id):
        self.value_a = None
        self.value_b = None
        self.value_c = None
        self.value_d = None
        self.__component_id = component_id

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return 'CDescriptor'

    def restore_component(self):
        pass


class MockedNodeViewModel(MLComponentNodeViewModel):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor):
        super().__init__(ml_component_descriptor)

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        return self._descriptor
