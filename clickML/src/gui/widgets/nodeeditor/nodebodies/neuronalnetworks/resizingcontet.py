from kivy.uix.stacklayout import StackLayout

from gui.mvvm.contextview import ContextView


class ResizingContent(StackLayout, ContextView):
    def _define_bindings(self):
        pass