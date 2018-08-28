# coding=utf-8
# date: 2018-8-27,23:14:55
# name: smz

import torch as th
"""
变量的一种,可被视作Module的变量,是torch.autograd.Variable的子类
在和Module类一起使用会有特殊的功能
    1. 当它们被分配为Module的属性时,会被自动添加到Module的parameters中
    2. 而分配Variable作为Module的属性则没有这样的效果, 因为, 当想要缓存一些临时状态时,比如模型中,RNN最后隐藏层的状态,
       如果没有Parameter这个类的话,这些临时的值也会被注册到parameters中
    3. Parameter不是易变的(volatile),并且默认是需要计算梯度值的

"""