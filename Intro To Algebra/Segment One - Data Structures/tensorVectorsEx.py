import numpy as np
import tensorflow as tf
import torch

#numpy
x = np.array([2,3,5])
print(f"2D tensor X: {x}")
print(len(x))
print(x.shape)
print(type(x))
print(x[0])

x2 = np.array([[2,3,5]])
print(f"3D tensor X2: {x2}")

xT = x2.T #numpy transpose operation
print(f"tensor transpose XT: {xT}")

#pytorch and tensorflow

x_pt = torch.tensor([25,30,35])
print(f"pytorch tensor: {x}")

x_tf = tf.Variable([10,20,30])
print(f"tensorFlow tensor: {x_tf}")