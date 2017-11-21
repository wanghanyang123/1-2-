import tensorflow as tf

x=tf.Variable([1,2])
a=tf.constant([2,2])

sub=tf.subtract(x,a)
add=tf.add(x,a)

init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(sub))
    print(sess.run(add))

#创建一个变量初始化为0
state=tf.Variable(0,name='counter')
new_value=tf.add(state,1)
update=tf.assign(state,new_value)

init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    #print(sess.run(init))
    for _ in range(5):
        sess.run(update)
        print(sess.run(state))
