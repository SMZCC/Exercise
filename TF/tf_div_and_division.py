# coding=utf-8
# date: 2018-4-26,19:11:23
# name: smz

from __future__ import division

import tensorflow as tf


def example_div():
    matrix_a = tf.convert_to_tensor([[1, 2], [3, 4]], dtype=tf.float32)
    matrix_b = tf.convert_to_tensor([[1, 2], [3, 4]], dtype=tf.float32)
    resutl_one = tf.div(matrix_a, matrix_b)   # elementwise

    with tf.Session() as sess:
        print '-' * 50 + 'example_div' + '-' * 50
        print sess.run(fetches=[resutl_one])


def example_division():
    matrix_a = tf.convert_to_tensor([[1, 2], [3, 4]], dtype=tf.float32)
    matrix_b = tf.convert_to_tensor([[1, 2], [3, 4]], dtype=tf.float32)
    result_two = tf.division   # 这个东西不是除法

if __name__ == '__main__':
    example_div()