from kivy.properties import StringProperty

from gui.kivyhelpers import load_kv
from gui.widgets.nodeeditor.nodebodies.stacklayoutednodebodybase import StackLayoutedNodeBodyBase

load_kv(__file__)


class CsvToArrayNodeBody(StackLayoutedNodeBodyBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    csvFilePath: StringProperty = StringProperty()

    def _define_bindings(self):
        self._bind_to_context('csvFilePath', 'csvFilePath')

    def _on_context_changed(self):
        self.ids.output_field.context = self.context.output