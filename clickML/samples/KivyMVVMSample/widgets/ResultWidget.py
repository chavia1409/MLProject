import KivyHelpers
from varname import nameof
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty
from mvvm.BindableView import BindableView
KivyHelpers.loadKv(__file__)

class ResultWidget(BoxLayout, BindableView):

    result = NumericProperty(0)
    mode:StringProperty = StringProperty()

    def _defineBindings(self):
        self._bindToContext(nameof(self.result), "calcResult")
        self._bindToContext(nameof(self.mode), "mode")