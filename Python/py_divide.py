# coding=utf-8
# date: 2018-9-15,19:56:11
# name: smz

"""
py2.7中 / 和 // 都是取整除法,只保留整数部分
若想不是取整除法:
    1.使用from __future__ import division,取整可用//
    2.将除数或者被除数写成浮点类型即可

"""


def demo_one():
    print '3/2:', 3/2      # 1
    print '3 // 2:', 3//2  # 1
    print '3./2:', 3./2    # 1.5
    print '3/2.:', 3/2.    # 1.5
    print '3.//2:', 3.//2  # 1.0
    print '3//.2:', 3//.2  # 14 ???,不是15?
    print '3//2.:', 3//2.  # 1.0


if __name__ == '__main__':
    demo_one()