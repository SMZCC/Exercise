# coding=utf-8
# date: 2018-9-15,21:40:38
# name: smz

import numpy as np
"""
ndarray = np.clip(matrix_a, a_min, a_max)  ===> ndarray
将矩阵matrix_a中的小于a_min的元素使用a_min代替,大于a_max的元素使用a_max代替
返回的array中的元素\in [a_min, a_max]
"""


def demo_one():
    matrix = np.clip([24], 10, 12)
    print 'np.clip([24], 10, 12):', matrix


if __name__ == '__main__':
    demo_one()