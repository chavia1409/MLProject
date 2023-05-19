from abc import ABC, abstractmethod
from common.models.mlcomponentdescriptor import MLComponentDescriptor


class CodeGenerator(ABC):

    @abstractmethod
    def generate_code_file(self, ml_components: list[MLComponentDescriptor], saving_dir: str, name: str) -> None:
        pass
