# coding=utf-8
# date: 2018-9-18,14:02:11
# name: smz

import numpy as np
"""
v = np.round(a, decimals=0)
返回5舍6入的数值,decimals表示要保存的位数
注意:
    1.np.round实际是调用的around函数
    2.np.around()功能与np.round()是一样的
"""


def demo_one():
    print 'np.round(0.4):', np.round(0.4)  # 0.0
    print 'np.round(0.5):', np.round(0.5)  # 0.0
    print 'np.round(0.6):', np.round(0.6)  # 1.0


if __name__ == '__main__':
    demo_one()