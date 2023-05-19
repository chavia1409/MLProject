from gui.kivyhelpers import load_kv
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty, NumericProperty
from kivy.metrics import dp
load_kv(__file__)

class NodeBodyTextField(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    field_text: StringProperty = StringProperty()
    label_text: StringProperty = StringProperty()
    label_width: StringProperty = NumericProperty(dp(50))