from kivy.properties import StringProperty
from gui.kivyhelpers import load_kv
from kivy.uix.relativelayout import RelativeLayout
from gui.mvvm.contextview import ContextView

load_kv(__file__)


class LSTMContent(RelativeLayout, ContextView):
    units = StringProperty()

    def _define_bindings(self):
        self._bind_to_context('units', 'units')