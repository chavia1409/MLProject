import uuid

from common.models.component_descriptors.neural_networks.keras_layers.ld_resizing import ResizingDescriptor
from gui.viewmodels.nodeviewmodels.neuronalnetworks.layerviewmodelbase import LayerViewModelBase


class ResizingLayerViewModel(LayerViewModelBase):
    def __init__(self, parent, descriptor):
        super().__init__(parent, descriptor)

    @property
    def name(self):
        return 'Resizing'

    @property
    def layer_descriptor(self):
        descriptor = ResizingDescriptor(uuid.uuid4())
        return descriptor