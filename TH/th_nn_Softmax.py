# coding=utf-8
# date: 2018-8-23,21:16:59
# name: smz

import numpy as np
import torch as th
"""
softmax = torch.nn.Softmax(2D Tensor)
实际上是调用的F.softmax() <= import torch.nn.functional as F   
注意:
  1. 仅仅接受2D的Tensor,并且仅在第二个轴(索引为1)内进行softmax计算 => [[1, 2]] --> [[exp(1)/(exp(1)+exp(2)), exp(2)/(exp(1)+exp(2))]]
     [[1, 2], [3, 4]] --> [[exp(1)/(exp(1)+exp(2)), exp(2)/(exp(1)+exp(2))], [exp(3)/(exp(3)+exp(4)), exp(4)/(exp(3)+exp(4))]]
  2. 输入的数据必须是浮点型的数据
"""

def demo_softmax():
    vs = th.from_numpy(np.array([[5, 10]])).type(th.FloatTensor)
    softmax = th.nn.Softmax()
    vs_softmax = softmax(vs)
    print 'vs_softmax:', vs_softmax

    vs_2 = th.from_numpy(np.array([[1, 2], [3, 4]])).type(th.FloatTensor)
    vs_2_softmax = softmax(vs_2)
    print 'vs_2_sotfmax:', vs_2_softmax


if __name__ == '__main__':
    demo_softmax()

