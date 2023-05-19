import os
import uuid

from backend.generator_demo.temp_config import config
from common.models.component_descriptors.image_processing.cd_image_dataset_from_directory import ImageDatasetDescriptor
from common.models.component_descriptors.neural_networks.cd_sequential_model import SequentialModelDescriptor
from common.models.component_descriptors.neural_networks.cd_train_sequential import TrainSequentialDescriptor
from common.models.component_descriptors.neural_networks.keras_layers.ld_MaxPool2D import MaxPool2DDescriptor
from common.models.component_descriptors.neural_networks.keras_layers.ld_conv2D import conv2D_Descriptor
from common.models.component_descriptors.neural_networks.keras_layers.ld_dense import DenseDescriptor
from common.models.component_descriptors.neural_networks.keras_layers.ld_flatten import FlattenDescriptor
from common.models.component_descriptors.neural_networks.keras_layers.ld_rescaling import RescalingDescriptor


def main():
    code_generator = config()

    # components

    dataset = ImageDatasetDescriptor(uuid.uuid4())
    dataset.directory = "clickml/src/backend/generator_demo/Dataset"
    dataset.labels = "inferred"
    dataset.label_mode = "int"
    dataset.color_mode = "rgba"

    # layer

    conv2D_1 = conv2D_Descriptor(uuid.uuid4())
    conv2D_1.filters = 8
    conv2D_1.kernel_size = (3, 3)
    conv2D_1.activation = "relu"
    conv2D_1.input_shape = (224, 224, 3)

    conv2D_2 = conv2D_Descriptor(uuid.uuid4)
    conv2D_2.filter = 16
    conv2D_2.kernel_size = (3, 3)
    conv2D_2.activation = "relu"

    conv2D_3 = conv2D_Descriptor(uuid.uuid4())
    conv2D_3.filter = 32
    conv2D_3.kernel_size = (3, 3)
    conv2D_3.activation = "relu"

    dense = DenseDescriptor(uuid.uuid4())
    dense.units = 64
    dense.activation = "relu"

    dense_2 = DenseDescriptor(uuid.uuid4())
    dense_2.units = 2
    dense_2.activation = "softmax"

    flatten = FlattenDescriptor(uuid.uuid4())
    flatten.data_format = "channels_last" \
                          ""
    maxPool2D = MaxPool2DDescriptor(uuid.uuid4())
    maxPool2D.pool_size = (2, 2)
    maxPool2D.strides = None
    maxPool2D.padding = "valid"

    maxPool2D_2 = MaxPool2DDescriptor(uuid.uuid4())
    maxPool2D_2.pool_size = 2
    maxPool2D_2.strides = 2
    maxPool2D_2.padding = "valid"

    maxPool2D_3 = MaxPool2DDescriptor(uuid.uuid4())
    maxPool2D_3.pool_size = 2
    maxPool2D_3.strides = 2
    maxPool2D_3.padding = "valid"

    rescaling = RescalingDescriptor(uuid.uuid4())
    rescaling.scale = 1
    rescaling.offset = 255

    #resizing = ResizingDescriptor(uuid.uuid4())

    layers = [rescaling, conv2D_1, maxPool2D, conv2D_2, maxPool2D_2, conv2D_3, maxPool2D_3, flatten, dense, dense_2]

    seq_model = SequentialModelDescriptor(uuid.uuid4())
    seq_model.name = "ImageClassModel"
    seq_model.metrics = ["accuracy"]
    seq_model.optimizer = "Adam"
    seq_model.layers = layers
    seq_model.loss = "categorical_crossentropy"

    train = TrainSequentialDescriptor(uuid.uuid4())
    train.data = dataset
    train.validation_split = 0.1
    train.epochs = 50



    """#component connections

    rescaling.suc.id_next = conv2D_1.component_id

    conv2D_1.pre.id_prev = rescaling.component_id
    conv2D_1.suc.id_next = maxPool2D.component_id

    conv2D_2.pre.id_prev = maxPool2D.component_id
    conv2D_2.suc.id_next = maxPool2D_2.component_id

    conv2D_3.pre.id_prev = maxPool2D_2.component_id
    conv2D_3.suc.id_next = maxPool2D_3.component_id

    maxPool2D.pre.id_prev = conv2D_1.component_id
    maxPool2D.suc.id_next = conv2D_2.component_id

    maxPool2D_2.pre.id_prev = conv2D_2.component_id
    maxPool2D_2.suc.id_next = conv2D_3.component_id

    maxPool2D_3.pre.id_prev = conv2D_3.component_id
    maxPool2D_3.suc.id_next = flatten.component_id

    flatten.pre.id_prev = maxPool2D_3.component_id
    flatten.suc.id_next = dense.component_id

    dense.pre.id_prev = flatten.component_id
    dense.suc.id_next = dense_2.component_id

    dense_2.pre.id_prev = dense.component_id"""

    #creating project

    lc_list = [dataset]

    code_generator.generate_code_file(lc_list, os.getcwd(), "image_class", validator_mode="on")

if __name__ == "__main__":
    main()




