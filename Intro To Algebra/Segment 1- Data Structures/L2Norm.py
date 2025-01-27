import numpy as np
#import tensorflow as tf
import torch

#numpy
x = np.array([2,3,5])

print((2**2 + 3**2 + 5**2)**(1/2)) #print L2 norm of x array manually

xN = np.linalg.norm(x) #built L2 norm function in numpy
print(f"L2 norm of x: {xN}") 