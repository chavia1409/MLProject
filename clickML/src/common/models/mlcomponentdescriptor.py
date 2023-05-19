from abc import ABC, abstractmethod
from backend.ml_components.ml_component import MLComponent
from varname import nameof
import uuid


class MLComponentDescriptor(ABC):
    """
    Descriptor for MLComponents. Based on Memento pattern.
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
    def restore_component(self) -> MLComponent:
        pass
