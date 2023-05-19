from gui.kivyhelpers import load_kv
from kivy.properties import StringProperty, ObjectProperty
from gui.widgets.nodeeditor.nodebodies.stacklayoutednodebodybase import StackLayoutedNodeBodyBase
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.inputfield import InputField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.outputfield import OutputField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.nodebodytextfield import NodeBodyTextField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.multiselection import MultiSelection
from common.models.component_descriptors.component_constants import DEFAULT
load_kv(__file__)

class SaveTextNodeBody(StackLayoutedNodeBodyBase):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    path: StringProperty = StringProperty()
    encoding: ObjectProperty = ObjectProperty()
    errors: StringProperty = StringProperty()
    newline: ObjectProperty = ObjectProperty()

    def _define_bindings(self):
        self._bind_to_context('path', 'path')
        self._bind_to_context('encoding', 'encoding')
        self._bind_to_context('errors', 'errors')
        self._bind_to_context('newline', 'newline')

    def _on_context_changed(self):
        self.ids.input_field.context = self.context.input
        self.ids.output_field.context = self.context.output
        
    
    
