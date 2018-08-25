# coding=utf-8
# date: 2018-8-22,16:35:17
# name: smz

import  numpy as np
"""
np的基础类,基本方法有：
    .astype()
    .T
    .dot()
    .mean(axis=1) 计算时是axis轴内一个元素依次取一个值计算一个均值,直至所有的元素取尽
                  如: [[1, 2], [3, 4]],axis=0, 0轴内有两个元素[1, 2], [3, 4], 依次取一个1+3=>2, 2+4=>3 ==>[2, 3]
"""
def demo_array():
    matrix_a = np.array([[1, 2], [3, 4]])
    print 'matrix_a.mean(axis=1):\n', matrix_a.mean(axis=1)
    print 'matrix_a.mean(axis=0):\n', matrix_a.mean(axis=0)


if __name__ == '__main__':
    demo_array()