from kivy.properties import StringProperty, ObjectProperty
from varname import nameof

from gui.kivyhelpers import load_kv
from gui.mvvm.contextview import ContextView
from gui.widgets.nodeeditor.nodebodies.stacklayoutednodebodybase import StackLayoutedNodeBodyBase
load_kv(__file__)


class TextReaderNodeBody(StackLayoutedNodeBodyBase, ContextView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    file: StringProperty = StringProperty()
    encoding: ObjectProperty = ObjectProperty()
    errors: StringProperty = StringProperty()
    newline: ObjectProperty = ObjectProperty()
    select_command = ObjectProperty()

    def _on_context_changed(self):
        self.ids.output_field.context = self.context.output

    def _define_bindings(self):
        self._bind_to_context('file', 'file')
        self._bind_to_context('encoding', 'encoding')
        self._bind_to_context('errors', 'errors')
        self._bind_to_context('newline', 'newline')
        self._bind_to_context('select_command', 'select_command')