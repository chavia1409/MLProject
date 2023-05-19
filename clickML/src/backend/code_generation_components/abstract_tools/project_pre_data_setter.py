from abc import ABC, abstractmethod

from backend.ml_components.ml_component import MLComponent


class ProjectPreDataSetter(ABC):
    """class that sets information about predecessors of components in the respective MLComponents"""

    @abstractmethod
    def set_pre_data(self, components: list[MLComponent]) -> list[MLComponent]:
        """calling do_preprocessing() methods of MLComponent in valid order"""
