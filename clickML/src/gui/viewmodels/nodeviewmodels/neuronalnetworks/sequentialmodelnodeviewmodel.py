import uuid

from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.neural_networks.cd_sequential_model import SequentialModelDescriptor
from common.models.component_descriptors.neural_networks.keras_layers.ld_CenterCrop import CenterCropDescriptor
from common.models.component_descriptors.neural_networks.keras_layers.ld_dense import DenseDescriptor
from common.models.component_descriptors.neural_networks.keras_layers.ld_dropout import DropoutDescriptor
from common.models.component_descriptors.neural_networks.keras_layers.ld_gru import GRUDescriptor
from common.models.component_descriptors.neural_networks.keras_layers.ld_lstm import LSTMDescriptor
from common.models.component_descriptors.neural_networks.keras_layers.ld_conv2D import conv2D_Descriptor
from common.models.component_descriptors.neural_networks.keras_layers.ld_MaxPool2D import MaxPool2DDescriptor
from common.models.component_descriptors.neural_networks.keras_layers.ld_flatten import FlattenDescriptor
from common.models.component_descriptors.neural_networks.keras_layers.ld_rescaling import RescalingDescriptor
from common.models.component_descriptors.neural_networks.keras_layers.ld_resizing import ResizingDescriptor

from common.models.ml_layer_component_descriptor import MLLayerComponentDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import OutputDotViewModelFactoryBase, \
    InputDotViewModelFactoryBase
from gui.mvvm.viewmodelbase import ViewModelBase
from gui.services.filepickersevicebase import FilePickerServiceBase
from gui.viewmodels.nodeviewmodels.neuronalnetworks.centercroplayerviewmodel import CenterCropLayerViewModel
from gui.viewmodels.nodeviewmodels.neuronalnetworks.conv2dlayerviewmodel import Conv2DLayerViewModel
from gui.viewmodels.nodeviewmodels.neuronalnetworks.denselayerviewmodel import DenseLayerViewModel
from gui.viewmodels.nodeviewmodels.neuronalnetworks.dropoutlayerviewmodel import DropoutLayerViewModel
from gui.viewmodels.nodeviewmodels.neuronalnetworks.flattenlayerviewmodel import FlattenLayerViewModel
from gui.viewmodels.nodeviewmodels.neuronalnetworks.grulayerviewmodel import GRULayerViewModel
from gui.viewmodels.nodeviewmodels.neuronalnetworks.lstmlayerviewmodel import LSTMLayerViewModel
from gui.viewmodels.nodeviewmodels.neuronalnetworks.maxpool2dlayerviewmodel import MaxPool2DLayerViewModel
from gui.viewmodels.nodeviewmodels.neuronalnetworks.rescalinglayerviewmodel import RescalingLayerViewModel
from gui.viewmodels.nodeviewmodels.neuronalnetworks.resizinglayerviewmodel import ResizingLayerViewModel
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel


