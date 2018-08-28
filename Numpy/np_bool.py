# coding=utf-8
# date: 2018-8-26,22:56:48
# name: smz
import numpy as np
"""
这里对于这个布尔值仅仅说明关于取值的情况：
1. 被取值的对象必须是ndarray的类型,一般的列表,元组等等不可
2. 当某个轴内需要使用多个布尔值来取值时,需要用[]括起来,如: matrix_a = [[1, 2], [3, 4]] 第一个轴内取[3, 4],不取[1, 2]的索引为matrix_a[[False, True]]
3. 利用布尔矩阵和另一个矩阵相乘,可以将不需要的值变为0
4. 利用布尔取值取出来的值会被当作元素处理,外面会被再添加一个轴,如: matrix_a = [[1, 2]], matrix_a[True] : [[[1, 2]]]
"""
def demo_bool_fetch_value():
    matrix_a = np.array([1, 2, 3, 4])
    print 'matrix_a[[True, False, True, False]]:\n', matrix_a[[True, False, True, False]]  # [True, False, True, False]表示第一个轴内取这些元素

    matrix_b = np.array([[True, False], [False, True]])   # 将不需要的值变为0
    matrix_c = np.array([[1, 2], [3, 4]])
    matrix_d = matrix_b * matrix_c
    print 'matrix_b * matrix_c:\n', matrix_d

    print 'matrix_c[[True, False], [True, False]]\n', matrix_c[[True, False], [True, False]]
    # 第一个[True, False]表示在第一个轴内,取第一个元素,不取第二个元素,结果为: [1, 3]
    # 第二个[True, False]表示在第二个轴内,取第一个元素,不取第二个元素,结果为: [1]
    print 'matrix_c[True]:\n', matrix_c[True]
    # [[[1 2]
    #   [3 4]]]
    print 'matrix_c[:]:\n', matrix_c[:]
    # [[1 2]
    #  [3 4]]

if __name__ == '__main__':
    demo_bool_fetch_value()