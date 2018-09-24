# coding=utf-8
# date: 2018-8-27,23:14:55
# name: smz

import torch as th
from torch.nn import Parameter

"""
变量的一种,可被视作Module的变量,是torch.autograd.Variable的子类
在和Module类一起使用会有特殊的功能
    1. 当它们被分配为Module的属性时,会被自动添加到Module的parameters中
    2. 而分配Variable作为Module的属性则没有这样的效果, 因为, 当想要缓存一些临时状态时,比如模型中,RNN最后隐藏层的状态,
       如果没有Parameter这个类的话,这些临时的值也会被注册到parameters中
    3. Parameter不是易变的(volatile),并且默认是需要计算梯度值的
    
# definition
class Parameter(Variable):
    def __new__(cls, data=None, requires_grad=True):
        return super(Parameter, cls).__new__(cls, data, requires_grad=requires_grad)

    def __repr__(self):
        return 'Parameter containing:' + self.data.__repr__()
        
注意:
    1.该类没有.copy_()方法,因为其是继承的<Variable>,而<Variable>没有.copy_()方法
    2.可以使用赋值符号=来改变值

"""

def demo_one():
    param_1 = Parameter(th.FloatTensor([1, 2]))
    # param_1.copy_(th.FloatTensor([3, 4]))    # 报错
    print 'param1.copy_(th.FloatTensor([3, 4]):', param_1


if __name__ == '__main__':
    demo_one()