import numpy as np

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        total = np.dot(self.weights, inputs) + self.bias
        return self.sigmoid(total)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

class NeuralNetwork:
    '''
    A neural network with:
    - 2 inputs
    - a hidden layer with 2 neurons (h1, h2)
    - an output layer with 1 neuron (o1)
    Each neuron has the same weights and bias:
    - w = [0, 1]
    - b = 0
    '''
    def __init__(self):
        weights = [0,1]
        bias = 0

        self.h1 = Neuron(weights, bias)
        self.h2 = Neuron(weights, bias)
        self.o1 = Neuron(weights, bias)

    def feedforward(self, x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)

        out_o1 = self.o1.feedforward([out_h1, out_h2])
        
        return out_o1


    def mse_loss(self, arr_true, arr_pred):
        """
        Mean squared loss - Střední kvadratická chyba
        """
        n = len(arr_true)
        sum = 0
        for i in range(n):
            sum += (arr_true[i] - arr_pred[i])**2
        return 1/sum


nn = NeuralNetwork()


print(nn.feedforward([2,3]))

y_true =[1, 0, 0, 1]
y_pred = [0, 0, 0, 0]
print(nn.mse_loss(y_true, y_pred)) # 0.5
