from gui.kivyhelpers import load_kv
from kivy.uix.relativelayout import RelativeLayout
from gui.mvvm.contextview import ContextView
from kivy.properties import StringProperty, NumericProperty, Logger, BooleanProperty

from .connectiondotbase import ConnectionDotBase
load_kv(__file__)


class InputField(RelativeLayout, ConnectionDotBase):
    label_text: StringProperty = StringProperty()
    label_italic = BooleanProperty(False)
    label_bold = BooleanProperty(False)

    def handle_touch_down(self, dot, touch):
        if dot.collide_point(*touch.pos):
            if self.context is not None:
                self.context.drag_command()
            return False

    def handle_touch_up(self, dot, touch):
        if dot.collide_point(*touch.pos):
            if self.context is not None:
                self.context.drop_command()
            return False
