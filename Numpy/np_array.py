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
    .copy()       np中对象中似乎都有该方法,用于复制一个对象返回
注：
    1.np.array()中元素的类型可以是各种数值类型,也可以是bool类型,甚至还可以是str类型
    2.轴这个东西是ndarray中的概念,即使是一个数,也是有轴的,因为np.array(这里不可使用4这种没有轴的数字,至少也要写成[4])
"""


def demo_array():
    matrix_a = np.array([[1, 2], [3, 4]])
    print 'matrix_a.mean(axis=1):\n', matrix_a.mean(axis=1)
    print 'matrix_a.mean(axis=0):\n', matrix_a.mean(axis=0)


if __name__ == '__main__':
    demo_array()