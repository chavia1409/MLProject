from kivy.properties import StringProperty, NumericProperty, BooleanProperty

from gui.kivyhelpers import load_kv
from gui.converter.booltostrconverter import BoolToStrConverter
from kivy.uix.relativelayout import RelativeLayout
from gui.mvvm.contextview import ContextView
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.inputfield import InputField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.outputfield import OutputField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.multiselection import MultiSelection
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.labeledcheckbox import LabeledCheckBox
from gui.widgets.nodeeditor.nodebodies.stacklayoutednodebodybase import StackLayoutedNodeBodyBase
load_kv(__file__)

class ScoreNodeBody(StackLayoutedNodeBodyBase, ContextView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    print = BooleanProperty(True)

    def _define_bindings(self):
        self._bind_to_context('print', 'print')

    def _on_context_changed(self):
        self.ids.regression_input.context = self.context.regression_input
        self.ids.output.context = self.context.output

