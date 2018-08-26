# coding=utf-8
# date: 2018-8-26,15:36:54
# name: smz

import torch as th
import numpy as np
from collections import OrderedDict
"""
class SomeClass(torch.nn.Module):
    def __init__(self):
        super(SomeClass, self).__init__()
所有的Module的基类,可用于管理所有的module对象
基本属性:
    ._modules           OrderedDict 用于保存当前module下包含哪些module,一级
    ._parameters        OrderedDict 用于保存当前module下包含哪些parameter,初始为空
    ._buffers           OrderedDict 用于保存当前module下的常数
    .training           True, 表示当前module是否是训练状态
    
基本方法:
    .children()         返回当前<Module>的孩子(<Module>),一级,实际是调用.named_children()
    .name_children()    返回当前<Module>的 名字,孩子 对, 一级
    .modules()          返回当前<Module>的所有<Module>, 实际是调用.named_module()
    .named_modules()    返回当前<Module>的所有 name, <Module> 对
    .train()            将当前<Module>设置为训练模式,当有Dropout or BatchNorm层时,是必须的
    .eval()             将当前<Module>设置为测试模式,当有Dropout or BatchNorm层时,是必须的
    .zero_grad()        将当前<Module>的所有变量的梯度全部设置为0,在进行梯度计算前需要执行,当前优化器也有类似的功能
"""
class model(th.nn.Module):
    def __init__(self):
        super(model, self).__init__()
        self.layers = th.nn.Sequential(
            # layers 这个Sequential的_modules中包含两个<Module> 一个是'conv1',另一个是'conv2'
            OrderedDict([
            ('conv1', th.nn.Sequential(th.nn.Conv2d(3, 96, 2), th.nn.Dropout())),
                # conv1 这个<Modules>的_modules中包含Conv2d和Dropout两个<Module>,名字分别为索引'0'和'1'
            ('conv2', th.nn.Sequential(th.nn.Conv2d(96, 128, 2), th.nn.Dropout()))
        ]))  # 结构: layers->两个Sequential->各自两个网络层
    def forward(self, input):
        out = self.layers(input)
# 以下是调试中时model_one对象中所包含的对象,括号中是其对应的名字,之所以有layers那是因为该model_one中有个属性名为layers的属性
# model (
#   (layers): Sequential (
#     (conv1): Sequential (
#       (0): Conv2d(3, 96, kernel_size=(2, 2), stride=(1, 1))
#       (1): Dropout (p = 0.5)
#     )
#     (conv2): Sequential (
#       (0): Conv2d(96, 128, kernel_size=(2, 2), stride=(1, 1))
#       (1): Dropout (p = 0.5)
#     )
#   )
# )

if __name__ == '__main__':
    model_one = model()