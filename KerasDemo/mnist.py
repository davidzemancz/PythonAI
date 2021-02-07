from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras import utils

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

neural_network = Sequential()
neural_network.add(Dense(512, activation="relu", input_shape=(28 * 28, )))
neural_network.add(Dense(10, activation="softmax"))
neural_network.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])

train_images = train_images.reshape(60_000, 28 * 28)
train_images = train_images.astype("float32") / 255

test_images = test_images.reshape(10_000, 28 * 28)
test_images = test_images.astype("float32") / 255

train_labels = utils.to_categorical(train_labels)
test_labels = utils.to_categorical(test_labels)

neural_network.fit(train_images, train_labels, epochs = 5, batch_size = 128)

test_loss, test_acc = neural_network.evaluate(test_images, test_labels)
print("test_acc:", test_acc)