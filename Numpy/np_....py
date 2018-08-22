# coding=utf-8
# date: 2018-8-21,12:03:24
# name: smz

import numpy as np

"""
矩阵操作中三个点是表示取该轴所有元素,同：
"""

def demo():
    matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
    print 'matrix_a[...]:\n', matrix_a[...]
    print 'matrix_a[0][...]:\n', matrix_a[0][...]

    matrix_b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # (2, 2, 2)
    print 'matrix_b[0, ...]:\n', matrix_b[0, ...]
    print 'matrix_b[0, :, :]:\n', matrix_b[0, :, :]
    print 'matrix_b[0, :]:\n', matrix_b[0, :]
    print 'matrix_b[0]:\n', matrix_b[0]

    print 'matrix_b[0, ..., 1]:\n', matrix_b[0, ..., 1]  # 第一个轴取索引为0的值,第二个轴全取,第三个轴取索引为1的值
    print 'matrix_b[0, :, 1]:\n', matrix_b[0, :, 1]


if __name__ == '__main__':
    demo()