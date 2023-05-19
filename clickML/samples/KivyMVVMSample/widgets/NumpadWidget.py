import KivyHelpers
from varname import nameof
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, ObjectProperty
from mvvm.BindableView import BindableView

KivyHelpers.loadKv(__file__)

class NumpadWidget(GridLayout, BindableView): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    result = NumericProperty(0)

    clickCommand:ObjectProperty = None
    changeModeCommand:ObjectProperty = None
    cancelCommand:ObjectProperty = None
    
    def _defineBindings(self):
        self._bindToContext(nameof(self.result), "calcResult")
        self._bindToContext(nameof(self.clickCommand), "clickCommand")
        self._bindToContext(nameof(self.changeModeCommand), "changeModeCommand")
        self._bindToContext(nameof(self.cancelCommand), "cancelCommand")
