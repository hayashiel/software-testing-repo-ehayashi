# hayashiel
# 11-6-24
# https://peps.python.org/pep-0008/#comments
# https://realpython.com/documenting-python-code/
# https://docs.python.org/3/library/inspect.html
# https://scikit-learn.org/1.5/computing.html (Section 4-7)
# https://scikit-learn.org/1.5/api/sklearn.preprocessing.html
# https://stackoverflow.com/questions/2227141/get-types-of-arguments-in-python
# Use Command python -m unittest discover -p "'custom_prefix'_*.py"
# https://www.geeksforgeeks.org/how-to-check-git-logs/
# https://realpython.com/python-string-formatting/
# https://www.atlassian.com/git/tutorials/saving-changes/git-commit

# Outline: Data Preparation
# Cleaning Methods
# Visualization Methods
# Feature Selection Methods
# Transformer / Pipelines

# Imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import *
from sklearn.pipeline import *
from sklearn.datasets import load_iris
from inspect import signature

# Test the signature function twice
def test_signature_function(integer: int, text: str) -> int:
    return integer + int(text)

def test_signature_function2(integer: int, text: str):
    print(integer)
    print(text)

print(signature(test_signature_function).__str__)
print(signature(test_signature_function2))





# Cleaning Methods
# class Solution:
#     def __init__(self, solution_dataset, list_of_funcs):
#         self.solution_dataset = solution_dataset
#         self.list_of_funcs = list_of_funcs
    
#     def fit(self):
#        if len(filter(lambda x: isinstance(x, function), self.list_of_funcs)) != len(self.list_of_funcs):
#            print("Input Valid Functions")
#            return X
#        return make_pipeline(*self.list_of_funcs).fit(X)
           
# if __name__ == "__main__":
#     sol = Solution(np.array([[1,2,3,4,5]]), StandardScaler)
#     sol.fit()


def info(dataset):
    print_message = ""
    for column in dataset:
        print_message += "{} {:.30s}".format(column[0].shape, str(type(column[0])))
    return print_message
    
dataset = load_iris(return_X_y = True)
print(dataset[0].dtype, dataset[1].shape)
print(info(dataset))

# Pointers:
#   - Print Message (Figuring out better regex + string formatting skills) https://realpython.com/python-string-formatting/
#   - Figuring out how to make a class module. ✅ 
#   - https://www.geeksforgeeks.org/class-method-vs-static-method-python/