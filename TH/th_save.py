# coding=utf-8
# date: 2018-8-23,22:48:38
# name: smz

import numpy as np
import torch as th
"""
torch.save(obj, file_path)
将对象obj保存在文件file_path中
注意：
  保存的是什么,使用torch.load(file_path)读出来的就是什么,实际上就是利用了pickle序列化的存储
"""
def demo_save():
    weights = th.from_numpy(np.array([[1, 2], [3, 4]]))
    th.save({'weights':weights}, './data/weights_1.pth')
    th.save(weights, './data/weights_2.pth')

if __name__ == '__main__':
    demo_save()
    weights_1 = th.load('./data/weights_1.pth')
    weights_2 = th.load('./data/weights_2.pth')
    print 'weights_1 loaded data:', weights_1   # {'weights': [[1, 2], [3, 4]]}  保存的dict
    print 'weights_2 loaded data:', weights_2   # [[1, 2], [3, 4]] 保存的tensor