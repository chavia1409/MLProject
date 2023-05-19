from abc import ABC, abstractmethod

from backend.ml_components.ml_component import MLComponent
from common.models.mlcomponentdescriptor import MLComponentDescriptor


class ProjectTransformer(ABC):
    """class for needed conversion of given data model from frontend to complete model"""

    @abstractmethod
    def do_transformation(self, components: list[MLComponentDescriptor]) -> list[MLComponent]:
        """turning list[MLComponentDescriptors] into list[MLComponents]"""
