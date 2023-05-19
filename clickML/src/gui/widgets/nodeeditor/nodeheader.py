from gui.kivyhelpers import load_kv
from varname import nameof
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.behaviors.drag import DragBehavior
from kivy.properties import StringProperty

from gui.mvvm.contextview import ContextView

load_kv(__file__)


class NodeHeader(DragBehavior, RelativeLayout, ContextView):
    title: StringProperty = StringProperty()

    def _define_bindings(self):
        self._bind_to_context('title', 'title')
        return super()._define_bindings()
