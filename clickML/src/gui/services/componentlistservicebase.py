from abc import abstractmethod, ABC


class ComponentListServiceBase(ABC):

    @abstractmethod
    def set(self, descriptor, name, parent):
        pass

    @abstractmethod
    def get_list(self) -> list[[]]:
        pass
