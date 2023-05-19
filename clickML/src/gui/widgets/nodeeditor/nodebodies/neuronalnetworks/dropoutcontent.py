from kivy.properties import NumericProperty, StringProperty, BooleanProperty

from gui.kivyhelpers import load_kv
from kivy.uix.stacklayout import StackLayout
from gui.mvvm.contextview import ContextView
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.nodebodytextfield import NodeBodyTextField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.labeledcheckbox import LabeledCheckBox
load_kv(__file__)


class DropoutContent(StackLayout, ContextView):

    rate_in_percent = NumericProperty(0)
    seed = StringProperty()
    seed_enabled = BooleanProperty(True)
    def _define_bindings(self):
        self._bind_to_context('rate_in_percent', 'rate_in_percent')
        self._bind_to_context('seed', 'seed')
        self._bind_to_context('seed_enabled', 'seed_enabled')