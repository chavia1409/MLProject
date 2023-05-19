from kivy.properties import NumericProperty, BooleanProperty

from gui.kivyhelpers import load_kv
from gui.widgets.nodeeditor.nodebodies.stacklayoutednodebodybase import StackLayoutedNodeBodyBase

load_kv(__file__)


class PrintTextNodeBody(StackLayoutedNodeBodyBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    number_of_chars_enabled = BooleanProperty(True)
    number_of_chars = NumericProperty()

    def _define_bindings(self):
        self._bind_to_context('number_of_chars_enabled', 'number_of_chars_enabled')
        self._bind_to_context('number_of_chars', 'number_of_chars')

    def _on_context_changed(self):
        self.ids.input_field.context = self.context.input
        self.ids.output_field.context = self.context.output

