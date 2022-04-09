# Construction Phase
import tensorflow as tf
'''
a = tf.variable(0.)
b = tf.constant(1.)

op_add = a.asssign(a+b)
op_multiply = b.asssign(b*2)
init = tf.global_variables_initializer()

# Execution Phase
with tf.Session() as sess:
    init.run()
    for i in range(50):
        sess.run(op_add)
        sess.run(op_multiply)
    print(a.eval())
'''
print("TensorFlow version: {}".format(tf.__version__))