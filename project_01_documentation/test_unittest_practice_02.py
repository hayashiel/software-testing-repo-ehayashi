# Pleace remember to 
import unittest
import numpy as np

# Import Classes
from unittest_practice_02 import *

# TestCase Class for testing the Dense Class.
class TestLinear(unittest.TestCase):
    # Set up for Unit Test
    def setUp(self):
        self.linear = Dense(5, 1)
    def test_multiplication_shape(self):
        self.assertTrue(self.linear.call(np.ones((1,5))).shape, np.ones((5,1)).shape)


class TestBinary(unittest.TestCase):
    def setUp(self):
        self.binary = Binary(5, 1)
    def test_multiplication_shape(self):
        self.assertTrue(self.binary.call(np.ones((1,5))).shape, np.ones((5,1)).shape)
    def test_range_values(self):
        self.assertTrue(np.min(self.binary.call(np.ones((1,5)))) >= 0)
        self.assertTrue(np.min(self.binary.call(np.ones((1,5)))) <= 1)

class TestSoftmax(unittest.TestCase):
    def setUp(self):
        self.softmax = Softmax(5,1)
    def test_multiplication_shape(self):
        self.assertTrue(self.softmax.call(np.ones((1,5))).shape, np.ones((5,1)).shape)
    def test_range_values(self):
        self.assertTrue(np.min(self.softmax.call(np.ones((1,5)))) >= 0)
        self.assertTrue(np.min(self.softmax.call(np.ones((1,5)))) <= 1)

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = Model([("Dense", 100, 10), ("Dense", 10,2), ("Binary", 2,1)])
    def test_model(self):
        self.assertTrue(self.model.call(np.ones((5,100))).shape == np.ones((5,1)).shape)    


