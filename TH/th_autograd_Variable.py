# coding=utf-8
# date: 2018-8-22,16:53:07
# name: smz

import torch as th
import numpy as np
from torch.autograd import Variable

"""
from torch.autograd import Variable
Variable是封装了Tensor的类,主要是用于计算梯度用的,其属性,requires_grad默认是False
x = Variable(Tensor, requires_grad=False)  
基本属性：
    x.data  Tensor,x的值,具有一定的形状,取值的话,需要通过索引
    x.grad  Variable, x对应的梯度值
基本方法：
    基本同Tensor
    x.backward()  当x为loss的时候
    x.grad.data.zero_()  将梯度值重置为0
    
注意:
    1. 没有.copy_()方法,所以一个<Variable>调用.copy_()的话是会报错的,这个错误极可能隐秘地发生在恢复模型的时候
       由于模型中的参数都是<Parameter>的,而<Parameter>都是继承<Variable>的,所以若是使用<Parameter>.copy_()来
       恢复权值的话,是会报错的
    2. 使用赋值符号=来替换值
"""


def demo_variable():
    matrix_a = np.array([[1, 2], [3, 4]])
    var_a = Variable(th.from_numpy(matrix_a))
    print 'var_a:', var_a
    print 'var_a.requires_grad:', var_a.requires_grad

if __name__ == '__main__':
    demo_variable()