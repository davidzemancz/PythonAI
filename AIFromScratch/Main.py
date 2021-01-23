from Layer import Layer
import Loss
import numpy as np

# Vstup
input = np.array([0.3, 0.2, -0.7, 0.4]) 

weights_1 = np.array([[1, 1, 1, 1], [-0.5, -0.3, 0.7, 0.2]])
biases_1 = np.array([0, 0]) 
layer_1 = Layer(weights_1, biases_1)
print(layer_1.feed(input))


