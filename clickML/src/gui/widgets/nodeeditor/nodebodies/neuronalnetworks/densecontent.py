from kivy.properties import StringProperty, BooleanProperty

from gui.kivyhelpers import load_kv
from kivy.uix.stacklayout import StackLayout
from gui.mvvm.contextview import ContextView
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.nodebodytextfield import NodeBodyTextField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.labeledcheckbox import LabeledCheckBox

load_kv(__file__)


class DenseContent(StackLayout, ContextView):

    units = StringProperty()
    activation_enabled = BooleanProperty()
    activation = StringProperty()

    def _define_bindings(self):
        self._bind_to_context('units', 'units')
        self._bind_to_context('activation_enabled', 'activation_enabled')
        self._bind_to_context('activation', 'activation')