# coding=utf-8
# date: 2018-9-14,22:37:15
# name: smz

import numpy as np
"""
empty_array = np.empty(shape, dtype=None, order='C')  => ndarray
返回一个新的ndarray, 该ndarray是空的(没有初始值,故而需要用户给每个元素赋值),但是类型为dtype类型
args:
    shape: <Tuple>
    dtype: 元素的类型
    order: str:'C' or 'F', 表示按行存储(C语言)还是按列存储(Fortran)
    
注意：
    1.若是某个轴的长度为0的话,表示该轴内并没有元素,此时即使使用索引0,也会出现IndexError异常,但是轴的个数却是依旧存在的
        如：empty_array = np.empty((0, 1, 2)), 虽然该empty_array在第一个轴上长度就是0,也就是没有元素,但是轴的个数依旧是3个
    2.长度为0的empty_array可以使用np.concatenate来填充数据,但是要注意轴的个数应该一致,否则会出现np.concatenate会出现ValueError异常
"""


def demo_one():
    empty_array_one = np.empty((0, 1))
    empty_array_two = np.empty((0))
    print 'np.empty((0, 1)):\n', empty_array_one
    print 'np.empty((0)):\n', empty_array_two
    print '*' * 70

    # empty_array_one[0, 1] = 1   # IndexError
    # empty_array_two[0] = 2      # IndexError
    # print 'empty_array_one[0, 1]:\n', empty_array_one
    # print 'empty_array_two[0]:\n', empty_array_two

    array_one = np.array([[1]])
    new_one = np.concatenate([empty_array_one, array_one], axis=0)

    array_two = np.array([2])
    new_two = np.concatenate([empty_array_two, array_two], axis=0)
    print 'np.concatenate([empty_array_one, array_one], axis=0):\n', new_one
    print 'np.concatenate([empty_array_two, array_two], axis=0):\n', new_two


if __name__ == '__main__':
    demo_one()
