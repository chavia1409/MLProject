import KivyHelpers
from varname import nameof
from kivy.uix.recycleview import RecycleView
from kivy.properties import StringProperty, NumericProperty, ListProperty, AliasProperty
from mvvm.BindableView import BindableView

KivyHelpers.loadKv(__file__)

class ResultsListWidget(RecycleView, BindableView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = self.results
    
    results:ListProperty = ListProperty() 

    def on_results(self, instance, value):
        self.data = [{'text': str(x)} for x in self.results] 
    def _defineBindings(self):
        self._bindToContext(nameof(self.results), "oldResults")