from common.models.component_descriptors.neural_networks.keras_layers.ld_dense import DenseDescriptor
from gui.mvvm.viewmodelbase import ViewModelBase


class LayerViewModelBase(ViewModelBase):
    def __init__(self, parent, descriptor):
        super().__init__()
        self.__parent = parent
        self._descriptor = descriptor
    @property
    def name(self):
        return ''

    def delete(self):
        self.__parent.delete_layer(self)

    @property
    def component_type(self):
        return self._descriptor.component_type

    @property
    def layer_descriptor(self):
        pass