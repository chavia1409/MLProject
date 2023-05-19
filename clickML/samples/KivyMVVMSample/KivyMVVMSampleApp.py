import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from screens import MainScreen
from kivy.factory import Factory

class KivyMVVMSampleApp(App):
    def build(self):
        
        sm = ScreenManager()
        
        sm.add_widget(MainScreen.MainScreen(name="Main"))
        return sm
if __name__ == '__main__':
    KivyMVVMSampleApp().run()