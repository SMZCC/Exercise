# coding=utf-8
# date: 2018-10-29,20:19:39
# name: smz

import numpy as np


def demo_one():
    array1 = np.array([[1, 2], [3, 4]])
    array2 = np.array([[5, 6], [7, 8]])
    res1 = np.concatenate((array1, array2), axis=0)
    res2 = np.concatenate((array1, array2), axis=1)
    print "res1:", res1
    print "res2:", res2


if __name__ == '__main__':
    demo_one()
