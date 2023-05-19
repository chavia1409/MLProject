"""Module for serialization of a ClickMLProjectModel"""

import os
import pickle

from common.exceptions.click_ml_exceptions import SpecificationError
from common.interfaces.ProjectSerializer import ProjectSerializer
from common.models.ClickMLProjectModel import ClickMLProjectModel


class ProjectModelSerializer(ProjectSerializer):

    def save_project(self, project_model: ClickMLProjectModel, file_path: str) -> None:
        """Saves ClickMlProjectModel file_path."""
        if not os.path.isdir(os.path.dirname(file_path)):
            raise SpecificationError("file_path", file_path, "ProjectModelSerializer", "Not a valid directory!")
        if not file_path.endswith(".cmlproj"):
            raise SpecificationError("file_path", file_path, "ProjectModelSerializer", "Not a '.cmlproj' file!")
        with open(file_path, "wb") as file:
            pickle.dump(project_model, file)

    def load_project(self, file_path: str) -> ClickMLProjectModel:
        """Returns ClickMLProjectModel loaded from given file_path."""
        if not os.path.isfile(file_path):
            raise SpecificationError("file_path", file_path, "ProjectModelSerializer", "Not a file!")
        if not file_path.endswith(".cmlproj"):
            raise SpecificationError("file_path", file_path, "ProjectModelSerializer", "Not a '.cmlproj' file!")
        with open(file_path, "rb") as file:
            return pickle.load(file)
