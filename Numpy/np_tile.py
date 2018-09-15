# coding=utf-8
# date: 2018-9-15,21:29:35
# name: smz

import numpy as np
"""
ndarray = np.tile(ndarry, (2, 3))
从最后一个轴开始,将每个轴内的所有元素作为一个整体重复指定次数,
对于没有指定重复次数的轴,默认重复次数为1
"""


def demo_one():
    matrix_a = np.array([[1, 2], [3, 4]])
    matrix_b = np.tile(matrix_a, [2, 2])

    print 'np.tile(matrix_a):\n', matrix_b


if __name__ == '__main__':
    demo_one()