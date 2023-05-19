"""
Python script generated with clickML.

Project name: TDSE
Project type: IMAGE CLASSIFICATION
Creation date: 2022-07-27
Number of MLComponents: 3
"""

from keras.layers import Conv2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Input
from keras.layers import MaxPool2D
from keras.layers import Rescaling
from keras.models import Sequential
from keras.utils import image_dataset_from_directory

training_dataset = image_dataset_from_directory(directory='F:\\Fruits\\FruitsProj', labels='inferred', label_mode='int', color_mode='rgb', 
    batch_size=32, image_size=(200, 120), shuffle=False, validation_split=0.2, interpolation='bilinear', subset='training') 
validation_dataset = image_dataset_from_directory(directory='F:\\Fruits\\FruitsProj', labels='inferred', label_mode='int', color_mode='rgb', 
    batch_size=32, image_size=(200, 120), shuffle=False, validation_split=0.2, interpolation='bilinear', subset='validation') 
output_shape = 14 
input_shape = (32, 200, 120, 3)

# creating sequential model
model = Sequential(name='Fruits')
model.add(Input(shape=input_shape))
model.add(Rescaling(scale=0, offset=0))
model.add(Conv2D(filters=16, kernel_size=(3, 0)))
model.add(MaxPool2D(pool_size=0))
model.add(Conv2D(filters=32, kernel_size=(3, 0)))
model.add(MaxPool2D(pool_size=0))
model.add(Conv2D(filters=64, kernel_size=(3, 0)))
model.add(MaxPool2D(pool_size=0))
model.add(Flatten())
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=output_shape))
model.compile(optimizer='Adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# training sequential model
model.fit(x=training_dataset, y=validation_dataset, epochs=15)
