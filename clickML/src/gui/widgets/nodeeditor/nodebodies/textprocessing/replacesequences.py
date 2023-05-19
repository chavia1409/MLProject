from kivy.properties import StringProperty, ObjectProperty, ListProperty
from varname import nameof

from gui.kivyhelpers import load_kv
from gui.widgets.nodeeditor.nodebodies.stacklayoutednodebodybase import StackLayoutedNodeBodyBase

load_kv(__file__)


class ReplaceSequencesNodeBody(StackLayoutedNodeBodyBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    sequences_original: list[StringProperty] = ObjectProperty([])
    sequences_replace: list[StringProperty] = ObjectProperty([])

    def _define_bindings(self):
        self._bind_to_context('sequences_original', 'sequences_original')
        self._bind_to_context('sequences_replace', 'sequences_replace')

    def _on_context_changed(self):
        self.ids.input_field.context = self.context.input
        self.ids.output_field.context = self.context.output
