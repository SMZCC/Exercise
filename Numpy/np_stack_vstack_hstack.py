# coding=utf-8
# date: 2018-10-28,21:13:19
# name: smz

import numpy as np
"""
1. res = np.vstack((array1, array2))
列元素合并
将当前的两个矩阵0轴内的所有元素作为新轴内的元素进行合并: [array1[0,...], array2[0,...]],
若array只有一个轴,那么用于合并的元素就是该轴以及该轴内的所有元素,如:array1 = [1, 2], array2 = [3, 4],
array1的0轴内的所有元素为[1, 2], array2的0轴内的所有元素为[3, 4],那么合并的结果为:[[1, 2], [3, 4]]

2. res = np.hstack((array1, array2)) 
行元素合并:是将当前两个矩阵的对应的最后一个轴内的元素进行分别合并
如array1 = [[1, 2], [3, 4]], array2 = [[5, 6], [7, 8]]
[1, 2]对应[5, 6] ==> [1, 2, 5, 6]
[3, 4]对应[7, 8] ==> [3, 4, 7, 8]
结果为: [[1, 2, 5, 6], [3, 4, 7, 8]]

3.res = np.stack((array1, array2), axis=0)
依次从两个矩阵中取出指定轴内的元素(一个一个地取,而不是一次全部取出),在这些元素的外面套上一个新轴,作为合并的轴
其他的轴原样套上 

"""


def demo_one():
    """vstack"""
    array1 = np.array([1, 2])
    array2 = np.array([3, 4])
    res = np.vstack((array1, array2))   # [[1, 2], [3, 4]]
    print res


def demo_two():
    """hstack"""
    array1 = np.array([1, 2])
    array2 = np.array([3, 4])
    res = np.hstack((array1, array2))   # [1, 2, 3, 4]
    print res


def demo_three():
    """hstack"""
    array1 = np.array([[1, 2]])
    array2 = np.array([[3, 4]])
    res = np.hstack((array1, array2))  # [[1, 2, 3, 4]]
    print res


def demo_four():
    """vstack"""
    array1 = np.array([[1, 2]])
    array2 = np.array([[3, 4]])
    res = np.vstack((array1, array2))  # [[1, 2], [3, 4]]
    print res


def demo_five():
    array1 = np.array([[1, 2], [3, 4]])
    array2 = np.array([[5, 6], [7, 8]])
    res1 = np.vstack((array1, array2))  # [[1, 2], [3, 4], [5, 6], [7, 8]]
    res2 = np.hstack((array1, array2))  # [[1, 2, 5, 6], [3, 4, 7, 8]
    print res1
    print res2


def demo_six():
    array1 = np.array([[1, 2], [3, 4]])
    array2 = np.array([[5, 6], [7, 8]])
    res0 = np.stack((array1, array2), axis=0)  # [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    res1 = np.stack((array1, array2), axis=1)  # [[[1, 2], [5, 6]], [[3, 4], [7, 8]]]
    print res1


if __name__ == '__main__':
    # demo_one()
    demo_six()