# coding=utf-8
# date: 2018-8-21,11:58:46
# name: smz

import numpy as np

"""
np.newaxis要看是在哪个轴上使用的,在哪个轴使用的,就会在该轴元素外面套一个轴
"""

def demo():
    matrix_a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])  # (3, 4)

    matrix_b = matrix_a[..., np.newaxis]    # (3, 4, 1)
    print 'matrix_b shape:', matrix_b.shape
    print 'matrix_b:\n', matrix_b
    print

    matrix_c = matrix_a[np.newaxis, ...]  # (1, 3, 4)
    print 'matrix_c shape:', matrix_c.shape
    print 'matrix_c:\n', matrix_c

if __name__ == '__main__':
    demo()
