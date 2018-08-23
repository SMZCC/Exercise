# coding=utf-8
# date: 2018-8-23,19:32:31
# name: smz

import numpy as np

"""
np.random.permutation(int/ndarray)
若是int 先生成range(int), 然后再将元素打乱
若是ndarray,将ndarray中的元素打乱
注意：
    其打乱的也就是第一个轴内(索引为0)的元素 => [[1, 2], [3, 4]]最多会变为: [[3, 4], [1, 2]],但不会变为: [[1, 3], [2, 4]]等等
"""

def demo_permutation():
    demo_one = np.random.permutation(5)
    demo_two = np.random.permutation(np.array([[1, 2], [3, 4]]))
    print 'int:\n', demo_one
    print 'ndarray:\n', demo_two


if __name__ == '__main__':
    demo_random_permutation()