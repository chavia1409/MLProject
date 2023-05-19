from kivy.properties import ObjectProperty, ListProperty

from kivy.uix.label import Label

from kivymd.uix.behaviors import HoverBehavior, RectangularElevationBehavior, FocusBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatIconButton

from gui.kivyhelpers import load_kv
from kivy.uix.boxlayout import BoxLayout
from gui.mvvm.contextview import ContextView

load_kv(__file__)


class TerminalWidget(HoverBehavior, BoxLayout, ContextView):
    run_command = ObjectProperty(None)
    preview_command = ObjectProperty(None)
    translate_command = ObjectProperty(None)
    save_command = ObjectProperty(None)
    load_command = ObjectProperty(None)
    blue =((3/255, 138/255, 1, 1))
    pink = ((1, 20/255, 147/255,1))
    orange = ((1,70/255,0, 1))
    green = ((0, 230/255, 64/255, 1))
    yellow = ((1,1,0,1))
    purple = ((1,0,1,1))
    gray = ((120 / 255, 120 / 255, 128 / 255, 1))

    line_save =ListProperty((3/255, 138/255, 1, 1))
    line_load = ListProperty((3/255, 138/255, 1, 1))
    line_translate = ListProperty((3/255, 138/255, 1, 1))
    line_run = ListProperty((3/255, 138/255, 1, 1))
    line_preview =ListProperty((3/255, 138/255, 1, 1))
    line_terminal =ListProperty((3/255, 138/255, 1, 1))


    def on_enter(self):
        self.line_save = self.gray
        self.line_load = self.gray
        self.line_translate = self.gray
        self.line_run = self.gray
        self.line_preview = self.gray

    def on_leave(self):
        self.line_save = self.blue
        self.line_load = self.blue
        self.line_translate = self.blue
        self.line_run = self.blue
        self.line_preview = self.blue

    def button_color_touch_down(self, button):
        match button:
            case 'save':
                self.line_save = self.yellow
                return

            case 'load':
                self.line_load = self.yellow
                return
            case 'translate':
                self.line_translate = self.yellow
                return
            case 'run':
                self.line_run = self.yellow
                return
            case 'preview':
                self.line_preview = self.yellow
                return

    def button_color_touch_up(self, button):
        match button:
            case "save":
                self.line_save = self.gray
                return
            case 'load':
                self.line_load = self.gray
                return
            case 'translate':
                self.line_translate = self.gray
                return
            case 'run':
                self.line_run = self.gray
                return
            case 'preview':
                self.line_preview = self.gray
                return

    def _define_bindings(self):
        self._bind_to_context("run_command", 'run_command')
        self._bind_to_context("translate_command", 'translate_command')
        self._bind_to_context("preview_command", 'preview_command')
        self._bind_to_context("save_command", 'save_command')
        self._bind_to_context("load_command", 'load_command')


class TerminalOutputLabel(Label):
    pass

class FocusWidget(MDBoxLayout, FocusBehavior):
    pass
