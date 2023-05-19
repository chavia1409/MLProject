from kivy.metrics import dp
from kivy.properties import ObjectProperty, NumericProperty, ListProperty, StringProperty, BooleanProperty
from kivymd.uix.behaviors import FocusBehavior
from kivymd.uix.boxlayout import MDBoxLayout

from gui.kivyhelpers import load_kv
from gui.mvvm.contextview import ContextView
from gui.widgets.nodeeditor.nodebodies.nodebodyelements.nodebodytextfield import NodeBodyTextField
from gui.widgets.nodeeditor.nodebodies.stacklayoutednodebodybase import StackLayoutedNodeBodyBase

load_kv(__file__)


class ImageDatasetNodeBody(StackLayoutedNodeBodyBase, ContextView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    directory = StringProperty()
    labels = ObjectProperty()
    label_mode = ObjectProperty()
    color_mode = ObjectProperty()
    batch_size = NumericProperty()
    image_size = ObjectProperty()
    shuffle = BooleanProperty()
    validation_split = NumericProperty(0.0)
    seed = StringProperty()
    interpolation = ObjectProperty()
    crop_to_aspect_ratio = BooleanProperty()
    class_name_counter = NumericProperty(1)
    select_path = ObjectProperty()

    image_size_x = NumericProperty(256)
    image_size_y = NumericProperty(256)


    def set_validation_split(self):
        try:
            float(self.ids.validation_split_input.text)
            self.validation_split = float(self.ids.validation_split_input.text)
        except:
            self.validation_split = 0.0


    def set_image_size_x(self):
        try:
            float(self.ids.image_input_x.text)
            self.image_size_x = int(self.ids.image_input_x.text)
        except:
            self.image_size_x=256

    def set_image_size_y(self):
        try:
            float(self.ids.image_input_y.text)
            self.image_size_y = int(self.ids.image_input_y.text)


        except:
            self.image_size_x = 256
    def set_batch_size(self):
        try:
            float(self.ids.batch_input.text)
            self.batch_size = int(self.ids.batch_input.text)
        except:
            self.batch_size=32

    def _on_context_changed(self):
        self.ids.net_input.context = self.context.net_input
        self.ids.net_output.context = self.context.net_output
        self.ids.output_shape.context = self.context.output_shape
        self.ids.input_shape.context = self.context.input_shape


    def _define_bindings(self):
        self._bind_to_context("directory", "directory")
        self._bind_to_context("labels", "labels")
        self._bind_to_context("label_mode", "label_mode")
        self._bind_to_context("color_mode", "color_mode")
        self._bind_to_context("batch_size", "batch_size")
        self._bind_to_context("image_size", "image_size")
        self._bind_to_context("shuffle", "shuffle")
        self._bind_to_context("validation_split", "validation_split")
        self._bind_to_context("seed", "seed")
        self._bind_to_context("interpolation", "interpolation")
        self._bind_to_context("crop_to_aspect_ratio", "crop_to_aspect_ratio")
        self._bind_to_context("select_path", "select_path")
        self._bind_to_context("image_size_x", "image_size_x")
        self._bind_to_context("image_size_y", "image_size_y")

class FocusWidget(MDBoxLayout, FocusBehavior):
    pass