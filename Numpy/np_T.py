# coding=utf-8
# date: 2018-8-22,15:48:37
# name: smz

import numpy as np
"""
numpy中的array对象的方法T表示转置,同np.transpose(ndarray, (1, 0))
"""

def demo_T():
    matrix_a = np.array([[1, 2], [3, 4], [5, 6]])
    print 'matrix_a.T:\n', matrix_a.T
    print 'np.transpose(matrix_a, (1, 0)):\n', np.transpose(matrix_a, (1, 0))

if __name__ == '__main__':
    demo_T()