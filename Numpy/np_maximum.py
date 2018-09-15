# coding=utf-8
# date:2018-9-15,20:55:27
# name: smz

import numpy as np
"""
max_value_array = np.maximum(x1, x2, *args, *kwargs)  ==> ndarray
逐元素比较两个array的大小,返回值大的元素,若是相同返回第一个array的元素
                  
"""


def demo_one():
    array_one = np.array([[1, 2], [3, 4]])
    array_two = np.array([[3, 3]])  # 可以被广播为和array_one一样大
    max_value_array = np.maximum(array_one, array_two)

    print 'np.maximum(array_one, array_two):\n', max_value_array  # [[3 3]
                                                                  # [3 4]]



if __name__ == '__main__':
    demo_one()