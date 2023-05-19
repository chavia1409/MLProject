from abc import ABC, abstractmethod
from typing import Type


class GeneralFactoryBase(ABC):

    @abstractmethod
    def create(self, t: Type, **kwargs):
        pass