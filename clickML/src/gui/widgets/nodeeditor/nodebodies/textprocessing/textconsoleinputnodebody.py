from gui.kivyhelpers import load_kv
from kivy.uix.relativelayout import RelativeLayout
from gui.mvvm.contextview import ContextView
from gui.widgets.nodeeditor.nodebodies.stacklayoutednodebodybase import StackLayoutedNodeBodyBase

load_kv(__file__)


class TextConsoleInputNodeBody(StackLayoutedNodeBodyBase):
    def _on_context_changed(self):
        if self.context is not None:
            self.ids.output.context = self.context.output
