# coding=utf-8
# date: 2018-8-24,13:23:57
# name: smz

import torch as th

"""
obj = torch.load(file_path)
将保存的对象读取出来,读取出来的结果同保存前对象的状态一致
"""
def demo_load():
    obj = th.load('./data/weights_2.pth')
    print 'loaded obj:', obj

if __name__ == '__main__':
    demo_load()