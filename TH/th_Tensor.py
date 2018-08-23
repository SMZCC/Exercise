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
基本数据类型有：
    torch.FloatTensor
    torch.IntTensor
    以上每种类型都有对应的cuda类型
    torch.cuda.FloatTensor
"""

def demo_tensor():
    tensor_a = th.from_numpy(np.array([[1, 2], [3, 4]]))
    tensor_b = th.from_numpy(np.array([[5, 6], [7, 8]]))
    tensor_c = tensor_a.mm(tensor_b)
    tensor_d = tensor_a * tensor_b   # 哈达玛积
    tensor_e = tensor_a.view((1, 4))
    tensor_f = tensor_a.cuda()

    print 'tensor_a.mm(tensor_b):\n', tensor_c
    print 'tensor_a * tensor_b:\n', tensor_d
    print 'tensor_a.view((1, 4)):\n', tensor_e
    print 'tensor_a.cuda():', tensor_f  # gpu
    print 'tensor_a:', tensor_a        # cpu
    print 'tensor_a.size:', tensor_a.size()

if __name__ == '__main__':
    demo_tensor()