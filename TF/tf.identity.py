# coding=utf-8
# date: 2018-4-11,21:13:29
# name: smz


import tensorflow as tf


def example_one():
    x = tf.Variable(0.0)
    x_plus_1 = tf.assign_add(x, 1)

    with tf.control_dependencies([x_plus_1]):
        y = x
    init = tf.global_variables_initializer()

    with tf.Session() as session:
        init.run()
        for i in range(5):
            print'example_one y: ', y.eval()    # 0, 0, 0, 0, 0, dependencies未被执行
        # print 'example one tf.global_variables:', tf.global_variables()   # 只有一个 tf.global_variables: [<tf.Variable 'Variable:0' shape=() dtype=float32_ref>]

def example_two():
    x = tf.Variable(0.0)
    x_plus_1 = tf.assign_add(x, 1)

    with tf.control_dependencies([x_plus_1]):
        y = tf.identity(x)
    init = tf.global_variables_initializer()
    with tf.Session() as session:
        init.run()
        for i in range(5):
            print 'example_two y: ', y.eval()  # 1, 2, 3, 4, 5
        print 'example_two x: ', x.eval()
        # print 'example_two tf.global_variables:', tf.global_variables()  # 只有一个

def example_three():
    x = tf.Variable(0.0)
    x_plus_1 = tf.assign_add(x, 1)


    with tf.control_dependencies([x_plus_1]):
        y = x
        sess = tf.InteractiveSession()
        init = tf.global_variables_initializer()
        sess.run(init)

        for i in range(5):
            print 'example_three y:', sess.run(y)  # 1., 1., 1., 1., 1. 执行一次dependencies
        print 'example_three x:', sess.run(x)  # 1. 被执行一次
        # print 'example_three tf.global_variables:', tf.global_variables() # 只有一个


def exampel_four():
    x = tf.Variable(0.0)
    y = tf.Variable(0.0)
    x_plus_1 = tf.assign_add(x, 1)

    with tf.control_dependencies([x_plus_1]):
        tf.assign(y, x)

    init = tf.global_variables_initializer()
    with tf.Session() as session:
        init.run()
        for i in range(5):
            print 'example_four y: ', y.eval()  # 0., 0., 0., 0., 0.
        print 'example_four x: ', x.eval()
        # print 'example_two tf.global_variables:', tf.global_variables()  # 只有一个

def example_five():
    x = tf.Variable(0.0)
    x_plus_1 = tf.assign_add(x, 1)

    with tf.control_dependencies([x_plus_1]):
        y = tf.identity(x)
    init = tf.global_variables_initializer()
    init.run()
    print 'example_five y:', y.eval()  # 依赖被执行了


if __name__ == '__main__':
    example_one()
    example_two()
    example_three()
    exampel_four()
    example_five()
