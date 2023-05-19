from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivymd.uix.button import MDRectangleFlatIconButton

from gui.services.terminalserviecebase import TerminalServiceBase
from gui.widgets.terminalwidget import TerminalOutputLabel


class TerminalService(TerminalServiceBase):
    def __init__(self, terminal_widget):
        self.__terminal_widget = terminal_widget
        self.__max_width = 1000

    def create_popup(self, title: str, text: str, size_x, size_y, add_scroll_x:bool=False):
        popup_label = TerminalOutputLabel(text=text)
        popup_label.size_hint = (1, 1)
        scroll = ScrollView()
        scroll.add_widget(popup_label)
        if add_scroll_x:
            popup_label.size_hint = (None, None)
            popup_label.width = max(size_x, (popup_label.width))
            popup_label.height = 4 *  dp(size_y)

        popup = Popup(title=title,
                      title_size=dp(16),
                      content=scroll,
                      separator_color=(0,0,0,0),
                      title_color=(3/255, 138/255, 1, 1),
                      size_hint=(None, None), size=(dp(size_x), dp(size_y)))

        popup.open()

    def write_line(self, text: str):
        label = TerminalOutputLabel(text=text, markup=True)
        self.__terminal_widget.ids.output_stack.add_widget(label)
        self.__terminal_widget.ids.output_stack.width = self.max_width(label)

    def add_text_with_icon(self, text: str, icon: str, color):
        btn = MDRectangleFlatIconButton(text=text,
                                        text_color=color,
                                        icon=icon,
                                        icon_color=color,
                                        line_color=(0, 0, 0, 0))
        self.__terminal_widget.ids.output_stack.add_widget(btn)

    def max_width(self, label: Label):
        self.__max_width = max(self.__max_width, (len(label.text) * label.font_size) /2 )
        return self.__max_width

    def disable_translate(self):
        self.__terminal_widget.ids.translate.disabled = True

    def disable_preview(self):
        self.__terminal_widget.ids.preview.disabled = True

    def disable_run(self):
        self.__terminal_widget.ids.run.disabled = True

    def enable_preview(self):
        self.__terminal_widget.ids.preview.disabled = False

    def enable_translate(self):
        self.__terminal_widget.ids.translate.disabled = False

    def enable_run(self):
        self.__terminal_widget.ids.run.disabled = False

