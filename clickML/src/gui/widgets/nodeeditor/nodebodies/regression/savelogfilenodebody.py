from gui.kivyhelpers import load_kv
from kivy.properties import StringProperty, ObjectProperty
from gui.widgets.nodeeditor.nodebodies.stacklayoutednodebodybase import StackLayoutedNodeBodyBase
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.inputfield import InputField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.outputfield import OutputField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.nodebodytextfield import NodeBodyTextField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.multiselection import MultiSelection
from common.models.component_descriptors.component_constants import DEFAULT

load_kv(__file__)


class SaveLogfileNodeBody(StackLayoutedNodeBodyBase):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    filePath: StringProperty = StringProperty()

    def _define_bindings(self):
        self._bind_to_context('filePath', 'filePath')

    def _on_context_changed(self):
        self.ids.input_field.context = self.context.input



