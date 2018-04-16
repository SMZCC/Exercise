# coding=utf-8
# date: 2018-4-13,18:03:50
# name: smz

import tensorflow as tf
from tensorflow.python import debug as tfdbg


def example_control_one():

    x = tf.Variable(1)
    y = tf.add(x, 1)

    with tf.control_dependencies([y]):
        z = y

    init = tf.global_variables_initializer()
    sess = tf.InteractiveSession()
    sess.run(init)
    # sess = tfdbg.LocalCLIDebugWrapperSession(sess)
    print '-' * 50 + 'one' + '-' * 50
    for i in xrange(4):
      print 'x:', sess.run(x),'|', 'y:', sess.run(y)  # 依赖成功执行

def example_control_two():
    x = tf.Variable(1)
    y = tf.add(x, 1)

    with tf.control_dependencies([y]):
        z = tf.identity(y)   # 这里修改为tf.identity   # 结果一样只执行了一次依赖,不一定只执行了一次依赖,因为y的值来源于x,而x未发生改变

    init = tf.global_variables_initializer()
    sess = tf.InteractiveSession()
    sess.run(init)
    # sess = tfdbg.LocalCLIDebugWrapperSession(sess)
    print '-' * 50 + 'two' + '-' * 50
    for i in xrange(4):
        print 'x:', sess.run(x), '|', 'y:', sess.run(y)


def example_control_three():
    """
    将y的值直接来源于x
    :return:
    """
    x = tf.Variable(1.)
    x_plus_one = tf.add(x, 1)

    with tf.control_dependencies([x_plus_one]):
        y = x  # 这里没有操作,应该没有发生依赖关系,通过调试也发现了,这里一共只有一个变量,并没有依赖产生

    init = tf.global_variables_initializer()
    sess = tf.InteractiveSession()
    sess.run(init)
    # sess = tfdbg.LocalCLIDebugWrapperSession(sess)
    print '-' * 50 + 'three' + '-' * 50
    for i in range(5):
        print 'x:', sess.run(x), '|', 'y:', sess.run(y)

def example_control_four():
    """
    将y的值直接来源于x
    :return:
    """
    x = tf.Variable(1., name='x')
    x_plus_one = tf.add(x, 1, name='x_plus_1')

    with tf.control_dependencies([x_plus_one]):
        y = tf.identity(x)  # identity操作被建立了前提依赖,但是由于没有改变x的值(没有使用assign_add),加1后的值给了x_plus_one
    init = tf.global_variables_initializer()    # 故而,y依旧等于x的值1, 而x_plus_one的值为2,说明执行过一次依赖
    sess = tf.InteractiveSession()
    sess.run(init)
    # sess = tfdbg.LocalCLIDebugWrapperSession(sess)
    print '-' * 50 + 'four' + '-' * 50
    for i in range(5):
        print 'x:', sess.run(x), '|', 'y:', sess.run(y), '|', 'x_plus_one:', sess.run(x_plus_one)




if __name__ == '__main__':
    # example_control_one()
    # example_control_two()
    # example_control_three()
    example_control_four()