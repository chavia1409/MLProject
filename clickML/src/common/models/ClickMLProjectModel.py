from typing import Optional
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.mlcomponentdesignerdescriptor import MLComponentDesignerDescriptor


class ClickMLProjectModel:
    """
    Class representing the complete project.

    Attributes:
        __name: Optional[str]
            (required) Name of the project, should be str
        __components: list[MLComponent]
            (optional) List of MLComponents according to Flowchart created by the user
        __designers: list[MLComponentDesignerDescriptor]
            (optional) List of MLComponentDesigner which hold the UI relevant data for a MLComponent
    """

    def __init__(self) -> None:
        self.__name: Optional[str] = None
        self.__components: list[MLComponentDescriptor] = list()
        self.__designers: list[MLComponentDesignerDescriptor] = list()

    @property
    def name(self) -> Optional[str]:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def components(self) -> list[MLComponentDescriptor]:
        return self.__components

    @components.setter
    def components(self, value: list[MLComponentDescriptor]) -> None:
        self.__components = value

    @property
    def designers(self) -> list[MLComponentDesignerDescriptor]:
        return self.__designers

    @designers.setter
    def designers(self, value: list[MLComponentDesignerDescriptor]) -> None:
        self.__designers = value

