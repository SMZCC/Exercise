# coding=utf-8
# date: 2018-8-22,17:09:27
# name: smz

import numpy as np
import torch as th
from torch.autograd import Variable
from torch.autograd import Function
from torch.autograd import gradcheck
"""
通过继承Function类可以自定义能够自动微分的算子
实现该算子的必要步骤：
    实现forward函数
    实现backward函数
使用该算子的步骤：
 0.3及以上版本
    op =  xx.apply()   # apply()中可以传入输入值,也可以在重命名后的函数中传入输入值
    result = op()
 0.2及以下版本
    op = xx()      # 生成实例
    result = op()  # 调用
   
最后可以使用grad_check()来检查梯度是否计算正确,gradcheck通过数值逼近来计算梯度f(x+diata)-f(x),可能具有一定的误差,通过控制eps的大小可以控制容忍的误差.
 0.3及以上版本
    gradcheck(xx.apply(), (input,), 1e6)
 0.2及以下版本
    gradcheck(xx(), (input, ), 1e6)
 
"""

class ReLU(Function):

    # 0.3及以上版本
    @staticmethod
    def forward(ctx, input):
        ctx.save_for_backward(input)           # 保存反向传播中需要使用的值input
        return input.clamp(min=0)              # relu公式

    @staticmethod
    def backward(ctx, grad_output):
        input = ctx.saved_tensors
        grad_input = grad_output.clone()    # 一般情况下relu(x)对x的导数为1,貌似grade_output默认是1
        grad_input[input < 0] = 0           # 若relu(x)中x的值小于0的话,relu(x)=0,导数为0
        return grad_input



class MyReLU(Function):
    """
    We can implement our own custom autograd Functions by subclassing
    torch.autograd.Function and implementing the forward and backward passes
    which operate on Tensors.
    """
    # 0.2及以下版本
    def forward(self, input):
        """
        In the forward pass we receive a Tensor containing the input and return a
        Tensor containing the output. You can cache arbitrary Tensors for use in the
        backward pass using the save_for_backward method.
        """
        self.save_for_backward(input)
        return input.clamp(min=0)

    def backward(self, grad_output):
        """
        In the backward pass we receive a Tensor containing the gradient of the loss
        with respect to the output, and we need to compute the gradient of the loss
        with respect to the input.
        """
        input, = self.saved_tensors
        grad_input = grad_output.clone()
        grad_input[input < 0] = 0
        return grad_input


if __name__ == '__main__':

    var_x = Variable(th.from_numpy(np.array([4])).type(th.FloatTensor), requires_grad=True)
    print th.__version__  # 0.2
    # relu = ReLU()     # 出错,无法调用,会报参数个数错误
    relu = MyReLU()     # 0.2版本调用
    loss = relu(var_x)

    loss.backward()

    print 'loss:', loss
    print 'var_x.data:', var_x.data
    print 'var_x.grad:', var_x.grad.data
    print 'gradcheck:', gradcheck(MyReLU(), (var_x,), 1e-2)


# 0.2.0_3
# loss: Variable containing:
#   4
# [torch.FloatTensor of size 1]
#
# var_x.data:
#   4
# [torch.FloatTensor of size 1]
#
# var_x.grad:
#   1
# [torch.FloatTensor of size 1]
#
# gradecheck: True

