import numpy as np
import tensorflow as tf
import torch


#numpy
X2 = np.array([[25, 2], [5, 26], [3, 7]])

#torch
X_pt = torch.tensor([[25, 2], [5, 26], [3, 7]])

#tensorFlow
X_tf = tf.Variable([[25, 2], [5, 26], [3, 7]])

#dot product

#numpy
X = np.array([25, 2, 5])
y = np.array([0, 1, 2])

print(np.dot(X,y))

#pytorch
x_pt = torch.tensor([25,  2,  5])
y_pt = torch.tensor([0, 1, 2])
print(torch.dot(x_pt,y_pt)) 

#tensorFlow
x_tf = ([25,  2,  5])
y_tf = tf.Variable([0, 1, 2])
print(tf.reduce_sum(tf.multiply(x_tf, y_tf)))