from kivy.properties import StringProperty, NumericProperty, BooleanProperty

from gui.kivyhelpers import load_kv
from kivy.uix.relativelayout import RelativeLayout
from gui.mvvm.contextview import ContextView
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.inputfield import InputField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.outputfield import OutputField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.multiselection import MultiSelection
from gui.widgets.nodeeditor.nodebodies.stacklayoutednodebodybase import StackLayoutedNodeBodyBase
load_kv(__file__)

class TrainFitLinNodeBody(StackLayoutedNodeBodyBase, ContextView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    test_size: StringProperty = StringProperty()
    train_size: StringProperty = StringProperty()
    random: StringProperty = StringProperty()
    shuffle = BooleanProperty(True)
    X_Plot_value: StringProperty = StringProperty()
    Y_Plot_value: StringProperty = StringProperty()

    def _define_bindings(self):
        self._bind_to_context('test_size', 'test_size')
        self._bind_to_context('train_size', 'train_size')
        self._bind_to_context('random', 'random')
        self._bind_to_context('shuffle', 'shuffle')
        self._bind_to_context('X_Plot_value', 'X_Plot_value')
        self._bind_to_context('Y_Plot_value', 'Y_Plot_value')

    def _on_context_changed(self):
        self.ids.data_input.context = self.context.data_input
        self.ids.target_input.context = self.context.target_input
        self.ids.output_regression.context = self.context.output_regression
        self.ids.output_save_csv.context = self.context.output_save_csv
        self.ids.output_plot.context = self.context.output_plot