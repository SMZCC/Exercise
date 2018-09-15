# coding=utf-8
# date: 2018-9-14,20:40:52
# name: smz

import numpy as np
"""
array = np.random.randn(dim0, dim1, ...)
从均值为0,方差为1的正态分布中采样,样本的维度信息由*dims决定
arguments:
    *dims: 用来指定返回的维度信息,若什么都不指定的话,就返回一个float值
    
注意：
    1.如果想用<Tuple>来指定样本的维度信息的话,就使用np.random.standard_normal()
    2.若想从任意的N(\mu, \sigma^2)的分布中采样,可使用下式
        array = sigma * np.random.randn(...) + mu
        例如: 从N(3, 6.25)的分布中采样(2,4)的array:
            由于\sigma^2 = 6.25 ==> \sigma = 2.5,而\mu显然为3,所以:
            array = 2.5 * np.random.randn(2, 4) + 3
"""


def demo_one():
    array_one = np.random.randn()
    print 'array_one:', array_one  # float,没有轴


def demo_two():
    array_two = np.random.randn(1)
    print 'array_two:', array_two   # (1, )轴为1


if __name__ == '__main__':
    demo_one()
    demo_two()