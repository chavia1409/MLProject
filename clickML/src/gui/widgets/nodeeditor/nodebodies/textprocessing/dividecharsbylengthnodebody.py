from kivy.properties import NumericProperty, ListProperty, StringProperty

from gui.kivyhelpers import load_kv
from gui.widgets.nodeeditor.nodebodies.stacklayoutednodebodybase import StackLayoutedNodeBodyBase

load_kv(__file__)


class DivideCharsByLengthNodeBody(StackLayoutedNodeBodyBase):
    input_text_background = ListProperty((1, 1, 1, 1))
    input_text: StringProperty = StringProperty()
    prediction_input: StringProperty = StringProperty()
    seq_length: NumericProperty = NumericProperty(0)


    def set_seq_length(self):
        self.seq_length = self.ids.textinput.text
        self.input_text_background = (1, 1, 1, 1)

    def change_text_input_color(self, value):
        self.input_text_background = value

    def _on_context_changed(self):
        self.ids.input_field.context = self.context.input_text
        self.ids.output_field.context = self.context.prediction_input
        self.ids.output_field_2.context = self.context.net_input
        self.ids.output_field_3.context = self.context.net_output
        self.ids.output_field_4.context = self.context.input_shape
        self.ids.output_field_5.context = self.context.output_shape

    def _define_bindings(self):
        self._bind_to_context('seq_length', 'seq_length')
