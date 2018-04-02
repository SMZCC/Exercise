# coding=utf-8
# date: 2018-4-1,22:45:30
# name: smz

# ema.variables_to_restore得到的似乎是所有图的变量

import tensorflow as tf


if __name__ == '__main__':
    g_1 = tf.Graph()
    g_2 = tf.Graph()

    g_1.as_default()
    with tf.variable_scope('g1'): # 定义变量
        matrix_a = tf.get_variable(name='matrix_a', shape=(),
                                   initializer=tf.constant_initializer(3))

    matrix_b = tf.Variable(3, name='matrix_b')

    ema = tf.train.ExponentialMovingAverage(0.99)
    average_maintain_op = ema.apply([matrix_a])  # 第一个操作是给a计算影子变量

    change_a = tf.assign(matrix_a, 10)  # 第二个操作改变a的值

    sess = tf.InteractiveSession()

    g_2.as_default()
    with tf.variable_scope('g_2'):
        matrix_c = tf.get_variable(dtype=tf.float32, shape=(), name='matrix_c',
                                       initializer=tf.constant_initializer(8))

    #variables_init = tf.initialize_variables([matrix_c])
    #sess.run(variables_init)
    init = tf.global_variables_initializer()
    sess.run(init)

    print 'graph_1, variables_to_restore:', sess.run(ema.variables_to_restore())
    #print 'graph_2, variables_to_restore:', sess_2.run(ema.variables_to_restore())
    print 'matrix_a:', sess.run(matrix_a)
    print 'origin matrix_a value and average value', sess.run([matrix_a, ema.average(matrix_a)])
    _, matrix_a_ = sess.run([change_a, matrix_a])
    av = sess.run(ema.average(matrix_a))
    print 'changed matrix_a value and average value', matrix_a, av
    print 'test'

