# coding=utf-8
# date: 2018-8-24,14:52:49
# name: smz

import numpy as np
import torch as th
"""
result = torch.stack((tensor_a, tensor_b), dim=0)
增加一个dim轴,使得该轴内的元素合并起来
参数:
    def stack(sequence, dim=0, out=None):
    Concatenates sequence of tensors along a new dimension.
    All tensors need to be of the same size.
    Arguments:
        sequence (Sequence): sequence of tensors to concatenate.
        dim (int): dimension to insert(用于插入的轴). Has to be between 0 and the number
            of dimensions of concatenated tensors (inclusive).
"""
def demo_stack():
    tensor_a = th.from_numpy(np.array([[1, 2], [3, 4]]))
    tensor_b = th.from_numpy(np.array([[5, 6], [7, 8]]))
    tensor_c = th.stack((tensor_a, tensor_b), dim=0)
    print 'torch.stack((tensor_a, tensor_b), dim=0):', tensor_c
    print 'torch.stack((tensor_a, tensor_b), dim=1):', th.stack((tensor_a, tensor_b),dim=1)  # [1, 2], [5, 6]放在一起形成新的元素[[1, 2], [5, 6]]
                                                                                       # 然后  [3, 4], [7, 8]放在一起形成新的元素[[3, 4], [7, 8]]
                                                                                       # 两个元素放到一个tensor中[[[1, 2], [5, 6]], [[3, 4], [7, 8]]]

if __name__ == '__main__':
    demo_stack()

