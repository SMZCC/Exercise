# coding=utf-8
# date: 2018-8-26,22:35:14
# name: smz

import numpy as np
"""
matrix_a = np.array([[1, 2], [3, 4]]
where_result = np.where(matrix_a==3)
返回矩阵中符合条件的元素的索引,结果是tuple类
注意:
    1.若要将结果当作索引使用的话,要通过索引从tuple中将结果取出来
"""
def demo_where():
    vector_a = np.array([1, 3, 4, 7])
    vector_b = np.array([2, 5, 1, 3])
    where_one = np.where(vector_a>2)
    where_two = np.where(vector_b==3)

    print 'where_one:\n', where_one
    print 'where_two:\n', where_two

    matrix_a = np.array([[1,3], [3, 4]])
    where_three = np.where(matrix_a==3)
    print 'where_there:\n', where_three


if __name__ == '__main__':
    demo_where()

# where_one:
# (array([1, 2, 3]),)
# where_two:
# (array([3]),)
# where_there:
# (array([0, 1]), array([1, 0]))