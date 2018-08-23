# coding=utf-8
# date: 2018-8-22,20:52:00
# name: smz

import torch as th
"""
从均匀分布中随机取值,取值范围为[0, 1)
tensor = torch.rand(shape)
"""

def demo_rand():
    tensor_a = th.rand((3, 2))
    print tensor_a

if __name__ == '__main__':
    demo_rand()