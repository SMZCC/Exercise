# coding=utf-8
# date: 2018-8-22,16:29:47
# name: smz

import torch as th
import numpy as np

"""
tensor是torch的基础类
基本方法有：
    .type() 返回值为设定的数据类型
    .mm(tensor_b) 与tensor_b进行正常的矩阵乘积
    .clamp(min, max) 将tensor的值限定在[min, max],可以只有一个参数[min, +inf)或(-inf, max]
    .t()  转置
    .clone() 拷贝
    .pow()
    .sum()
    .zero_() 在反向传播更新完梯度的时候,需要将对应的梯度值变为0,防止梯度累加
基本数据类型有：
    torch.FloatTensor
    torch.IntTensor
    以上每种类型都有对应的cuda类型
    torch.cuda.FloatTensor
"""