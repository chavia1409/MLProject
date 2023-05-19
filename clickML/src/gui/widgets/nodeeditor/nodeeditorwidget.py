import uuid

from kivy.properties import ObjectProperty, Logger

from gui.kivyhelpers import load_kv
from kivy.uix.relativelayout import RelativeLayout
from gui.mvvm.contextview import ContextView
from gui.widgets.nodeeditor.nodecontainerwidget import NodeContainerWidget
from .connectionline import ConnectionLine
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from ...factories.connectiondotnodeviewmodelfactory import InputDotViewModelFactory, OutputDotViewModelFactory
from varname import nameof

from ...factories.mlcomponentnodeviewmodelfactory import MLComponentNodeViewModelFactory

load_kv(__file__)


class NodeEditorWidget(RelativeLayout, ContextView):
    __line = None

    delete_node_command = ObjectProperty(None)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_linking = False

    def _define_bindings(self):
        self._bind_to_context('delete_node_command', 'delete_node_command')

    def create_line(self, x1, y1, x2, y2):
        Logger.info(f'create_line.{x1}, {y1} {x2}, {y2}')
        line = ConnectionLine()
        line.x1 = x1
        line.x2 = x2
        line.y1 = y1
        line.y2 = y2
        self.ids.node_space.add_widget(line, -1)
        return line

    def remove_line(self, line):
        if line not in self.ids.node_space.children:
            return
        self.ids.node_space.remove_widget(line)

    def start_linking(self, x1, y1):
        self.is_linking = True
        line = ConnectionLine()
        line.x1 = x1
        line.y1 = y1
        line.x2 = x1
        line.y2 = y1
        if self.__line is not None:
            self.ids.node_space.remove_widget(self.__line)
        self.__line = line
        self.ids.node_space.add_widget(line, -1)
        return line

    def on_touch_move(self, touch):
        ret = super(NodeEditorWidget, self).on_touch_move(touch)
        if self.__line is not None:
            self.__line.x2, self.__line.y2 = self.ids.node_space.to_widget( *self.to_window(*touch.pos))
        return ret

    def on_touch_up(self, touch):
        ret = super(NodeEditorWidget, self).on_touch_up(touch)
        if self.__line is not None:
            self.is_linking = False
            self.ids.node_space.remove_widget(self.__line)
        if self.collide_point(*touch.pos) and hasattr(touch, 'componentype_to_add') and touch.componentype_to_add is not None:
            self.context.add_node(touch.componentype_to_add, *self.ids.node_space.to_widget( *self.to_window(*touch.pos)))
        if hasattr(touch, 'componentype_to_add'):
            touch.componentype_to_add = None
        return ret

    def add_node(self, node: NodeContainerWidget):
        self.ids.node_space.add_widget(node)

    def remove_node(self, node: NodeContainerWidget):
        self.ids.node_space.remove_widget(node)


    # def on_touch_down(self, touch):
    #     ret = super(NodeEditorWidget, self).on_touch_down(touch)
    #     self.add_widget(self.__line, -1)
    #     self.__line.x1, self.__line.y1 = self.to_local(*touch.pos)
    #     self.__line.x2, self.__line.y2 = self.to_local(*touch.pos)
    #
    #     return ret
    #
    # def on_touch_move(self, touch):
    #     ret = super(NodeEditorWidget, self).on_touch_move(touch)
    #     self.__line.x2, self.__line.y2 = self.to_local(*touch.pos)
    #     return ret
    #
    # def on_touch_up(self, touch):
    #     ret = super(NodeEditorWidget, self).on_touch_up(touch)
    #     self.remove_widget(self.__line)
    #     return ret


class BetterScrollView(ScrollView, RelativeLayout):

    def on_touch_move(self, touch):
        ret = False
        if self.parent.is_linking:
            return super(RelativeLayout, self).on_touch_move(touch)

        ret = super(BetterScrollView, self).on_touch_move(touch)
        return ret

    def on_touch_down(self, touch):
        x, y = touch.x, touch.y
        touch.push()
        touch.apply_transform_2d(self.to_local)
        ret = super(RelativeLayout, self).on_touch_down(touch)
        touch.pop()
        if ret is not True:
            ret = super(BetterScrollView, self).on_touch_down(touch)
        return ret

    def on_touch_up(self, touch):
        x, y = touch.x, touch.y
        touch.push()
        touch.apply_transform_2d(self.to_local)
        ret = super(RelativeLayout, self).on_touch_up(touch)
        touch.pop()
        if touch.grab_current is self:
            ret2 = super(BetterScrollView, self).on_touch_up(touch)
        return ret