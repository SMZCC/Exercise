# coding=utf-8
# date: 2018-8-23,20:15:44
# name: smz

import torch as th
import numpy as np
import torch.nn.functional as F
"""
import torch.nn.functional as F
F.log_softmax([x1, x2]), 先对x1, x2进行softmax([x1, x2])计算,再分别对其进行log(x)计算
注意：
  x1, x2必须是TH浮点型Tensor
"""

def demo_log_softmax():
    # np 实现作为对比
    vars_ = np.array([5, 10])
    e_var_1 = np.exp(vars_[0])
    e_var_2 = np.exp(vars_[1])
    total_sum = e_var_1 + e_var_2
    softmax_vars_ = np.array([np.true_divide(e_var_1, total_sum), np.true_divide(e_var_2, total_sum)])
    np_log_softmax = np.array([np.log(softmax_vars_[0]), np.log(softmax_vars_[1])])

    print 'log_softmax calculated by np:\n', np_log_softmax

    # th实现
    print 'log_softmax calculated by th:\n', F.log_softmax(th.from_numpy(vars_).type(th.FloatTensor))  # 一开始这里为torch.LongTensor报错


# log_softmax calculated by np:
#               [-5.00671535 - 0.00671535]
# log_softmax calculated by th:
#   Variable containing:
#           -5.0067
#           -0.0067
# [torch.FloatTensor of size 2]
# 两者结果一致,除了保留的精度不同


if __name__ == '__main__':
    demo_log_softmax()
