# coding=utf-8
# date: 2018-8-23,22:02:46
# name: smz

import numpy as np
import torch as th
"""
result = torch.cat((tensor_a, tensor_b), dim=1)
将两个tensor对应的轴1内元素合并起来
"""
def demo_cat():
    tensor_a = th.from_numpy(np.array([[1, 2], [3, 4]]))
    tensor_b = th.from_numpy(np.array([[5, 6], [7, 8]]))
    tensor_c = th.cat((tensor_a, tensor_b), dim=1)
    tensor_d = th.cat((tensor_a, tensor_b), dim=0)
    print 'cat((tensor_a, tensor_b), dim=1):', tensor_c     # [[1, 2, 5, 6], [3, 4, 7, 8]]
    print 'cat((tensor_a, tensor_b), dim=0):', tensor_d     # [[1, 2], [3, 4], [5, 6], [7, 8]]

if __name__ == '__main__':
    demo_cat()