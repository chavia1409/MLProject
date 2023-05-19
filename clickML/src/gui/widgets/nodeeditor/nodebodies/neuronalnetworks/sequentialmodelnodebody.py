from kivy.properties import BooleanProperty, StringProperty, ListProperty, ObjectProperty
from kivy.uix.stacklayout import StackLayout
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from gui import style
from gui.kivyhelpers import load_kv
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
#from kivymd.uix.expansionpanel.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from gui.mvvm.contextview import ContextView
from gui.widgets.nodeeditor.nodebodies.neuronalnetworks.centercropcontent import CenterCropContent
from gui.widgets.nodeeditor.nodebodies.neuronalnetworks.conv2d import Conv2DContent
from gui.widgets.nodeeditor.nodebodies.neuronalnetworks.densecontent import DenseContent
from gui.widgets.nodeeditor.nodebodies.neuronalnetworks.dropoutcontent import DropoutContent
from gui.widgets.nodeeditor.nodebodies.neuronalnetworks.flattencontent import FlattenContent
from gui.widgets.nodeeditor.nodebodies.neuronalnetworks.grucontent import GRUContent
from gui.widgets.nodeeditor.nodebodies.neuronalnetworks.lstmcontent import LSTMContent
from gui.widgets.nodeeditor.nodebodies.neuronalnetworks.maxpool2dcontent import MaxPool2DContent
from gui.widgets.nodeeditor.nodebodies.neuronalnetworks.rescaling import RescalingContent
from gui.widgets.nodeeditor.nodebodies.neuronalnetworks.resizingcontet import ResizingContent
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.inputfield import InputField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.outputfield import OutputField
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.labeledcheckbox import LabeledCheckBox
from kivymd.uix.menu import MDDropdownMenu
from gui.widgets.nodeeditor.nodebodies.stacklayoutednodebodybase import StackLayoutedNodeBodyBase
load_kv(__file__)


class SequentialModelNodeBody(GridLayout, ContextView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layer_names_types = {
            'Dense': 'Dense',
            'Dropout': 'Dropout',
            'LSTM': 'Long Short-Term Memory layer',
            'conv2D_Layer': 'Conv2D',
            'MaxPool2DLayerComponent': 'MaxPool',
            'Flatten': 'Flatten',
            'RescalingLayer':'Rescaling',
            'CenterCrop':'CenterCrop',
            'GRU':'GRU',
            'Resizing':'Resizing',
        }
        menu_items = [
            {
                "text_color": [1.0, 1.0, 1.0, 1.0],
                "theme_text_color": 'Custom',
                "text": f"{self.layer_names_types[key]}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=key: self._add_layer_by_key(x),
            } for key in self.layer_names_types
        ]
        self.menu = MDDropdownMenu(
            background_color=style.header_backgorund_color,
            caller=self.ids.add_layer_button,
            items=menu_items,
            width_mult=4,
        )
    name_enabled = BooleanProperty(True)
    name = StringProperty()

    weight_file_enabled = BooleanProperty()
    weight_file_path = StringProperty()

    layers = ListProperty()

    optimizer = ObjectProperty()

    loss_funktion = StringProperty()

    metric_functions = ListProperty([])

    def _define_bindings(self):
        self._bind_to_context('name_enabled', 'name_enabled')
        self._bind_to_context('name', 'name')
        self._bind_to_context('weight_file_enabled', 'weight_file_enabled')
        self._bind_to_context('weight_file_path', 'weight_file_path')
        self._bind_to_context('layers', 'layers')
        self._bind_to_context('loss_funktion', 'loss_function')
        self._bind_to_context('metric_functions', 'metric_functions')
        self._bind_to_context('optimizer', 'optimizer')




    def on_layers(self, ins, value):
        for widget in self.ids.layers_list.children.copy():
            self.ids.layers_list.remove_widget(widget)
        for layer in value:
            layer_view = LayerView()
            layer_view.context = layer
            self.ids.layers_list.add_widget(layer_view)

    def on_metric_functions(self, ins, value):
        for widget in self.ids.metrics_list.children.copy():
            self.ids.metrics_list.remove_widget(widget)
        for metric_function in value:
            view = MetricFunctionView()
            view.context = metric_function
            self.ids.metrics_list.add_widget(view)

    def add_metric_function(self):
        self.context.add_metric('')

    def _on_context_changed(self):
        self.ids.input_shape.context = self.context.input_shape
        self.ids.output_shape.context = self.context.output_shape
        self.ids.output_model.context = self.context.model_output

    def add_layer(self):
        self.menu.open()

    def _add_layer_by_key(self, key):
        self.menu.dismiss()
        self.context.add_layer(key)



class LayerView(GridLayout, ContextView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    layer_name = StringProperty()

    def remove(self):
        self.context.delete()

    def _define_bindings(self):
        self._bind_to_context('layer_name', 'name')

    def _on_context_changed(self):
        if self.context is None:
            return
        content = None
        if self.context.component_type == 'Dropout':
            content = DropoutContent()
        if self.context.component_type == 'Dense':
            content = DenseContent()
        if self.context.component_type == 'LSTM':
            content = LSTMContent()
        if self.context.component_type == 'Flatten':
            content = FlattenContent()
        if self.context.component_type == 'MaxPool2DLayerComponent':
            content = MaxPool2DContent()
        if self.context.component_type == 'conv2D_Layer':
            content = Conv2DContent()
        if self.context.component_type == 'RescalingLayer':
            content = RescalingContent()
        if self.context.component_type == 'CenterCrop':
            content = CenterCropContent()
        if self.context.component_type == 'GRU':
            content = GRUContent()
        if self.context.component_type == 'Resizing':
            content = ResizingContent()

        if content is None:
            return
        content.context = self.context

        self.__dialog = MDDialog(
                title="[color=038AFF]"+self.context.name+'[/color]',
                type="custom",
                height=dp(200),
                content_cls=content,
                md_bg_color=style.header_backgorund_color,
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=(1,1,1,1),
                        on_press= lambda x: self.__dialog.dismiss()
                    ),
                ],
            )

    def open_edit(self):
        if self.__dialog is None:
            return
        self.__dialog.open()

class MetricFunctionView(GridLayout, ContextView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    name = StringProperty()

    def _define_bindings(self):
        self._bind_to_context('name', 'name')