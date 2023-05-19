from abc import ABC, abstractmethod
import uuid
from backend.ml_components.ml_layer_component import MLLayerComponent


class MLLayerComponentDescriptor(ABC):
    """
    Descriptor for MLLayerComponents. Based on Memento pattern.
    """

    @property
    @abstractmethod
    def component_id(self) -> uuid:
        pass

    @property
    @abstractmethod
    def component_type(self) -> str:
        pass

    @abstractmethod
    def restore_layer(self) -> MLLayerComponent:
        pass
