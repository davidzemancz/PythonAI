import numpy as np

class Layer:
    def __init__(self, weights, biases):
        self.input = np.array([])
        self.output = np.array([])
        self.weights = np.array(weights)
        self.biases = np.array(biases)
        self.learing_rate = 0.3
        
        self.biases_new = np.array(biases)
        self.weights_new = np.array(weights)
        pass

    def sigmoid(self, value):
        return 1 / (1 + np.exp(-value))

    def sigmoid_deriv(self, value):
        return self.sigmoid(value)*(1 - self.sigmoid(value))

    def activation(self, value):
        return self.sigmoid(value)

    def feed_forward(self, input):
        self.input = input

        result = np.dot(self.weights, self.input.T)
        result += self.biases
        for i in range(len(result)):
            result[i] = self.activation(result[i])

        self.output = result
        return self.output
    
    def mse_loss(y_true, y_pred):
        return ((y_true - y_pred) ** 2).mean()

    def feed_backwards(self, expected, prev_layer = None):
        for row in range(len(self.weights)):
            for col in range(len(self.weights[row])):
                
                if prev_layer is not None:
                    sum = 0
                    for row_2 in range(len(prev_layer.weights)):
                        weight_prev = prev_layer.weights[row_2][row]
                        sum += weight_prev * self.sigmoid_deriv(self.output[row_2]) * 2 * (self.output[row_2] - expected[row_2])
                    
                    result = self.input[col] * self.sigmoid_deriv(self.output[row]) * sum
                    result_b = self.input[col] * self.sigmoid_deriv(self.output[row]) * sum
                    
                else:
                    result = self.input[col] * self.sigmoid_deriv(self.output[row]) * 2 * (self.output[row] - expected[row])
                    result_b = self.sigmoid_deriv(self.output[row]) * 2 * (self.output[row] - expected[row])
                
                self.weights_new[row][col] = self.weights_new[row][col] - self.learing_rate * result
                
                self.biases_new[row] = self.biases_new[row] - self.learing_rate * result_b

    
    def push(self):
        self.weights = self.weights_new
        self.biases = self.biases_new