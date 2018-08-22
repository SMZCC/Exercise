# coding=utf-8
# date: 2018-8-22,17:09:27
# name: smz

import numpy as np
import torch as th
from torch.autograd import Variable
from torch.autograd import Function
"""
通过继承Function类可以自定义能够自动微分的算子
必要步骤：
    实现forward函数
    实现backward函数
"""

class Relu(Function):
    def forward(*args, **kwargs):
        pass

    def backward(*grad_outputs):
        pass