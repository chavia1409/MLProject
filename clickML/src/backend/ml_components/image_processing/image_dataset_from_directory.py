from __future__ import annotations

import copy
from typing import Union, TYPE_CHECKING, Any

from backend.component_enum import Components
from backend.ml_components.ml_component import MLComponent
from common.exceptions.click_ml_exceptions import SpecificationError, RequiredArgumentError
from common.models.component_descriptors.component_constants import DEFAULT, KERAS_LAYERS_POL
from common.models.pre_suc_descriptors import PredecessorDescriptor, SuccessorDescriptor

if TYPE_CHECKING:
    from common.models.component_descriptors.image_processing.cd_image_dataset_from_directory import \
        ImageDatasetDescriptor

"""Takes a given directory filled with images, with subdirectories distributed according to the labels and turns
it into a Dataset to be used in the neural network"""
# supported image formats: jpeg, png, bmp, gif (first frame)


class ImageDataset(MLComponent):

    def __init__(self, descriptor: ImageDatasetDescriptor) -> None:


        # add here new varnames
        self.__directory = DEFAULT
        self.__labels = DEFAULT
        self.__label_mode = DEFAULT
        self.__class_names = DEFAULT
        self.__color_mode = DEFAULT
        self.__batch_size = DEFAULT
        self.__image_size = DEFAULT
        self.__shuffle = DEFAULT
        self.__validation_split = DEFAULT
        self.__seed = DEFAULT
        self.__interpolation = DEFAULT
        self.__crop_to_aspect_ratio = DEFAULT

        des = copy.deepcopy(descriptor)
        super().__init__(des.component_id)

        self.suc = des.suc
        self.suc_2 = des.suc_2
        self.suc_3 = des.suc_3
        self.suc_4 = des.suc_4

        self.directory = des.directory
        self.labels = des.labels
        self.label_mode = des.label_mode
        self.class_names = des.class_names
        self.color_mode = des.color_mode
        self.batch_size = des.batch_size
        self.image_size = des.image_size
        self.shuffle = des.shuffle
        self.validation_split = des.validation_split
        self.seed = des.seed
        self.interpolation = des.interpolation
        self.crop_to_aspect_ratio = des.crop_to_aspect_ratio

    @property
    def predecessors(self) -> list[PredecessorDescriptor]:
        return []

    @property
    def successors(self) -> list[SuccessorDescriptor]:
        return [self.suc, self.suc_2, self.suc_3, self.suc_4]

    @property
    def values_for_successors(self) -> dict[str, Any]:
        pre_dict = {
            self.suc.name: "training_dataset",
            self.suc_2.name: "validation_dataset",
            self.suc_3.name: "output_shape",
            self.suc_4.name: "input_shape"
        }
        return pre_dict

    @property
    def directory(self) -> str:
        return self.__directory

    @directory.setter
    def directory(self, value: str) -> None:
        if isinstance(value, str):
            self.__directory = value
        else:
            raise SpecificationError("directory", value, "to_dataset")

    @property
    def labels(self) -> str:
        return self.__labels

    @labels.setter
    def labels(self, value: str) -> None:
        if value == "inferred":
            self.__labels = value
        else:
            raise SpecificationError("labels", value, "to_dataset")

    @property
    def label_mode(self) -> str:
        return self.__label_mode

    @label_mode.setter
    def label_mode(self, value: str) -> None:
        if value == "int" or value == "categorical" or value == "binary":
            self.__label_mode = value
        elif value == DEFAULT:
            pass
        else:
            raise SpecificationError("label_mode", value, "to_dataset")

    @property
    def class_names(self) -> list[str]:
        return self.__class_names

    @class_names.setter
    def class_names(self, value: list[str]) -> None:
        if isinstance(value, list):
            self.__class_names = value
        elif value == DEFAULT:
            pass
        else:
            raise SpecificationError("class_names", value, "to_dataset")

    @property
    def color_mode(self) -> str:
        return self.__color_mode

    @color_mode.setter
    def color_mode(self, value: str) -> None:
        if value == "grayscale" or value == "rgb" or value == "rgba":
            self.__color_mode = value
        elif value == DEFAULT:
            pass
        else:
            raise SpecificationError("color_mode", value, "to_dataset")

    @property
    def batch_size(self) -> int:
        return self.__batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        if isinstance(value, int) and 0 < value:
            self.__batch_size = value
        elif value == DEFAULT:
            self.__batch_size = 32
        else:
            raise SpecificationError("batch_size", value, "to_dataset")

    @property
    def image_size(self) -> tuple[int, int]:
        return self.__image_size

    @image_size.setter
    def image_size(self, value: tuple[int, int]) -> None:
        if isinstance(value, tuple) and value[0] > 0 and value[1] > 0:
            self.__image_size = value
        elif value == DEFAULT:
            self.__image_size = (256, 256)
        else:
            raise SpecificationError("image_size", value, "to_dataset")

    @property
    def shuffle(self) -> bool:
        return self.__shuffle

    @shuffle.setter
    def shuffle(self, value: bool) -> None:
        if isinstance(value, bool):
            self.__shuffle = value
        elif value == DEFAULT:
            pass
        else:
            raise SpecificationError("shuffle", value, "to_dataset")

    @property
    def seed(self) -> str:
        return self.__seed

    @seed.setter
    def seed(self, value: str):
        if isinstance(value, str):
            self.__seed = value
        elif value == DEFAULT:
            pass
        else:
            raise SpecificationError("seed", value, "to_dataset")

    @property
    def validation_split(self) -> float:
        return self.__validation_split

    @validation_split.setter
    def validation_split(self, value: float) -> None:
        if isinstance(value, float):
            self.__validation_split = value
        elif value == DEFAULT:
            pass
        else:
            raise SpecificationError("validation_split", value, "to_dataset")

    @property
    def interpolation(self) -> str:
        return self.__interpolation

    @interpolation.setter
    def interpolation(self, value: str ) -> None:
        if value in KERAS_LAYERS_POL:
            self.__interpolation = value
        elif value == DEFAULT:
            pass
        else:
            raise SpecificationError("interpolation", value, "to_dataset")

    @property
    def crop_to_aspect_ratio(self) -> bool:
        return self.__crop_to_aspect_ratio

    @crop_to_aspect_ratio.setter
    def crop_to_aspect_ratio(self, value: bool) -> None:
        if isinstance(value, bool):
            self._crop_to_aspect_ratio = value
        elif value == DEFAULT:
            pass
        else:
            raise SpecificationError("crop_to_aspect_ratio", value, "to_dataset")

    @property
    def num_channels(self) -> int:
        if self.__color_mode == "grayscale":
            return 1
        if self.__color_mode == "rgb":
            return 3
        if self.__color_mode == "rgba":
            return 4
        if self.__color_mode == DEFAULT:
            return 3
        else:
            raise SpecificationError("num_channels", 'test', "to_dataset")

    def get_needed_imports(self) -> list[str]:
        return ["from keras.utils import image_dataset_from_directory"]

    def check_param(self) -> dict[str, Any]:
        param_dict = {"directory": self.directory, "labels": self.labels}
        if self.label_mode != DEFAULT:
            param_dict.update({"label_mode": self.label_mode})
        if self.class_names != DEFAULT:
            param_dict.update({"class_names": self.class_names})
        if self.color_mode != DEFAULT:
            param_dict.update({"color_mode": self.color_mode})
        if self.batch_size != DEFAULT:
            param_dict.update({"batch_size": self.batch_size})
        if self.image_size != DEFAULT:
            param_dict.update({"image_size": self.image_size})
        if self.shuffle != DEFAULT:
            param_dict.update({"shuffle": self.shuffle})
        if self.validation_split != DEFAULT:
            param_dict.update({"validation_split": self.validation_split})
        if self.seed != DEFAULT:
            param_dict.update({"seed": self.seed})
        if self.interpolation != DEFAULT:
            param_dict.update({"interpolation": self.interpolation})
        if self.crop_to_aspect_ratio != DEFAULT:
            param_dict.update({"crop_to_aspect_ratio": self.crop_to_aspect_ratio})
        return param_dict

    @property
    def parameters_Image_Dataset(self) -> str:
        param_dict = self.check_param()
        return self.toolkit.create_param_string(param_dict)

    def to_code(self) -> str:
        train_data = f"training_dataset = image_dataset_from_directory({self.parameters_Image_Dataset}, subset='training') \n"
        validation_data = f"validation_dataset = image_dataset_from_directory({self.parameters_Image_Dataset}, subset='validation') \n"
        output_s = f"output_shape = {len(self.class_names)} \n"
        input_s = f"input_shape = {self.batch_size, self.image_size[0], self.image_size[1], self.num_channels }"
        return train_data + validation_data + output_s + input_s

    def check_if_valid(self) -> bool:
        if self.directory == DEFAULT:
            raise RequiredArgumentError("directory", "image_dataset_from_directory")
        if self.labels == DEFAULT:
            raise RequiredArgumentError("labels", "image_dataset_from_directory")
        return True

    def do_preprocessing(self) -> None:
        pass

    def type(self) -> Components:
        return Components.IMAGE_DATASET
