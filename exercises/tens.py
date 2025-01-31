import numpy as np
import tensorflow as tf

coff = np.array([[2.0], [-20.], [30.]], dtype=float)

w = tf.Variable(0.0, dtype=tf.float32)
x = tf.placeholder(tf.float32, [3, 1])

cost = w ** x[0][0] + x[1][0] * w + x[2][0]

train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

init = tf.global_variables_initializer()
session = tf.Session()
session.run(init)
for i in range(1000):
    session.run(train, feed_dict={x: coff})
print(session.run(w))
