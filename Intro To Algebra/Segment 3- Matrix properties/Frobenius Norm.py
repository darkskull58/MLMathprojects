import numpy as np
import tensorflow as tf
import torch


X = np.array([[1, 2], [3, 4]])
X
XF = np.linalg.norm(X) # same function as for vector L2 norm


X_pt = torch.tensor([[1, 2], [3, 4.]]) # torch.norm() supports floats only
X_pt_f = torch.norm(X_pt)


X_tf = tf.Variable([[1, 2], [3, 4.]]) # tf.norm() also supports floats only
X_tf_f = tf.norm(X_tf)

print(XF)
print(X_pt_f)
print(X_tf_f)