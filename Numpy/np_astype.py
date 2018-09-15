# coding=utf-8
# date: 2018-8-22,16:32:10
# name: smz

import numpy as np
"""
数据类型的切换,不同的框架有不同的api,np中是astype,tf中是cast,th中是type
注：以上三者新的数据类型的是在返回值中
"""
def demo_astype():
    matrix_a = np.array([[1, 2]], dtype=int)
    print 'matrix_a dtype:\n', matrix_a
    matrix_b = matrix_a.astype(float)
    print 'matrix_b dtype:\n', matrix_b   # 此时,matrix_a的dtype依旧是int


if __name__ == '__main__':
    demo_astype()