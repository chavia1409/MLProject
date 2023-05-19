
from kivy.properties import StringProperty, NumericProperty, ObjectProperty, ListProperty
from varname import nameof
from gui.kivyhelpers import load_kv
from gui.mvvm.contextview import ContextView
from gui.widgets.nodeeditor.nodebodies.stacklayoutednodebodybase import StackLayoutedNodeBodyBase
load_kv(__file__)


class DivideWordsBySentencesNodeBody(StackLayoutedNodeBodyBase, ContextView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    input_text_background = ListProperty((1, 1, 1, 1))
    input_text: StringProperty = StringProperty()
    prediction_input: StringProperty = StringProperty()
    max_seq_length: NumericProperty = NumericProperty(0)

    def set_seq_length(self):
        self.max_seq_length = self.ids.textinput.text
        self.input_text_background = ((1, 1, 1, 1))

    def change_text_input_color(self, value):
        self.input_text_background = value

    def _on_context_changed(self):
        self.ids.input_text.context = self.context.input_text
        self.ids.prediction_input.context = self.context.prediction_input
        self.ids.net_input.context = self.context.net_input
        self.ids.net_output.context = self.context.net_output
        self.ids.input_shape.context = self.context.input_shape
        self.ids.output_shape.context = self.context.output_shape

    def _define_bindings(self):
        self._bind_to_context('max_seq_length', 'max_seq_length')