import numpy as np
import tensorflow as tf
import torch


#numpy
X = np.array([[25, 2], [5, 26], [3, 7]])
print(X)
print(X.T)

#torch
X_pt = torch.tensor([[25, 2], [5, 26], [3, 7]])
print(X_pt.T)

#tensorFlow
X_tf = tf.Variable([[25, 2], [5, 26], [3, 7]])
print(tf.transpose(X_tf))