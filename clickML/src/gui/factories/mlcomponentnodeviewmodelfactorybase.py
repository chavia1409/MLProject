from abc import ABC, abstractmethod

from common.models.mlcomponentdescriptor import MLComponentDescriptor


class MLComponentNodeViewModelFactoryBase(ABC):

    @abstractmethod
    def create_by_descriptor(self, descriptor: MLComponentDescriptor):
        pass

    @abstractmethod
    def create(self, component_type: str):
        pass
    