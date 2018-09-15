# coding=utf-8
# date: 2018-8-22,16:11:54
# name: smz

import numpy as np
"""
matrix_a.dot(matrix_b)乃是正常的矩阵乘法, 同np.matmul(matrix_a, matrix_b)
"""
def demo_dot():
    matrix_a = np.array([[1, 2], [3, 4]])
    matrix_b = np.array([[5], [6]])
    matrix_c = matrix_a.dot(matrix_b)
    matrix_d = np.matmul(matrix_a, matrix_b)

    print 'matrix_a.dot(matrix_b):\n', matrix_c
    print 'matrix_a:\n', matrix_a
    print 'np.matmul(matrix_a, matrix_b):\n', matrix_d

if __name__ == '__main__':
    demo_dot()