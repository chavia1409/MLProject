from kivy.properties import StringProperty, NumericProperty, ObjectProperty

from gui.kivyhelpers import load_kv
from kivy.uix.relativelayout import RelativeLayout
from gui.mvvm.contextview import ContextView
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.inputfield import InputField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.outputfield import OutputField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.multiselection import MultiSelection
from gui.widgets.nodeeditor.nodebodies.stacklayoutednodebodybase import StackLayoutedNodeBodyBase
load_kv(__file__)

class PredictNodeBody(StackLayoutedNodeBodyBase, ContextView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    from_column: StringProperty = StringProperty()
    to_column: StringProperty = StringProperty()
    from_row: StringProperty = StringProperty()
    to_row: StringProperty = StringProperty()
    prediction_type: ObjectProperty = ObjectProperty()

    def _define_bindings(self):
        self._bind_to_context('from_column', 'from_column')
        self._bind_to_context('to_column', 'to_column')
        self._bind_to_context('from_row', 'from_row')
        self._bind_to_context('to_row', 'to_row')
        self._bind_to_context('prediction_type', 'prediction_type')

    def _on_context_changed(self):
        self.ids.model_input.context = self.context.model_input
        self.ids.output_regression.context = self.context.output_regression
        self.ids.output_save_csv.context = self.context.output_save_csv
        self.ids.output_plot.context = self.context.output_plot