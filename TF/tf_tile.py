# coding=utf-8
# date: 2018-3-30,22:37:49
# name: smz


import tensorflow as tf

import numpy as np
"""
tensor = tf.tile(tensor_b, [axis0, axis1, ...])
将tensor_b的各个轴内所有元素,按整体重复axis0, axis1遍
"""


def test_tile():
    sess = tf.InteractiveSession()
    matrix_a = tf.convert_to_tensor(np.array([[1, 2], [3, 4]]))
    matrix_b = tf.tile(matrix_a, [1, 2])
    print sess.run(matrix_b)       # [[1 2 1 2]
                                   #  [3 4 3 4]]
    matrix_c = tf.tile(matrix_a, [2, 1])
    print sess.run(matrix_c)       # [[1 2]
                                   #  [3 4]
                                   #  [1 2]
                                   #  [3 4]]



if __name__ == '__main__':
    test_tile()
