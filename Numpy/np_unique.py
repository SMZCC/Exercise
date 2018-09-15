# coding=utf-8
# date: 2018-8-29,22:58:26
# name: smz

import numpy as np
"""
np.unique(ar, return_index=False, return_inverse=False, return_counts=False, axis=None)
去除ndarray中的重复元素,并升序排序输出(默认)
注意:
    unique array: 没有重复元素的矩阵
    unique item : 构成unique array的元素
args:
    ----------
    ar : array_like
        输入矩阵,除非'axis'被指定了,那么这个输入矩阵将被拉成1-D
        
    return_index : bool, optional
        如果为True,同时返回构成unique array的元素的索引,如果没有提供'axis'关键字参数的话,该索引就是将输入拉成1-D的时候的元素的索引,
        若是提供了'axis',该索引就是在'axis‘内的索引
    
    return_inverse : bool, optional
        如果为True,返回 构成输入矩阵的元素在unique array中的索引是多少
        
    return_counts : bool, optional
        如果为True,返回每个元素在输入中重复的次数

    axis : int or None, optional
       指定轴内进行unique操作
"""

def demo_unique():
    matrix_a = np.array([[1, 1], [2, 2], [3, 3]])
    print 'np.unique(matrix_a, return_index=True):\n', np.unique(matrix_a, return_index=True)
    print 'np.unique(matrix_a, return_index=True, axis=1):\n', np.unique(matrix_a, return_index=True, axis=1)
    print 'np.unique(matrix_a, return_inverse=True):\n', np.unique(matrix_a, return_inverse=True)

if __name__ == '__main__':
    demo_unique()