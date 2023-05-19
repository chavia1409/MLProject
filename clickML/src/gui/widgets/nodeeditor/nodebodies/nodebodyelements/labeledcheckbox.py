from kivy.properties import BooleanProperty, StringProperty, NumericProperty

from gui.kivyhelpers import load_kv
from kivy.uix.stacklayout import StackLayout
from gui.mvvm.contextview import ContextView



load_kv(__file__)
class LabeledCheckBox(StackLayout, ContextView):
    def __init__(self, **kwargs):
        super(LabeledCheckBox, self).__init__(**kwargs)

    is_checked: BooleanProperty = BooleanProperty(False)
    label_text: StringProperty = StringProperty()



