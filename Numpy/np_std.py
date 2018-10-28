# coding=utf-8
# date: 2018-10-28,16:49:15
# name: smz

import numpy as np
"""
std = np.std(seq, axis=0)
计算指定轴内元素的标准差
注:
    方差: 各个数减去均值后的平方的和,再求平均
    标准差: 方差的开方
"""


def demo():
    nums = range(9)
    std = np.std(nums, axis=0)
    print std


if __name__ == '__main__':
    demo()