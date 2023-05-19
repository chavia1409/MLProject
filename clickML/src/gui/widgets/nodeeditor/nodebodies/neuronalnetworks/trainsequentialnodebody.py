from kivy.properties import BooleanProperty, StringProperty, ObjectProperty, NumericProperty

from gui.kivyhelpers import load_kv
from kivy.uix.relativelayout import RelativeLayout
from gui.mvvm.contextview import ContextView
from gui.widgets.nodeeditor.nodebodies.stacklayoutednodebodybase import StackLayoutedNodeBodyBase
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.inputfield import InputField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.outputfield import OutputField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.labeledcheckbox import LabeledCheckBox
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.multiselection import MultiSelection
load_kv(__file__)


class TrainSequentialNodeBody(StackLayoutedNodeBodyBase, ContextView):
    batch_size_enabled = BooleanProperty()
    batch_size = StringProperty()

    epochs_enabled = BooleanProperty()
    epochs = StringProperty()

    selected_verbose_mode = ObjectProperty()

    validation_split_enabled = BooleanProperty()
    validation_split_percent = NumericProperty()

    plot_progress = BooleanProperty()
    save_weights = BooleanProperty()

    def _define_bindings(self):
        self._bind_to_context('batch_size_enabled', 'batch_size_enabled')
        self._bind_to_context('batch_size', 'batch_size')
        self._bind_to_context('epochs_enabled', 'epochs_enabled')
        self._bind_to_context('epochs', 'epochs')
        self._bind_to_context('selected_verbose_mode', 'selected_verbose_mode')
        self._bind_to_context('validation_split_enabled', 'validation_split_enabled')
        self._bind_to_context('validation_split_percent', 'validation_split_percent')
        self._bind_to_context('plot_progress', 'plot_progress')
        self._bind_to_context('save_weights', 'save_weights')
        self._bind_to_context('plot_progress', 'plot_progress')
        self._bind_to_context('save_weights', 'save_weights')




    def _on_context_changed(self):
        self.ids.training_net_input.context = self.context.training_net_input
        self.ids.training_net_output.context = self.context.training_net_output
        self.ids.model_input.context = self.context.model_input
        self.ids.model_output.context = self.context.model_output