# coding=utf-8
# date: 2018-4-25,17:32:29
# name: smz


import tensorflow as tf
import numpy as np

def reshape_one():
    """含transpose"""
    g = tf.Graph()
    with g.as_default():
        input = tf.placeholder(dtype=tf.float32, shape=(None, 2, 2, 3), name='input')
        matrix = tf.transpose(input, (0, 3, 1, 2))
        shape = input.get_shape().as_list()
        matrix_one = tf.reshape(matrix, shape=(-1, shape[3], shape[1]*shape[2]))

    with tf.Session(graph=g) as sess:
        print '-' * 50 + 'reshape_one'+ '-' * 50
        input_data = np.array([[[[1, 2, 3], [4, 5, 6]],
                                [[7, 8, 9], [10, 11, 12]]],

                               [[[13, 14, 15], [16, 17, 18]],
                                [[19, 20, 21], [22, 23, 24]]],

                               [[[25, 26, 27], [28, 29, 30]],
                                [[31, 32, 33], [34, 35, 36]]],

                               [[[37, 38, 39], [40, 41, 42]],
                                [[43, 44, 45], [46, 47, 48]]],

                               [[[49, 50, 51], [52, 53, 54]],
                                [[55, 56, 57], [58, 59, 60]]]])   # (5, 2, 2, 3)
        print 'matrix_one:\n', sess.run(fetches=[matrix_one], feed_dict={input:input_data})  # out: (5, 3, 4)

def reshape_two():
    """不含transpose"""
    g = tf.Graph()
    with g.as_default():
        input = tf.placeholder(dtype=tf.float32, shape=(None, 2, 2, 3), name='input')
        # matrix = tf.transpose(input, (0, 3, 1, 2))  # 没有transpose的结果是不一样的
        # shape = input.get_shape().as_list()
        matrix_one = tf.reshape(input, shape=(-1, 3, 4))  # tf.reshape()中未知的batch_num使用-1代替

    with tf.Session(graph=g) as sess:
        print '-' * 50 + 'reshape_two' + '-' * 50
        input_data = np.array([[[[1, 2, 3], [4, 5, 6]],
                                [[7, 8, 9], [10, 11, 12]]],

                               [[[13, 14, 15], [16, 17, 18]],
                                [[19, 20, 21], [22, 23, 24]]],

                               [[[25, 26, 27], [28, 29, 30]],
                                [[31, 32, 33], [34, 35, 36]]],

                               [[[37, 38, 39], [40, 41, 42]],
                                [[43, 44, 45], [46, 47, 48]]],

                               [[[49, 50, 51], [52, 53, 54]],
                                [[55, 56, 57], [58, 59, 60]]]])  # (5, 2, 2, 3)
        print 'matrix_one:\n', sess.run(fetches=[matrix_one], feed_dict={input: input_data})  # out: (5, 3, 4)


if __name__ == '__main__':
    reshape_one()
    reshape_two()