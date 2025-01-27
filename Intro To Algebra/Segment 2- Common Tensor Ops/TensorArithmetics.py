import numpy as np
import tensorflow as tf
import torch


#numpy
X = np.array([[25, 2], [5, 26], [3, 7]])

print(X*2)
print(X+2)
print(X*2+2)

#torch
X_pt = torch.tensor([[25, 2], [5, 26], [3, 7]])
print(X_pt*2) # Python operators are overloaded; could alternatively use torch.mul() or torch.add()

#tensorFlow
X_tf = tf.Variable([[25, 2], [5, 26], [3, 7]])
print(X_tf*2) # Operators likewise overloaded; could equally use tf.multiply() tf.add()

A=X+2
print(A*X) # hadamard product ( element wise product of two tensors)

#Tensor Reduction

print(X.sum()) #Reduction for numpy

print(torch.sum(X_pt)) #Reduction for pytorch

print(tf.reduce_sum(X_tf)) #Reduction for tensorFlow

# Can also be done along one specific axis alone, e.g.:
print(X.sum(axis=0)) # summing over all rows (i.e., along columns)

print(X.sum(axis=1)) # summing over all columns (i.e., along rows)

print(torch.sum(X_pt, 0))

print(tf.reduce_sum(X_tf, 1))