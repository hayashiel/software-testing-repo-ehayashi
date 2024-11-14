# hayashiel
# 11-6-24
# https://peps.python.org/pep-0008/#comments
# https://realpython.com/documenting-python-code/
# Use Command python -m unittest discover -p "'custom_prefix'_*.py"

# Outline: (Borrowed from unittest_practice_02)
# Create Dense Layer
# Create Softmax Layer
# Create Binary Logit Layer
# Create Model Class
# UnitTest Above Functionality.

# Imports
import tensorflow as tf
import numpy as np


class Dense:
    """ Instantiate the Dense Class
    Keyword Arguments:
    x_shape -- shape of the input
    y_shape -- shape of the output
    """
    def __init__(self, x_shape, y_shape):
        self.x = np.zeros((x_shape, y_shape))
        self.b = np.zeros((y_shape))
    
    """ Call the Dense Layer
    Keyword Argument:
    inputs -- input passed as argument
    """
    def call(self, inputs):
        # Return output of linear equation
        return tf.matmul(inputs, self.x) + self.b

class Binary(Dense):
    """ Instantiate the Binary Class
    Keyword Arguments:
    x_shape -- shape of the input
    y_shape -- shape of the output
    """
    def __init__(self, x_shape, y_shape):
        super().__init__(x_shape, y_shape)

    """ Call the Binary Layer
    Keyword Argument:
    inputs -- input passed as argument
    """
    def call(self, inputs):
        # return output of sigmoid function
        return 1/(1+np.exp(super().call(inputs)))
    
class Softmax(Dense):
    """ Instantiate the Softmax Class
    Keyword Arguments:
    x_shape -- shape of the input
    y_shape -- shape of the output
    """
    def __init__(self, x_shape, y_shape):
        super().__init__(x_shape, y_shape)
    
    """ Call the Softmax Layer
    Keyword Argument:
    inputs -- input passed as argument
    """
    def call(self, inputs):
        # Return output of Logistic Function.
        return np.exp(super().call(inputs))/np.sum(np.exp(super().call(inputs)))
    
class Model:
    """ Instantiate the Model Class from a list of Layers
    Keyword Argument:
    list_layer_settings -- list of tuples, with tuple of layer type, input shape, and output shape
    """
    def __init__(self, list_layer_settings):
        self.layers = []
        for layer_type, x_shape, y_shape in list_layer_settings:
            if layer_type == "Dense":
                self.layers.append(Dense( x_shape, y_shape))
            elif layer_type == "Binary":
                self.layers.append(Dense( x_shape, y_shape))
            elif layer_type == "Softmax":
                self.layers.append(Dense( x_shape, y_shape))
            else:
                self.layers.append(Dense( x_shape, y_shape))
    
    """ Call the Model layer
    Keyword Argument: 
    inputs -- inputs into the Model
    """
    def call(self, inputs):
        x = inputs
        for layer in self.layers:
            x = layer.call(x)
        return x