from kivy.properties import StringProperty, BooleanProperty

from gui.kivyhelpers import load_kv
from kivy.uix.stacklayout import StackLayout
from gui.mvvm.contextview import ContextView

load_kv(__file__)


class Conv2DContent(StackLayout, ContextView):
    filters_value = StringProperty()
    kernel_size_one = StringProperty()
    kernel_size_two = StringProperty()
    two_kernel_size_values = BooleanProperty()

    def _define_bindings(self):
        self._bind_to_context('filters_value', 'filters')
        self._bind_to_context('kernel_size_one', 'kernel_size_one')
        self._bind_to_context('kernel_size_two', 'kernel_size_two')
        self._bind_to_context('two_kernel_size_values', 'two_kernel_size_values')