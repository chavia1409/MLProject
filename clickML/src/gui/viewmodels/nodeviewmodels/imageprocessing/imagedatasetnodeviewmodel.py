from common.models.component_descriptors.component_constants import DEFAULT
from common.models.component_descriptors.image_processing.cd_image_dataset_from_directory import ImageDatasetDescriptor
from common.models.mlcomponentdescriptor import MLComponentDescriptor
from gui.factories.connectiondotnodeviewmodelfactorybase import OutputDotViewModelFactoryBase, \
    InputDotViewModelFactoryBase
from gui.mvvm.command import Command
from gui.viewmodels.nodeviewmodels.nodeviewmodelbase import MLComponentNodeViewModel
from gui.viewmodels.nodeviewmodels.outputdotviewmodel import OutputDotViewModel


class ImageDatasetNodeViewModel(MLComponentNodeViewModel):
    def __init__(self, ml_component_descriptor: MLComponentDescriptor,
                 input_dot_factory: InputDotViewModelFactoryBase,
                 output_dot_factory: OutputDotViewModelFactoryBase, file_picker):
        super().__init__(ml_component_descriptor)
        self.__image_size_y = 256
        self.__image_size_x = 256
        self.__output_dot_factory = output_dot_factory
        self.__input_dot_factory = input_dot_factory
        self._set_descriptor_values()
        self.__file_picker = file_picker
    def _set_descriptor_values(self):

        self.__net_input: OutputDotViewModel = self.__output_dot_factory.create(self._descriptor.component_id,
                                                                             self._descriptor.suc)
        self.__net_output: OutputDotViewModel = self.__output_dot_factory.create(self._descriptor.component_id,
                                                                             self._descriptor.suc_2)
        self.__output_shape: OutputDotViewModel = self.__output_dot_factory.create(self._descriptor.component_id,
                                                                             self._descriptor.suc_3)
        self.__input_shape: OutputDotViewModel = self.__output_dot_factory.create(self._descriptor.component_id,
                                                                             self._descriptor.suc_4)

        self.__directory = self._descriptor.directory
        self.__labels = self._descriptor.labels
        self.__label_mode = self._descriptor.label_mode

        self.__color_mode = self._descriptor.color_mode
        self.__batch_size = self._descriptor.batch_size
        self.__image_size = self._descriptor.image_size
        self.__shuffle = self._descriptor.shuffle
        self.__validation_split = self._descriptor.validation_split
        self.__seed = self._descriptor.seed
        self.__interpolation = self._descriptor.interpolation
        self.__crop_to_aspect_ratio = self._descriptor.crop_to_aspect_ratio
        if self.__batch_size == DEFAULT:
            self.__batch_size = 32
        if self.interpolation is DEFAULT:
            self.__interpolation = "bilinear"
        if self.__crop_to_aspect_ratio is DEFAULT:
            self.__crop_to_aspect_ratio = False
        if self.__color_mode is DEFAULT:
            self.__color_mode = "rgb"
        if self.__directory is DEFAULT:
            self.__directory = ' '
        if self.__validation_split is DEFAULT:
            self.__validation_split = 0.0
        if self.__shuffle is DEFAULT:
            self.__shuffle = False
        if self.image_size is DEFAULT:
            self.__image_size = tuple((256,256))


    @property
    def title(self):
        return "Image Dataset"

    @property
    def net_input(self):
        return self.__net_input

    @property
    def net_output(self):
        return self.__net_output

    @property
    def input_shape(self):
        return self.__input_shape
    @property
    def output_shape(self):
        return self.__output_shape

    @property
    def directory(self):
        return self.__directory
    @property
    def labels(self):
        return self.__labels
    @property
    def label_mode(self):
        return self.__label_mode
    @property
    def color_mode(self):
        return self.__color_mode
    @property
    def batch_size(self):
        return self.__batch_size
    @property
    def image_size(self):
        return self.__image_size
    @property
    def shuffle(self):
        return self.__shuffle
    @property
    def validation_split(self):
        return self.__validation_split
    @property
    def seed(self):
        return self.__seed
    @property
    def interpolation (self):
        return self.__interpolation

    @property
    def crop_to_aspect_ratio(self):
        return self.__crop_to_aspect_ratio

    def select_path(self):
        path = self.__file_picker.pick_folder_name()
        if path is None:
            return
        self.directory = path

    @net_input.setter
    def net_input(self, value):
        self.__net_input=value
    @net_output.setter
    def net_output(self, value):
        self.__net_output=value
    @output_shape.setter
    def output_shape(self, value):
        self.__output_shape = value
    @input_shape.setter
    def input_shape(self, value):
        self.__input_shape = value

    @directory.setter
    def directory(self, value):
        if value == self.__directory:
            return
        self.__directory = value
        self._notify_property_changed('directory', value)

    @labels.setter
    def labels(self, value):
        if value == self.__labels:
            return
        self.__labels = value
        self._notify_property_changed('labels', value)

    @label_mode.setter
    def label_mode(self, value):
        if value == self.__label_mode:
            return
        self.__label_mode = value
        self._notify_property_changed('label_mode', value)


    @color_mode.setter
    def color_mode(self, value):
        self.__color_mode = value
        self._notify_property_changed('color_mode', value)

    @batch_size.setter
    def batch_size(self, value):
        if value == self.__batch_size:
            return
        self.__batch_size = value
        self._notify_property_changed('batch_size', value)

    @image_size.setter
    def image_size(self, value):
        if value == self.__image_size:
            return
        try:
            int(value)
            self.__image_size = value
            self._notify_property_changed('image_size', value)
        except:
            self.__image_size = tuple((256,256))

    @shuffle.setter
    def shuffle(self, value):
        if value == self.__shuffle:
            return
        self.__shuffle = value
        self._notify_property_changed('suffle', value)

    @validation_split.setter
    def validation_split(self, value):
        if value == self.__validation_split:
            return
        try:
            float(value)
            self.__validation_split = value
            self._notify_property_changed('validation_split', value)
        except:
            return

    @seed.setter
    def seed(self, value):
        if value == self.__seed:
            return
        self.__seed = value
        self._notify_property_changed('seed', value)

    @interpolation.setter
    def interpolation(self,value):
        if value ==self.__interpolation:
            return

        self.__interpolation = value
        self._notify_property_changed('interpolation', value)


    @crop_to_aspect_ratio.setter
    def crop_to_aspect_ratio(self, value):
        if value == self.__crop_to_aspect_ratio:
            return
        self.__crop_to_aspect_ratio = value
        self._notify_property_changed('crop_to_aspect_ratio', value)

    @property
    def image_size_x(self):
        return self.__image_size_x
    @image_size_x.setter
    def image_size_x(self, value):
        if value == self.__image_size_x:
            return
        self.__image_size_x = value
        self._notify_property_changed('image_size_x', value)

    @property
    def image_size_y(self):
        return self.__image_size_y

    @image_size_x.setter
    def image_size_y(self, value):
        if value == self.__image_size_y:
            return
        self.__image_size_y = value
        self._notify_property_changed('image_size_y', value)

    @property
    def ml_component_descriptor(self) -> MLComponentDescriptor:
        descriptor = ImageDatasetDescriptor(self.component_id)
        descriptor.suc = self.net_input.successor_descriptor
        descriptor.suc_2 = self.net_output.successor_descriptor
        descriptor.suc_3 = self.output_shape.successor_descriptor
        descriptor.suc_4 = self.input_shape.successor_descriptor
        if self.__directory.isspace():
            descriptor.directory = DEFAULT
        else:
            descriptor.directory = self.__directory
        descriptor.labels = self.labels
        descriptor.label_mode = self.label_mode
        descriptor.color_mode = self.color_mode
        descriptor.batch_size = self.batch_size
        descriptor.image_size = tuple((self.__image_size_x, self.__image_size_y))
        descriptor.shuffle = self.shuffle
        descriptor.validation_split = self.validation_split
        descriptor.seed = self.seed
        descriptor.interpolation = self.interpolation
        descriptor.crop_to_aspect_ratio = self.crop_to_aspect_ratio

        return descriptor
