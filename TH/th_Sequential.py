# coding=utf-8
# date: 2018-8-26,15:32:15
# name: smz

import torch as th
import numpy as np
from collections import OrderedDict
"""
model = torch.nn.Sequential()
用于装载模块(Module)的容器 => 可嵌套
输入参数:
    层类对象或者是OrderedDict类对象
    1.若是层类对象,在注册Module的时候,按层出现的序数作为名字
    2.若是OrderedDict()对象,按照关键字作为名字
所有方法:
    __init__(*args)         调用<Module>.add_module()方法,注册当前<Sequential>中的<Module>至当前<Module>的_modules中
    __getitem__(self, idx)  可通过添加的module的索引来获得对应的module
    __len__(self)           可通过len(<Module>)来获得<Module>的长度
    forward(input)          实际上是实现的__call__(input) 
注：
    以上方法全部不需要主动调用   
"""
class model(th.nn.Module):
    def __init__(self):
        super(model, self).__init__()
        self.layers = th.nn.Sequential(
            # layers 这个Sequential的_modules中包含两个<Module> 一个是'conv1',另一个是'conv2'
            OrderedDict([
            ('conv1', th.nn.Sequential(th.nn.Conv2d(3, 64, 3), th.nn.Dropout())),
                # conv1 这个<Modules>的_modules中包含Conv2d和Dropout两个<Module>,名字分别为索引'0'和'1'
            ('conv2', th.nn.Sequential(th.nn.Conv2d(64, 128, 3), th.nn.Dropout()))
        ]))  # 结构: layers->两个Sequential->各自两个网络层
    def forward(self, input):
        out = self.layers(input)
# 以下是调试中时model_one对象中的值,括号中是其对应的名字,之所以有layers那是因为该model_one中有个属性名为layers的属性
# model (
#   (layers): Sequential (
#     (conv1): Sequential (
#       (0): Conv2d(3, 64, kernel_size=(3, 3), stride=(1, 1))
#       (1): Dropout (p = 0.5)
#     )
#     (conv2): Sequential (
#       (0): Conv2d(64, 128, kernel_size=(3, 3), stride=(1, 1))
#       (1): Dropout (p = 0.5)
#     )
#   )
# )

if __name__ == '__main__':
    model_one = model()
    print 'check ..'