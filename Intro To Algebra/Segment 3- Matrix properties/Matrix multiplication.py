import numpy as np
import tensorflow as tf
import torch


A = np.array([[3, 4], [5, 6], [7, 8]])
b = np.array([1, 2])
C_mv = np.dot(A, b) # even though technically dot products are between vectors only

A_pt = torch.tensor([[3, 4], [5, 6], [7, 8]])
b_pt = torch.tensor([1, 2])
C_pt_mv = torch.matmul(A_pt, b_pt) # like np.dot(), automatically infers dims in order to perform dot product, matvec, or matrix multiplication

A_tf = tf.Variable([[3, 4], [5, 6], [7, 8]])
b_tf = tf.Variable([1, 2])
C_tf_mv = tf.linalg.matvec(A_tf, b_tf)

print(C_mv)
print(C_pt_mv)
print(C_tf_mv)


B = np.array([[1, 9], [2, 0]])
C_mm = np.dot(A, B)

B_pt = torch.from_numpy(B) # much cleaner than TF conversion
# another neat way to create the same tensor with transposition:
B_pt = torch.tensor([[1, 2], [9, 0]]).T
C_pt_mm = torch.matmul(A_pt, B_pt) # no need to change functions, unlike in TF


B_tf = tf.convert_to_tensor(B, dtype=tf.int32)
C_tf_mm = tf.matmul(A_tf, B_tf)

print(C_mm)
print(C_pt_mm)
print(C_tf_mm)