from kivy.properties import ObjectProperty, StringProperty

from gui.kivyhelpers import load_kv
from kivy.uix.screenmanager import Screen
from varname import nameof
from gui.mvvm.contextview import ContextView

load_kv(__file__)

class EditorScreen(Screen, ContextView):

    node_editor_context = ObjectProperty(None)
    terminal_context = ObjectProperty(None)
    project_name = StringProperty()

    def _define_bindings(self):
        self._bind_to_context('node_editor_context', 'node_editor')
        self._bind_to_context('terminal_context', 'terminal')
        self._bind_to_context('project_name', 'project_name')

    def on_project_name(self, instance, value):
        pass
