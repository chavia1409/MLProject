from abc import ABC, abstractmethod


class ConverterBase(ABC):

    @abstractmethod
    def convert(self, value) -> object:
        pass

    @abstractmethod
    def convert_back(self, value) -> object:
        pass