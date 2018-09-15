# coding=utf-8
# date: 2018-9-15,19:56:11
# name: smz


from __future__ import division
"""
py2.7中 / 和 // 都是取整除法,只保留整数部分,去尾
若想不是取整除法:
    1.使用from __future__ import division,取整可用//
    2.将除数或者被除数写成浮点类型即可

注意:
    1.无论是使用__future__或者是使用float数来达到/不是取整除法的目的时,通过//取整得到的数的类型都要取决于被除数和除数的类型
      若是被除数和除数中有float类型的话,那么取整的结果为float类型,从这个方面来讲,float方法的取整结果都是float类型的
      只有使用__future__方法的情况下,被除数和除数才有可能都是int型,而且/的结果是带小数,而//的结果是int型

"""


def demo_one():
    """运行这个之前,注释掉from __future__ import division"""
    print '3/2:', 3/2      # 1
    print '3 // 2:', 3//2  # 1
    print '3./2:', 3./2    # 1.5
    print '3/2.:', 3/2.    # 1.5
    print '3.//2:', 3.//2  # 1.0
    print '3//.2:', 3//.2  # 14 ???,不是15?
    print '3//2.:', 3//2.  # 1.0
    print '3.4//2:', 3.4//2  # 1.0


def demo_two():
    """运行这个demo之前不要注释掉from __future__ import division"""
    print '3/2:', 3/2     # 1.5
    print '3//2:', 3//2   # 1
    print '3./2:', 3./2   # 1.5
    print '3.//2:', 3.//2 # 1.0


if __name__ == '__main__':
    # demo_one()
    demo_two()