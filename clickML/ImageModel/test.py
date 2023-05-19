
import numpy as np
import tensorflow
from tensorflow import keras

predictor = keras.models.load_model('F:/PycharmProjects/clickml/ImageModel/model1')

class_names = ['apple', 'banana', 'cherry']

img = keras.utils.load_img('F:/PycharmProjects/clickml/ImageModel/TryTest/1.jpg', target_size=(208, 256))

img_array = keras.utils.img_to_array(img)

img_array = tensorflow.expand_dims(img_array, 0)  # Create a batch

predictions = predictor.predict(img_array)
score = tensorflow.nn.softmax(predictions[0])

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score)))


