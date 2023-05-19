from kivy.properties import NumericProperty
from kivy.uix.stacklayout import StackLayout

from gui.kivyhelpers import load_kv
from gui.mvvm.contextview import ContextView
load_kv(__file__)


class CenterCropContent(StackLayout, ContextView):
    height = NumericProperty(0)
    width = NumericProperty(0)

    def set_height(self):
        try:
            float(self.ids.height_input.text)
            self.height = int(self.ids.height_input.text)
        except:
            self.height = 0

    def set_width(self):
        try:
            float(self.ids.width_input.text)
            self.width = int(self.ids.width_input.text)
        except:
            self.width = 0

    def _define_bindings(self):
        self._bind_to_context('height', 'height')
        self._bind_to_context('width', 'width')
