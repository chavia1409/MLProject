import uuid
from typing import Union

from backend.ml_components.image_processing.image_dataset_from_directory import ImageDataset
from common.models.component_descriptors.component_constants import DEFAULT
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from common.models.pre_suc_descriptors import SuccessorDescriptor


class ImageDatasetDescriptor(MLComponentDescriptor):
    """
    # Attributes for the Descriptor of the image_dataset_from_directory util

    directory: str
        (required) Path variable as string. Path of the image_dataset to be imported

    labels: Union[str, list[int]]
        (required) Can be None, "inferred" (from the directory structure) or provided with a list of int variables

    label_mode: str
        (optional) String describing the encoding of labels. Can be "int", "categorical", "binary" or None

    class_name: Union[str, list[str]]
        (optional) Only valid if "labels" is "inferred".
        This is the explicit list of class names (must match names of subdirectories).
        Used to control the order of the classes (otherwise alphanumerical order is used)

    color_mode: str
        (optional) One of "grayscale", "rgb", "rgba". Default: "rgb".
        Whether the images will be converted to have 1, 3, or 4 channels.

    batch_size: Union[str, int]
        (optional) Size of the batches of data. Default: 32.
        If None, the data will not be batched (the dataset will yield individual samples).

    image_size: Union[str, tuple[int,int]]
        (optional) Size to resize images to after they are read from disk, specified as (height, width).
        Defaults to (256, 256)

    shuffle: Union[str, bool]
        (optional) Whether to shuffle the data. Default: True. If set to False, sorts the data in alphanumeric order

    seed: str
        (optional) Optional random seed for shuffling and transformations.

    validation_split: Union[str, float]
        (optional)  Optional float between 0 and 1, fraction of data to reserve for validation.

    subset: str
        (optional) Subset of the data to return. One of "training" or "validation". Only used if validation_split is set.

    interpolation: str
        (optional) String, the interpolation method used when resizing images.
        Defaults to bilinear.
        Supports bilinear, nearest, bicubic, area, lanczos3, lanczos5, gaussian, mitchellcubic.

    crop_to_aspect_ratio: Union[str, bool]
        (optional) If True, resize the images without aspect ratio distortion.
        When the original aspect ratio differs from the target aspect ratio,
        the output image will be cropped so as to return the largest possible window in the image (of size image_size) that matches the target aspect ratio.
        By default (crop_to_aspect_ratio=False), aspect ratio may not be preserved.

    """
    def __init__(self, component_id: uuid) -> None:
        self.__component_id: uuid = component_id

        # attributes for possible predecessors and successors
        self.suc: SuccessorDescriptor = SuccessorDescriptor("training_data")
        self.suc_2: SuccessorDescriptor = SuccessorDescriptor("validation_data")
        self.suc_3: SuccessorDescriptor = SuccessorDescriptor("output_shape")
        self.suc_4: SuccessorDescriptor = SuccessorDescriptor("input_shape")

        # required parameters for the util function
        self.directory: str = DEFAULT
        self.labels: Union[str, list[int]] = DEFAULT
        self.validation_split: Union[str, float] = DEFAULT

        # optional parameters for the util function
        self.label_mode: str = DEFAULT
        self.class_names: Union[str, list[str]] = DEFAULT
        self.color_mode: str = DEFAULT
        self.batch_size: Union[str, int] = DEFAULT
        self.image_size: Union[str, tuple[int, int]] = DEFAULT
        self.shuffle: Union[str, bool] = DEFAULT
        self.seed: str = DEFAULT
        self.interpolation: str = DEFAULT
        self.crop_to_aspect_ratio: Union[str, bool] = DEFAULT

    @property
    def component_id(self) -> uuid:
        return self.__component_id

    @property
    def component_type(self) -> str:
        return ImageDataset.__name__

    def restore_component(self) -> ImageDataset:
        return ImageDataset(self)
