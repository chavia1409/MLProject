from kivy.graphics import Color
from kivy.properties import ObjectProperty, ListProperty
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.label import MDIcon

from gui.kivyhelpers import load_kv

from gui.mvvm.contextview import ContextView

load_kv(__file__)


class BinWidget(HoverBehavior, MDIcon, ContextView):
    command = ObjectProperty(None)
    bin_color = ListProperty((192/255,192/255,192/255,1))

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos) and hasattr(touch, 'last_node'):
            if self.command is not None:
                self.command.invoke(touch.last_node.context)

    def on_enter(self):
        self.bin_color = (1,0,0,1)

    def on_leave(self):
        self.bin_color = ((192/255,192/255,192/255,1))