from kivy.properties import StringProperty, BooleanProperty

from gui.kivyhelpers import load_kv
from gui.widgets.nodeeditor.nodebodies.stacklayoutednodebodybase import StackLayoutedNodeBodyBase

load_kv(__file__)


class SaveToArrayOrCsvNodeBody(StackLayoutedNodeBodyBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    ArrayOrCsv: StringProperty = StringProperty()
    targetFilePath: StringProperty = StringProperty()
    # targetFileName: StringProperty = StringProperty()
    # arrayName: StringProperty = StringProperty()
    indexing: BooleanProperty = BooleanProperty()

    def _define_bindings(self):
        self._bind_to_context('ArrayOrCsv', 'ArrayOrCsv')
        self._bind_to_context('targetFilePath', 'targetFilePath')
        # self._bind_to_context('targetFileName', 'targetFileName')
        # self._bind_to_context('arrayName', 'arrayName')
        self._bind_to_context('indexing', 'indexing')

    def _on_context_changed(self):
        self.ids.output_field.context = self.context.output
        self.ids.input_field.context = self.context.input