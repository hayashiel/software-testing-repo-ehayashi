# hayashiel
# 10-21-24
# https://peps.python.org/pep-0008/#comments
# https://realpython.com/documenting-python-code/
# Use Command python -m unittest discover -p "'custom_prefix'_*.py"

# Outline:
# Create Dense Layer
# Create Softmax Layer
# Create Binary Logit Layer
# Create Model Class
# UnitTest Above Functionality.
import tensorflow as tf
import numpy as np

class Dense:
    def __init__(self, x):
        self.x = np.zeros((x, 1))
        self.b = np.zeros((1))
    def call(self, inputs):
        return tf.matmul(inputs, self.x) + self.b

class Binary(Dense):
    def __init__(self, x):
        super().__init__(x)
    def call(self, inputs):
        return 1/(1+np.exp(super().call(inputs)))
    
class Softmax(Dense):
    def __init__(self, x):
        super().__init__(x)
    def call(self, inputs):
        return np.exp(super().call(inputs))/np.sum(np.exp(super().call(inputs)))
    
class Model:
    def __init__(self, list_layer_settings):
        self.layers = []
        for layer_type, shape in list_layer_settings:
            if layer_type == "Dense":
                self.layers.append(Dense(shape))
            elif layer_type == "Binary":
                self.layers.append(Dense(shape))
            elif layer_type == "Softmax":
                self.layers.append(Dense(shape))
            else:
                self.layers.append(Dense(shape))
    def call(self, inputs):
        x = inputs
        for layer in self.layers:
            x = layer.call(x)
        return x