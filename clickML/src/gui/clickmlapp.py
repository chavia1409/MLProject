import os
import sys

from gui import style

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import kivy
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from gui.screens.editorscreen import EditorScreen
from kivy.core.window import Window
from gui.configure import configure
Window.maximize()

kivy.require('2.1.0')

class ClickMLApp(MDApp):
    def build(self):
        self.icon = 'logo_light.png'
        sm = ScreenManager()
        editor_screen = EditorScreen(name="EditorScreen")
        sm.add_widget(editor_screen)
        editor_screen.context = configure(editor_screen.ids.node_editor, editor_screen.ids.terminal_widget, editor_screen.ids.ComponentList_widget)
        return sm

if __name__ == '__main__':

    ClickMLApp().run()