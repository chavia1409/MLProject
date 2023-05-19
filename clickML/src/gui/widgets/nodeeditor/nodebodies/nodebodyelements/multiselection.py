import uuid

from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineAvatarIconListItem

from gui import style
from gui.kivyhelpers import load_kv
from kivy.uix.button import Button
from gui.mvvm.contextview import ContextView

load_kv(__file__)


class MultiSelection(Button, ContextView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(selected_item= self.selected_item_changed)

    selected_item: ObjectProperty = ObjectProperty()
    items: ListProperty = ListProperty([])

    def selected_item_changed(self, y, z):
        v = next(filter(lambda x: x[0] == z, self.items), None)
        if v is None:
            return
        self.text = v[1]

    def set_selection(self, value):
        self.menu.dismiss()
        if self.selected_item == value:
            return
        self.selected_item = value


    def on_items(self, ins, value):
        self.menu_items = []
        for v in value:
            self.menu_items.append({
                "text_color": [1.0, 1.0, 1.0, 1.0],
                "theme_text_color": 'Custom',
                "text": f"{v[1]}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=v[0]: self.set_selection(x),
            })
        self.menu = MDDropdownMenu(
            background_color = style.header_backgorund_color,
            caller=self,
            items=self.menu_items,
            width_mult=3,
        )

    def on_press(self):
        self.menu.open()
