from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, NumericProperty
from kivymd.uix.behaviors import FocusBehavior
from kivymd.uix.boxlayout import MDBoxLayout

from gui.kivyhelpers import load_kv
from kivy.uix.stacklayout import StackLayout
from gui.mvvm.contextview import ContextView

load_kv(__file__)


class RescalingContent(StackLayout, ContextView):
    scale = NumericProperty(0)
    offset = NumericProperty(0)

    def set_scale(self):
        try:
            float(self.ids.scale_input.text)
            self.scale = float(self.ids.scale_input.text)
        except:
            self.scale = 0.0
    def set_offset(self):
        try:
            float(self.ids.offset_input.text)
            self.offset = float(self.ids.offset_input.text)
        except:
            self.offset = 0.0

    def _define_bindings(self):
        self._bind_to_context('scale', 'scale')
        self._bind_to_context('offset', 'offset')

class FocusWidget(MDBoxLayout, FocusBehavior):
    pass