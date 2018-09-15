# coding=utf-8
# date: 2018-8-29,00:18:14
# name: smz

import torch as th
"""
关系运算符,这里主要讨论矩阵和单个值比较的情况:
    1.关系运算符的结果会将符合关系的元素置为1,将不符合关系的元素置为0
    2.结果中元素的类型为torch.ByteTensor
"""
def demo_larger():
    tensor_a = th.Tensor([[1, 2], [3, 4]])
    threshold = 3
    result = tensor_a > threshold
    print 'tensor_a > 3:', result


if __name__ == '__main__':
    demo_larger()