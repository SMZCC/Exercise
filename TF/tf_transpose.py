# coding=utf-8
# date: 2018-4-25,21:11:00
# name: smz

import tensorflow as tf

"""使用transpose转置矩阵"""

def trans_matrix_one():
    matrix_one = tf.convert_to_tensor([[1, 2], [3, 4]])
    with tf.Session() as sess:
        matrix_one_T = sess.run(tf.transpose(matrix_one, (1, 0)))

    print '-' * 50 + 'trans_matrix_one' + '-' * 50
    print 'matrix_one_T:\n', matrix_one_T


if __name__ == '__main__':
    trans_matrix_one()