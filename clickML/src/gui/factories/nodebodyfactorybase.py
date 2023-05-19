from abc import ABC, abstractmethod
from typing import Callable


class NodeBodyFactoryBase(ABC):

    @abstractmethod
    def create(self, component_type:str):
        pass
