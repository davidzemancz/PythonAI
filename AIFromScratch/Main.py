import sys
import numpy as np
import matplotlib

np.random.seed(0)

inputs = np.array([[1, 2, 3, 2.5],
          [2, 5, -1, 2],
          [-1.5, 2.7, 3.3, -0.8]])

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
        self.output = None

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer_1 = Layer_Dense(4, 5)
layer_2 = Layer_Dense(5, 2)

layer_1.forward(inputs)
#print(layer_1.output)
layer_2.forward(layer_1.output)
print(layer_2.output)