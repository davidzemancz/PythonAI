from keras.datasets import imdb
from keras import utils
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words = 10_000)


def vectorize_sequences(sequences, dim = 10_000):
    results = np.zeros((len(sequences), dim))
    for i,sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results

# Slovniky pro kodovani a dekodovani
# word_index = imdb.get_word_index()
#inveres_word_index = dict([(value, key) for (key, value) in word_index.items()])
# decoded = " ".join([inveres_word_index.get(i - 3, "?") for i in train_data[0]])
# print("Decode:", decoded)

x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)
y_train = np.asarray(train_labels).astype("float32")
y_test = np.asarray(test_labels).astype("float32")

neural_network = Sequential()
neural_network.add(Dense(16, activation="relu", input_shape = (10_000,)))
neural_network.add(Dense(16, activation="relu"))
neural_network.add(Dense(1, activation="sigmoid"))

# TODO co je binary_crossentropy a co je categorical_crossentropy ???
neural_network.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])

history = neural_network.fit(x_train, y_train, epochs = 20, batch_size = 128, validation_data = (x_test, y_test))

result = neural_network.evaluate(x_test, y_test)
print(result)

