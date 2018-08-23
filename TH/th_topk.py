# coding=utf-8
# date: 2018-8-23,22:20:57
# name: smz

import numpy as np
import torch as th
"""
value, index = torch.topk(input, k, dim=None, largest=True)
返回各个dim轴内(索引为dim的轴)前K个最值以及其对应的索引(在dim轴内的索引)
largest=True,返回最大值;largest=False, 返回最小值
"""
def demo_topk():
    tensor_a = th.from_numpy(np.array([i for i in range(10)]))   # 0, 1, ..., 9
    tensor_b = th.topk(tensor_a, 2)
    print 'tensor_a:', tensor_a
    print 'top 2 largest:', tensor_b

    tensor_c = th.from_numpy(np.array([[1, 2], [3, 4]]))
    tensor_d = th.topk(tensor_c, 1)
    print 'top 1 larges in 2D array:', tensor_d

if __name__ == '__main__':
    demo_topk()