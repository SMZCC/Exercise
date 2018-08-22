# coding=utf-8
# date: 2018-8-22,17:24:03
# name: smz

import torch as th
"""
torch.randn(shape), 
- 从均值为0,方差为1的正态分布中随机取值
- 返回一个Tensor
"""

def demo_th_randn():
    tensor_a = th.randn((2, 3))
    print 'tensor_a:\n', tensor_a

if __name__ == '__main__':
    demo_th_randn()