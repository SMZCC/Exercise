# coding=utf-8
# date: 2018-9-15,20:11:57
# name: smz

import numpy as np
"""
ndarray = np.random.rand(*dims)
从[0, 1)的均匀分布中随机取出维度大小为*dims的ndarray

说明:
    1.如果给*dims赋值了,那么赋了几个值,返回的结果就是几个轴的
    2.如果不给*dims赋值,那么返回的就是一个从[0, 1)的均匀分布中随机取出来的一个值,该值没有轴
"""


def demo__one():
    uniform_array_one = np.random.rand(1, 4)
    print 'np.random.rand(1, 4):', uniform_array_one

    uniform_array_two = np.random.rand(4)
    print 'np.random.rand(4):', uniform_array_two

    uniform_array_three = np.random.rand()
    print 'np.random.rand():', uniform_array_three


if __name__ == '__main__':
    demo__one()