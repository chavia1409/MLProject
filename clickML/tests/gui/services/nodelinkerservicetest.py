import unittest
import uuid
from unittest.mock import MagicMock, patch
import context
from gui.services.nodelinkerservice import NodeLinkerService

class NodeLinkerServiceTest(unittest.TestCase):

    def __init__(self, x):
        super().__init__(x)
        self.mocked_line = MockedLine()
        self.nodes_added_to_node_editor = []
        self.node_editor = MagicMock()
        self.node_editor.start_linking = MagicMock(return_value=self.mocked_line)
        self.node_editor.create_line = MagicMock(return_value=self.mocked_line)
        self.sut = NodeLinkerService(self.node_editor)

    def test_start_accept(self):
        #Arrange
        input_dot = MagicMock()
        input_dot.ml_component_id = uuid.uuid4()
        input_dot.name = 'Input'
        output_dot = MagicMock()
        output_dot.ml_component_id = uuid.uuid4()
        output_dot.name = 'Output'

        #Act
        self.sut.start(output_dot)
        self.sut.accept(input_dot)

        #Assert
        input_dot.connect.assert_called_with(self.mocked_line, output_dot.ml_component_id, output_dot.name)
        output_dot.connect.assert_called_with(self.mocked_line, input_dot.ml_component_id, input_dot.name)

    def test_relink_accept(self):
        # Arrange
        old_input_dot = MagicMock()
        old_input_dot.ml_component_id = uuid.uuid4()
        old_input_dot.name = 'old input'
        old_input_dot.connect = MagicMock()

        new_input_dot = MagicMock()
        new_input_dot.ml_component_id = uuid.uuid4()
        new_input_dot.name = 'new input'

        output_dot = MagicMock()
        output_dot.ml_component_id = uuid.uuid4()
        output_dot.name = 'Output'


        # Act
        self.sut.start(output_dot)
        self.sut.accept(old_input_dot)
        self.sut.relink(old_input_dot)
        self.sut.remove_by_output_dot(output_dot)   # normally called by output_dot
        self.sut.start(output_dot)                  # normally called by output_dot
        self.sut.accept(new_input_dot)

        # Assert
        old_input_dot.disconnect.assert_called()
        new_input_dot.connect.assert_called_with(self.mocked_line, output_dot.ml_component_id, output_dot.name)
        output_dot.connect.assert_called_with(self.mocked_line, new_input_dot.ml_component_id, new_input_dot.name)


class MockedLine:
    pass