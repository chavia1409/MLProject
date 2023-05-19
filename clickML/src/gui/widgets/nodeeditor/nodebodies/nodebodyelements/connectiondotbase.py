from kivy.properties import NumericProperty
from varname import nameof

from gui.mvvm.contextview import ContextView
from gui.widgets.nodeeditor import nodeeditorwidget


class ConnectionDotBase(ContextView):
    def __init__(self):
        super().__init__()

        self.bind(right=lambda x, y: self.update_position())
        self.bind(top=lambda x, y: self.update_position())


    dot_x: NumericProperty = NumericProperty(0)
    dot_y: NumericProperty = NumericProperty(0)
    node_editor = None


    def _on_context_changed(self):
        if self.context is not None and self.parent is not None:
            self.update_position()

    def _define_bindings(self):
        self._bind_to_context('dot_x', 'x')
        self._bind_to_context('dot_y', 'y')

    def update_position(self):
        x, y = self.get_dot_position()
        self.dot_x = x + self.ids.dot.height / 2
        self.dot_y = y + self.ids.dot.width / 2

    def get_dot_position(self):
        node_editor = self.get_node_editor()
        if node_editor is None:
            return 0,0
        x, y = self.ids.dot.to_window(*self.ids.dot.pos)
        x, y = node_editor.ids.node_space.to_widget(x, y)
        return x, y

    def get_node_editor(self):
        if self.node_editor is not None:
            return self.node_editor
        current = self.parent
        while not isinstance(current, nodeeditorwidget.NodeEditorWidget):
            if current.parent is None:
                return None
            current = current.parent
        self.node_editor = current
        return current