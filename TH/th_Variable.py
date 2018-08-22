# coding=utf-8
# date: 2018-8-22,16:53:07
# name: smz

import torch as th
import numpy as np
from torch.autograd import Variable

"""
Variable是封装了Tensor的类,主要是用于计算梯度用的
x = Variable(Tensor, requires_grad=True)
基本属性：
    x.data  Tensor,x的值,具有一定的形状,取值的话,需要通过索引
    x.grad  Variable, x对应的梯度值
基本方法：
    基本同Tensor
    x.backward()  当x为loss的时候
    x.grad.data.zero_()  将梯度值重置为0
"""