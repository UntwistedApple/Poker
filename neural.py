from numpy import exp, array, random, dot
import time


class neural_network:

    def __init__(self):
        random.seed(1)
        self.weights = 2 * random.random((5, 1)) - 1

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def train(self, inputs, outputs, num):
        for iteration in range(num):
            output = self.think(inputs)
            error = outputs - output
            adjustment = dot(inputs.T, error * output*(1-output))
            self.weights += adjustment

    def think(self, inputs):
        result = self.__sigmoid(dot(inputs, self.weights))
        return result

neuron = neural_network()

inputs = array([[1, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 0, 1]])
outputs = array([[1, 1, 0]]).T

neuron.train(inputs, outputs, 10000)

print(neuron.think(array([1, 0, 0, 1, 0])))

