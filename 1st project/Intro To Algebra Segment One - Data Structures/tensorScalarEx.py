import torch
import tensorflow as tf


#tensorFlow scalar examples
tf.Variable

x_tf = tf.Variable(25)
print(x_tf)
print(x_tf.shape)

y_tf = tf.Variable(5)

#adding tensorflow
sum_tf =  x_tf + y_tf
tf_sum = tf.add(x_tf, y_tf)

print(sum_tf)
print(tf_sum)

print(type(tf_sum.numpy())) #transforming tensorFlow tensor to numpy array

#tensorFlow float example

tf_float = tf.Variable(20, dtype=tf.float16)
print(tf_float)


#pytorch tensor examples
x_pt = torch.tensor(25)
print(x_pt)
print(x_pt.shape)