import numpy as np
#import tensorflow as tf
import torch

#numpy
x = np.array([2,3,5])

print(np.abs(2)+np.abs(3)+np.abs(5)) #print L1 norm of x array manually

print((2**2 + 3**2 + 5**2)) #print squared L2 norm of x array manually

print(np.dot(x,x)) #squared L2 norm in equal to dot product of x and x

print(np.max([np.abs(2),np.abs(3),np.abs(5)])) #print Max norm of x array manually