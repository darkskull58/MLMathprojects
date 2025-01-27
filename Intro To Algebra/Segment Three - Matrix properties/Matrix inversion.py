import numpy as np
import tensorflow as tf
import torch


#for equations: 4b + 2c = 4 and -5b =3c = -7
#solving for w, that is b and c (weights)

X = np.array([[4, 2], [-5, -3]])
Xinv = np.linalg.inv(X)  # inverse in numpy
y = np.array([4, -7])
w = np.dot(Xinv, y)
print(w)


torch.inverse(torch.tensor([[4, 2], [-5, -3.]])) # inverse in float type in pytorch

tf.linalg.inv(tf.Variable([[4, 2], [-5, -3.]])) # inverse in float in tensorFlow