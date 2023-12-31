# -*- coding: utf-8 -*-
"""DEEP LSTM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11jqrFbYe5_mA0wL5LTY1hJe1lIFzid0D
"""

from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing import sequence
import matplotlib.pyplot as plt

# Load the IMDB dataset
max_features = 10000  # Consider only the top 10,000 most frequent words
maxlen = 500  # Cut reviews after 500 words
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)

# Build the deep LSTM model
model = Sequential()

# Embedding layer
model.add(Embedding(max_features, 32, input_length=maxlen))

# First LSTM layer
model.add(LSTM(units=32, activation='tanh', return_sequences=True))

# Second LSTM layer
model.add(LSTM(units=32, activation='tanh', return_sequences=True))

# Third LSTM layer
model.add(LSTM(units=32, activation='tanh'))

# Output layer
model.add(Dense(units=1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history=model.fit(x_train, y_train, epochs=10, batch_size=128, validation_split=0.2)

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# Evaluate the model on the test set
loss, accuracy = model.evaluate(x_test, y_test)
print(f'Test accuracy: {accuracy * 100:.2f}%')