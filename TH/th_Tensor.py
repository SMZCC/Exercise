# coding=utf-8
# date: 2018-8-22,16:29:47
# name: smz

import torch as th
import numpy as np

"""
tensor是torch的基础类
基本方法有：
    .type() 返回值为设定的数据类型
    .mm(tensor_b) 与tensor_b进行正常的矩阵乘积,哈达玛积直接使用*即可,tensor_a * tensor_b
    .clamp(min, max) 将tensor的值限定在[min, max],可以只有一个参数[min, +inf)或(-inf, max]
    .t()  转置
    .clone() 拷贝
    .pow()
    .sum()
    .zero_() 在反向传播计算梯度前,需要将各变量对应的梯度值变为0,防止梯度累加
    .vew()   相当于reshape
    .cuda()  将返回值放到gpu中,而tensor本身还是在cpu
    .size()  相当于ndarray.shape
    .new()   返回新的tensor,类型同当前调用的tensor,若不传入数值的话,就没有维度,可以传入的类型有[1, 2], (1, 2), ndarray(), 单纯的数字
             前面三个类型传入是什么,返回就是什么,只有最后传入单纯的数字的时候,.new(2, 3)是返回shape为(2, 3)的随机矩阵
    .index_select(int dim, torch.LongTensor index)  在dim维度维度上进行取值,取值的索引为后面的参数,后面的参数必须是LongTensor类型的
    .long()  将当前的tensor数据类型改变为LongTensor类型
基本数据类型有：
    torch.FloatTensor
    torch.IntTensor
    以上每种类型都有对应的cuda类型
    torch.cuda.FloatTensor
对于显示效果说明：
    在控制台上显示的时候,一行是一个最基本的元素
"""

def demo_tensor():
    tensor_a = th.from_numpy(np.array([[1, 2], [3, 4]]))
    tensor_b = th.from_numpy(np.array([[5, 6], [7, 8]]))
    tensor_c = tensor_a.mm(tensor_b)
    tensor_d = tensor_a * tensor_b   # 哈达玛积
    tensor_e = tensor_a.view((1, 4))
    tensor_f = tensor_a.cuda()
    tensor_g = tensor_a.new()
    tensor_h = tensor_a.new([[1, 2]])

    print 'tensor_a.mm(tensor_b):\n', tensor_c
    print 'tensor_a * tensor_b:\n', tensor_d
    print 'tensor_a.view((1, 4)):\n', tensor_e
    print 'tensor_a.cuda():', tensor_f  # gpu
    print 'tensor_a:', tensor_a        # cpu
    print 'tensor_a.size:', tensor_a.size()
    print 'tensor_a.new:', tensor_g
    print 'tensor_a.new([[1, 2]]):', tensor_h
    print 'tensor_a.new(1):', tensor_a.new(1)              # 随机一个数,范围不清楚
    print 'tensor_a.new((2, 3)):', tensor_a.new((2, 3))    # 就是[2, 3]
    print 'tensor_a.new(np.array([1, 2])):', tensor_a.new(np.array([1, 2])) # 就是[1, 2]
    print 'tensor_a.new(2, 3):', tensor_a.new(2, 3)        # 随机(2, 3)的数,范围不清楚
    print 'tensor_a.index_select(0, th.from_numpy(np.array([1])).long()):', tensor_a.index_select(0, th.from_numpy(np.array([1])).long())


if __name__ == '__main__':
    demo_tensor()