import numpy as np

class Layer:
    def __init__(self, weights, biases):
        self.neurons = np.array([])
        self.weights = weights
        self.biases = biases
        pass

    def sigmoid(self, value):
        return 1 / (1 + np.exp(-value))

    def relu(self, value):
        return max(0, value)

    def activation(self, value):
        return self.relu(value)

    def feed(self, neurons):
        result = np.dot(self.weights, neurons.T)
        result += self.biases
        for i in range(len(result)):
            result[i] = self.activation(result[i])

        self.neurons = result
        return self.neurons
        

