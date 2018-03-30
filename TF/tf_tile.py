# coding=utf-8
# date: 2018-3-30,22:37:49
# name: smz


import tensorflow as tf

import numpy as np


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
