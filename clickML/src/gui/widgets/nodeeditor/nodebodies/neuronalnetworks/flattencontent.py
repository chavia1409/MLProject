from kivy.properties import StringProperty, BooleanProperty

from gui.kivyhelpers import load_kv
from kivy.uix.stacklayout import StackLayout
from gui.mvvm.contextview import ContextView

load_kv(__file__)


class FlattenContent(StackLayout, ContextView):
    data_format_enabled = BooleanProperty()
    data_format = StringProperty()

    def _define_bindings(self):
        self._bind_to_context('data_format_enabled', 'data_format_enabled')
        self._bind_to_context('data_format', 'data_format')
