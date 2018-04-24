import tensorflow as tf


#constants
a = tf.constant(5)
b = tf.constant(6)

y = tf.add(a,b)

with tf.Session() as sess:
	print(sess.run(y))


#placeholders
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

y = tf.add(a,b)

with tf.Session() as sess:
	print(sess.run(y,feed_dict={a:5,b:6}))



#Variables
a = tf.Variable(5)
b = tf.Variable(6)

y = tf.add(a,b)

init = tf.global_variables_initializer()
with tf.Session() as sess:
	sess.run(init)
	print(sess.run(y))
