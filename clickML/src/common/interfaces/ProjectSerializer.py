from abc import ABC, abstractmethod
from common.models import ClickMLProjectModel


class ProjectSerializer(ABC):

    @abstractmethod
    def save_project(self, project_model: ClickMLProjectModel, file_path: str) -> None:
        pass

    @abstractmethod
    def load_project(self, file_path: str) -> ClickMLProjectModel:
        pass
