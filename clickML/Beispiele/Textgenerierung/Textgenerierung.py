"""
Python script generated with clickML.

Project name: Textgenerierung
Project type: TEXT GENERATION
Creation date: 2022-07-28
Number of MLComponents: 8
"""

import numpy
import pandas as pd
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Input
from keras.layers import LSTM
from keras.models import Sequential
from keras.utils import np_utils
from matplotlib import pyplot as plt

# reading text from source file
with open(file='/Users/kaiko/Desktop/clickml/Beispiele/Textgenerierung/alice_chapters_1_2.txt') as file:
    text = file.read()

text = text.lower()

# delete sequences from text 
for seq in ['.', ',', ':', '!', '?', '-']:
    text = text.replace(seq, '')

# creating dict for transforming chars into numerical representation
chars = sorted(list(set(text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))

# dividing text into sequences of 100 characters
dataX = []
dataY = []
for i in range(0, len(text) - 100):
    seq_in = text[i:i + 100]
    seq_out = text[i + 100]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])

# reshaping and normalizing data
X = numpy.reshape(dataX, (len(dataX), 100, 1))
X = X / float(len(chars))
y = np_utils.to_categorical(dataY)

# creating sequential model
model = Sequential(name='MeinTextModell')
model.add(Input(shape=(X.shape[1], X.shape[2])))
model.add(LSTM(units=256))
model.add(Dropout(rate=0.2))
model.add(Dense(units=y.shape[1], activation='softmax'))
model.load_weights('/Users/kaiko/Desktop/clickml/Beispiele/Textgenerierung/epoch_30-loss_0.40.hdf5')
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_crossentropy',
    'accuracy'])

# training sequential model
history = model.fit(x=X, y=y, batch_size=256, epochs=7, verbose=1)

# plotting history with all specified metrics
pd.DataFrame(history.history).plot()
plt.show()

# picking start sequence
pattern = dataX[0]

# generate text
generated_text = ''
for _ in range(44):
    x = numpy.reshape(pattern, (1, len(pattern), 1))
    x = x / float(len(chars))
    prediction = model.predict(x, verbose=0)
    index = numpy.argmax(prediction)
    result = int_to_char[index]
    generated_text += result
    pattern.append(index)
    pattern = pattern[1:]

print(generated_text)
