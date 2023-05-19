from kivymd.uix.behaviors import HoverBehavior

from gui.kivyhelpers import load_kv
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty
from gui.mvvm.contextview import ContextView
from varname import nameof

load_kv(__file__)


class ConnectionLine(HoverBehavior, Widget, ContextView):
    line_color = ListProperty((192/255,192/255,192/255,1))

    x1: NumericProperty = NumericProperty(0)
    y1: NumericProperty = NumericProperty(0)
    x2: NumericProperty = NumericProperty(0)
    y2: NumericProperty = NumericProperty(0)

    def change_color_touch_move(self):
        self.line_color = ((3/255, 138/255, 1, 1))

    def change_color_touch_up(self):
        self.line_color = ((192/255,192/255,192/255,1))

    def _define_bindings(self):
        self._bind_to_context(nameof(self.x1), 'x1')
        self._bind_to_context(nameof(self.y1), 'y1')
        self._bind_to_context(nameof(self.x2), 'x2')
        self._bind_to_context(nameof(self.y2), 'y2')
