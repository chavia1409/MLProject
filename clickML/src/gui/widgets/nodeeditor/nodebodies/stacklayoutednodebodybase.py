from gui.kivyhelpers import load_kv
from kivy.uix.stacklayout import StackLayout
from gui.mvvm.contextview import ContextView

load_kv(__file__)


class StackLayoutedNodeBodyBase(StackLayout, ContextView):
    def __init__(self, **kwargs):
        super(StackLayoutedNodeBodyBase, self).__init__(**kwargs)