class SequentialModelNodeViewModel(MLComponentNodeViewModel):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 input_dot_factory: InputDotViewModelFactoryBase,
                 output_dot_factory: OutputDotViewModelFactoryBase,
                 file_picker: FilePickerServiceBase):
        super().__init__(ml_component_descriptor)
        self.__file_picker = file_picker
        self.__output_dot_factory = output_dot_factory
        self.__input_dot_factory = input_dot_factory
        self._set_descriptor_values()

    def _set_descriptor_values(self):
        self.__input_shape = self.__input_dot_factory.create(self.component_id, self._descriptor.pre)
        self.__output_shape = self.__input_dot_factory.create(self.component_id, self._descriptor.pre_2)
        self.__model_output = self.__output_dot_factory.create(self.component_id, self._descriptor.suc)
        self.__name_enabled = True
        self.__name = self._descriptor.name
        if self._descriptor.name == DEFAULT:
            self.__name_enabled = False
            self.__name = ''

        self.create_layers_viewmodels(self._descriptor.layers)
        self.__weight_file_enabled = True
        self.__weight_file_path = self._descriptor.weight_file
        if self._descriptor.weight_file == DEFAULT:
            self.__weight_file_enabled = False
            self.__weight_file_path = ''
        self.__optimizer = self._descriptor.optimizer
        self.__loss_function = self._descriptor.loss
        if self._descriptor.loss == DEFAULT:
            self.__loss_function = ''
        self.create_metrics_viewmodels(self._descriptor.metrics)

    def create_layers_viewmodels(self, layers):
        self.__layers = []
        if layers == DEFAULT:
            return
        for layer in layers:
            self.add_layer_by_descriptor(layer)

    def create_metrics_viewmodels(self, metrics):
        self.__metric_functions = []
        if metrics == DEFAULT:
            return
        for metric in metrics:
            self.add_metric(metric)
    @property
    def input_shape(self):
        return self.__input_shape

    @property
    def output_shape(self):
        return self.__output_shape

    @property
    def model_output(self):
        return self.__model_output

    @property
    def title(self):
        return 'Sequential Model'

    @property
    def name_enabled(self):
        return self.__name_enabled

    @name_enabled.setter
    def name_enabled(self, value):
        if self.__name_enabled == value:
            return
        self.__name_enabled = value
        self._notify_property_changed('name_enabled', value)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if self.__name == value:
            return
        self.__name = value
        self._notify_property_changed('name', value)

    @property
    def weight_file_enabled(self):
        return self.__weight_file_enabled

    @weight_file_enabled.setter
    def weight_file_enabled(self, value):
        if self.__weight_file_enabled == value:
            return
        self.__weight_file_enabled = value
        self._notify_property_changed('weight_file_enabled', value)

    @property
    def weight_file_path(self):
        return self.__weight_file_path

    @weight_file_path.setter
    def weight_file_path(self, value):
        if self.__weight_file_path == value:
            return
        self.__weight_file_path = value
        self._notify_property_changed('weight_file_path', value)

    def select_weight_file_path(self):
        path = self.__file_picker.pick_file_name()
        if path == None:
            return
        self.weight_file_path = path

    @property
    def optimizer(self):
        return self.__optimizer

    @optimizer.setter
    def optimizer(self, value):
        if self.__optimizer == value:
            return
        self.__optimizer = value
        self._notify_property_changed('optimizer', value)

    @property
    def loss_function(self):
        return self.__loss_function

    @loss_function.setter
    def loss_function(self, value):
        if self.__loss_function == value:
            return
        self.__loss_function = value
        self._notify_property_changed('loss_function', value)

    @property
    def layers(self):
        return self.__layers

    @layers.setter
    def layers(self, value):
        if self.__layers == value:
            return
        self.__layers = value
        self._notify_property_changed('layers', value)

    @property
    def metric_functions(self):
        return self.__metric_functions

    @metric_functions.setter
    def metric_functions(self, value):
        if self.__metric_functions == value:
            return
        self.__metric_functions = value
        self._notify_property_changed('metric_functions', value)

    def add_layer(self, args):
        if args == 'Dense':
            self.add_layer_by_descriptor(DenseDescriptor(uuid.uuid4()))
        if args == 'Dropout':
            self.add_layer_by_descriptor(DropoutDescriptor(uuid.uuid4()))
        if args == 'LSTM':
            self.add_layer_by_descriptor(LSTMDescriptor(uuid.uuid4()))
        if args == 'Flatten':
            self.add_layer_by_descriptor(FlattenDescriptor(uuid.uuid4()))
        if args == 'MaxPool2DLayerComponent':
            self.add_layer_by_descriptor(MaxPool2DDescriptor(uuid.uuid4()))
        if args == 'conv2D_Layer':
            self.add_layer_by_descriptor(conv2D_Descriptor(uuid.uuid4()))
        if args == 'RescalingLayer':
            self.add_layer_by_descriptor(RescalingDescriptor(uuid.uuid4()))
        if args == 'CenterCrop':
            self.add_layer_by_descriptor(CenterCropDescriptor(uuid.uuid4()))
        if args == 'Resizing':
            self.add_layer_by_descriptor(ResizingDescriptor(uuid.uuid4()))
        if args == 'GRU':
            self.add_layer_by_descriptor(GRUDescriptor(uuid.uuid4()))
        if args == '':
            self.add_layer_by_descriptor(CenterCropDescriptor(uuid.uuid4()))
    def add_layer_by_descriptor(self, descriptor):
        layerViewModel = None
        if descriptor.component_type == 'Dense':
            layerViewModel = DenseLayerViewModel(self, descriptor)
        if descriptor.component_type == 'Dropout':
            layerViewModel = DropoutLayerViewModel(self, descriptor)
        if descriptor.component_type == 'LSTM':
            layerViewModel = LSTMLayerViewModel(self, descriptor)
        if descriptor.component_type == 'Flatten':
            layerViewModel = FlattenLayerViewModel(self, descriptor)
        if descriptor.component_type == 'MaxPool2DLayerComponent':
            layerViewModel = MaxPool2DLayerViewModel(self, descriptor)
        if descriptor.component_type == 'conv2D_Layer':
            layerViewModel = Conv2DLayerViewModel(self, descriptor)
        if descriptor.component_type == 'RescalingLayer':
            layerViewModel = RescalingLayerViewModel(self, descriptor)
        if descriptor.component_type == 'CenterCrop':
            layerViewModel = CenterCropLayerViewModel(self, descriptor)
        if descriptor.component_type == 'GRU':
            layerViewModel = GRULayerViewModel(self, descriptor)
        if descriptor.component_type == 'Resizing':
            layerViewModel = ResizingLayerViewModel(self, descriptor)
        if layerViewModel is None:
            return
        self.layers.append(layerViewModel)
        self._notify_property_changed('layers', self.layers)

    def delete_layer(self, layer):
        layers = self.layers.copy()
        layers.remove(layer)
        self.layers = layers

    def add_metric(self, name):
        self.metric_functions.append(MetricFunctionViewModel(self, name))
        self._notify_property_changed('metric_functions', self.__metric_functions)

    def delete_metric_function(self, metric):
        metrics = self.metric_functions.copy()
        metrics.remove(metric)
        self.metric_functions = metrics

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = SequentialModelDescriptor(self.component_id)
        descriptor.pre = self.__input_shape.predecessor_descriptor
        descriptor.pre_2 = self.__output_shape.predecessor_descriptor
        descriptor.suc = self.model_output.successor_descriptor
        descriptor.name = self.__name
        if not self.__name_enabled:
            descriptor.name = DEFAULT
        layers = []
        for layer in self.__layers:
            layers.append(layer.layer_descriptor)
        descriptor.layers = layers
        if len(layers) == 0:
            descriptor.layers = DEFAULT
        descriptor.loss = self.__loss_function
        metrics = []
        for metric in self.__metric_functions:
            metrics.append(metric.name)
        descriptor.metrics = metrics
        if len(metrics) == 0:
            descriptor.metrics = DEFAULT
        descriptor.optimizer = self.optimizer
        descriptor.weight_file = self.__weight_file_path
        if not self.__weight_file_enabled:
            descriptor.weight_file = DEFAULT
        return descriptor

class MetricFunctionViewModel(ViewModelBase):

    def __init__(self, parent, name):
        super().__init__()
        self.__name = name
        self.__parent = parent

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == self.__name:
            return
        self.__name = value
        self._notify_property_changed('name', value)

    def delete(self):
        self.__parent.delete_metric_function(self)
