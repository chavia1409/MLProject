from kivy.properties import StringProperty, NumericProperty

from gui.kivyhelpers import load_kv
from kivy.uix.relativelayout import RelativeLayout
from gui.mvvm.contextview import ContextView
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.inputfield import InputField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.outputfield import OutputField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.multiselection import MultiSelection
from varname import nameof
from gui.widgets.nodeeditor.nodebodies.stacklayoutednodebodybase import StackLayoutedNodeBodyBase
load_kv(__file__)


class GenerateCharsNodeBody(StackLayoutedNodeBodyBase, ContextView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    init_chars: StringProperty = StringProperty()
    number_of_chars: NumericProperty = NumericProperty(0)

    def _define_bindings(self):
        self._bind_to_context('init_chars', 'init_chars_mode')
        self._bind_to_context('number_of_chars', 'number_of_chars')


    def _on_context_changed(self):
        self.ids.model_input.context = self.context.model_iput
        self.ids.init_chars_input.context = self.context.init_chars_input
        self.ids.output.context = self.context.generate_text_output

