from kivy.properties import StringProperty, BooleanProperty

from gui.kivyhelpers import load_kv
from kivy.uix.stacklayout import StackLayout
from gui.mvvm.contextview import ContextView

load_kv(__file__)


class MaxPool2DContent(StackLayout, ContextView):
    pool_size_one = StringProperty()
    pool_size_two = StringProperty()
    two_pool_size_values = BooleanProperty()

    def _define_bindings(self):
        self._bind_to_context('pool_size_one', 'pool_size_one')
        self._bind_to_context('pool_size_two', 'pool_size_two')
        self._bind_to_context('two_pool_size_values', 'two_pool_size_values')
