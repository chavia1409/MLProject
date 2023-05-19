from kivy.properties import BooleanProperty, StringProperty

from gui.converter.booltostrconverter import BoolToStrConverter
from gui.kivyhelpers import load_kv
from kivy.uix.stacklayout import StackLayout
from gui.mvvm.contextview import ContextView
from gui.widgets.nodeeditor.nodebodies.stacklayoutednodebodybase import StackLayoutedNodeBodyBase
from  gui.widgets.nodeeditor.nodebodies.nodebodyelements.labeledcheckbox import LabeledCheckBox
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.outputfield import OutputField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.inputfield import InputField
from varname import nameof

load_kv(__file__)

class LetterCaseNodeBody(StackLayoutedNodeBodyBase):
    def __init__(self, **kwargs):
        super(LetterCaseNodeBody, self).__init__(**kwargs)
        self.bind(is_upper= self.callback)
    is_upper = BooleanProperty(True)
    is_lower = BooleanProperty(False)

    def callback(self, x,y):
        pass

    def _define_bindings(self):
        self._bind_to_context('is_upper', 'is_upper_case')
        self._bind_to_context('is_lower', 'is_lower_case')

    def _on_context_changed(self):
        if self.context is not None:
            self.ids.output.context = self.context.output
            self.ids.input.context = self.context.input

