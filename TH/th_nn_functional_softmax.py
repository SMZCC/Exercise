# coding=utf-8
# date: 2018-8-23,21:27:18
# name: smz

import numpy as np
import torch as th
import torch.nn.functional as F
"""
import torch.nn.functional as F
result = F.softmax(input)

注意：
  1.传入的数值必须是浮点型的
  2.与torch.nn.Softmax()不同,这个softmax并不要求必须是2D,2D以内都是计算的最后一个轴内的softmax,但是3D及以上就比较难理解了,似乎是以最后两个轴为一个元素单位进行softmax计算
  3.在3.0及以上版本为 result = F.softmax(input, dim=None) 可以设置在哪个轴内进行softmax计算
"""

def demo_softmax():
    tensors = th.from_numpy(np.array([1, 2, 3])).type(th.FloatTensor)
    tensors_softmax = F.softmax(tensors)
    print 'tensors_softmax:', tensors_softmax

    tensors_a = th.from_numpy(np.array([[1, 2, 3], [3, 3, 9]])).type(th.FloatTensor)
    tensors_a_softmax = F.softmax(tensors_a)
    print 'tensors_a_softmax:', tensors_a_softmax

    tensors_b = th.from_numpy(np.array([[[1, 2, 3], [3, 3, 3]], [[4, 4, 5], [5, 4, 6]]])).type(th.FloatTensor)  # (2, 2, 3)
    tensors_b_softmax = F.softmax(tensors_b)
    print 'tensors_b_softmax:', tensors_b_softmax

    tensors_c = th.from_numpy(np.array([[[[1], [2], [3]], [[3], [3], [3]]], [[[4], [4], [5]], [[5], [4], [6]]]])).type(th.FloatTensor)  # (2, 2, 3, 1)
               # [[1], [2], [3]] 对应 [[3], [3], [3]] 计算softmax
               # [[4], [4], [5]] 对应 [[5], [4], [6]] 计算softmax
    tensors_c_softmax = F.softmax(tensors_c)
    print 'tensors_c_softmax:', tensors_c_softmax


if __name__ == '__main__':
    demo_softmax()