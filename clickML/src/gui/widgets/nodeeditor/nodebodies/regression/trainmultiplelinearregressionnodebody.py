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

class TrainMultipleLinearRegressionNodeBody(StackLayoutedNodeBodyBase, ContextView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        test_size: NumericProperty = NumericProperty(0.25)
        train_size: NumericProperty = NumericProperty(0.75)
        random_int: NumericProperty = NumericProperty()

    def _define_bindings(self):
        self._bind_to_context(nameof(self.test_size), 'test_size')
        self._bind_to_context(nameof(self.train_size), 'train_size')
        self._bind_to_context(nameof(self.random_int), 'random_int')

    def _on_context_changed(self):
        self.ids.data_input.context = self.context.data_input
        self.ids.target_input.context = self.context.target_input
        self.ids.output_regression.context = self.context.output_regression
        self.ids.output_save_csv.context = self.context.output_save_csv
        self.ids.output_plot.context = self.context.output_plot