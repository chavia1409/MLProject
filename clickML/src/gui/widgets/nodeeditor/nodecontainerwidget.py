from kivy.properties import ListProperty
from kivymd.uix.behaviors import HoverBehavior

from gui.kivyhelpers import load_kv
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors.drag import DragBehavior
from gui.mvvm.contextview import ContextView
from gui.factories.nodebodyfactorybase import NodeBodyFactoryBase

load_kv(__file__)


class NodeContainerWidget(HoverBehavior, DragBehavior, GridLayout, ContextView):
    __nodeBodyProvider: NodeBodyFactoryBase = None
    __nodeBody = None
    line = ListProperty((0,0,0,0))

    def __init__(self, node_body_provider: NodeBodyFactoryBase, **kwargs):
        super().__init__(**kwargs)
        self.__nodeBodyProvider = node_body_provider

    def on_enter(self):
        self.line = (120 / 255, 120 / 255, 128 / 255, 1)

    def on_leave(self):
        self.line = (0,0,0,0)

    def _on_context_changed(self):
        self.ids.header.context = self.context

        self.__change_nodebody()

        return super()._on_context_changed()

    def __change_nodebody(self):
        if self.__nodeBody is not None:
            self.remove_widget(self.__nodeBody)
            self.__nodeBody.context = None

        if self.context is not None and hasattr(self.context, 'component_type'):
            self.__nodeBody = self.__nodeBodyProvider.create(self.context.component_type)
            self.add_widget(self.__nodeBody)
            self.__nodeBody.context = self.context
            self.width = self.__nodeBody.width

    def on_touch_down(self, touch):
        ret = super(GridLayout, self).on_touch_down(touch)
        ret = super(NodeContainerWidget, self).on_touch_down(touch)
        if ret is True:
            touch.last_node = self

        if self.collide_point(*touch.pos):
            return True

    def on_touch_move(self, touch):
        ret = super(GridLayout, self).on_touch_move(touch)
        return super(NodeContainerWidget, self).on_touch_move(touch)

    def _define_bindings(self):
        self._bind_to_context('x', 'x')
        self._bind_to_context('y', 'y')

        return super()._define_bindings()

    def on_touch_up(self, touch):
        ret = super(NodeContainerWidget, self).on_touch_up(touch)
        return ret




