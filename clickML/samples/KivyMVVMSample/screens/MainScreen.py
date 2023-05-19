import KivyHelpers
from kivy.uix.screenmanager import Screen
from ViewModels.CalculatorViewModel import CalculatorViewModel

KivyHelpers.loadKv(__file__)

class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        vm = CalculatorViewModel()
        self.ids.resultWidget.context = vm
        self.ids.numpadWidget.context = vm
        self.ids.resultsListWidget.context = vm