from Layer import Layer
import numpy as np


hidden_layer = Layer([[0.5, 0.5],[0.5, 0.5],[0.5, 0.7]],[0, 1, 0])
output_layer = Layer([[0.5, 0.4, 0.2],[0.7, 0.1, 0.5]],[0, 1])

x_1 = 0.7
x_2 = 0.2
input = np.array([x_1, x_2])

for i in range(100):
    hidden_layer_output = hidden_layer.feed_forward(input)
    output = output_layer.feed_forward(hidden_layer_output)

    print(output)

    expected = [1, 0]
    output_layer.feed_backwards(expected)
    hidden_layer.feed_backwards(expected, output_layer)

    hidden_layer.push()
    output_layer.push()




