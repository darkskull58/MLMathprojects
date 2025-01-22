import numpy as np
import tensorflow as tf
import torch


X = np.array([[25, 2], [5, 26], [3, 7]])

print(f"matrix X: {X}")

# Select left column of matrix X (zero-indexed)
print(X[:,0])

# Select middle row of matrix X:
print(X[1,:])

# Another slicing-by-index example:
print(X[0:2, 0:2])

#torch
X_pt = torch.tensor([[25, 2], [5, 26], [3, 7]])
print(X_pt)
print(X_pt[1,:])


#tensorFlow
X_tf = tf.Variable([[25, 2], [5, 26], [3, 7]])
print(X_tf)

print(tf.rank(X_tf))
print(tf.shape(X_tf))
print(X_tf[1,:])