from kivy.uix.label import Label
from kivy.uix.treeview import TreeViewLabel, TreeView, TreeViewNode
from kivymd.uix.label import MDLabel
from gui.kivyhelpers import load_kv
from kivy.uix.boxlayout import BoxLayout
from gui.mvvm.contextview import ContextView
from kivy.uix.label import Label
from kivy.metrics import dp
from gui.services.componentlistservice import ComponentListService
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

load_kv(__file__)


class ComponentListWidget(BoxLayout, ContextView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tv = TreeView(hide_root=True)
        self.add_widget(self.tv)

    def buildTreeView(self, componentList):
        parentNodes = []
        rootNode = self.tv.add_node((TreeViewLabel(text='', is_open=True)))
        rootNodeEmpty = True
        for name, descriptor, parent in componentList.get_list():
            if parent is not None:
                if not parentNodes.__contains__(parent):
                    parentNode = self.tv.add_node(TreeViewLabel(text=parent, is_open=True))
                    parentNodes.append(parent)
                self.tv.add_node(ComponentTreeViewNode(text=name, nodebodyType=descriptor), parentNode)
            else:
                self.tv.add_node(ComponentTreeViewNode(text=name, nodebodyType=descriptor), rootNode)
                rootNodeEmpty = False
        if rootNodeEmpty:
            self.tv.remove_node(rootNode)


class ComponentTreeViewNode(Label, TreeViewNode, ContextView):

    def __init__(self, nodebodyType, **kwargs):
        super(ComponentTreeViewNode, self).__init__(**kwargs)
        self.nodebodyType = nodebodyType
        self.size_hint = 1, None
        self.height = dp(25)

    __drag = None

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            x, y = self.to_widget(*touch.pos)
            self.__drag = MDLabel(text=self.text, x=x, y=y - 50)
            self.parent.add_widget(self.__drag)
            touch.componentype_to_add = self.nodebodyType

    def on_touch_move(self, touch):
        if self.__drag is not None:
            x, y = self.to_widget(*touch.pos)
            self.__drag.x = x
            self.__drag.y = y - 50

    def on_touch_up(self, touch):
        if self.__drag is not None:
            self.parent.remove_widget(self.__drag)
