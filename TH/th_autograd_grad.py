# coding=utf-8
# date: 2018-9-12,19:10:42
# name: smz

import torch as th
from torch.autograd import Variable
"""
grads = torch.autograd.grad(outputs, inputs, grad_outputs=None, 
                retain_graph=None, create_graph=None, only_inputs=True))
返回outputs关于inputs的梯度值,该梯度值不会被记录到<Variable>的grad属性中,只会返回为grads
返回值grads是个<Tuple>
参数：
    outputs: 由inputs通过图的前向计算得到的结果,若该结果是个中间结果,那么该结果还有对应的梯度值grad_ouputs
    inputs: 叶子节点,即,变量
    grad_outputs: 与outputs对应的梯度,若outputs是最终的loss值,那么其实该值相当于是1
    retain_graph: bool,一张图中经过公共路径之后,损失函数开始了不同路径的演化,为了使得每个损失函数不会因为图的释放而不能求导而存在
    create_graph: bool,为了计算图中变量的高阶梯度时,由于要使用梯度来对叶子变量再次求导,此时相当于在新图上进行了求导,故而需要该参数保证
                  新图的存在
"""


def demo_one():
    """.backward()的基本用法
    公式计算: (x**2)**2 ==> out_1 ** 2 ==> out_2
    d(out_2)/d(out_1) = 2out_1
    d(out_1)/d(x) = 2x
    d(out_2)/d(x) = d(out_2)/d(out_1)*d(out_1)/d(x) = 2out_1 * 2x = 2x**2 * 2x ,当x=2时,结果为:2*4 * 2*2=32
    """
    var_a = Variable(th.Tensor([2]), requires_grad=True)
    out_1 = var_a.pow(2)
    out_2 = out_1.pow(2)

    out_2.backward()    # 注意:若是同样的变量,再次构图求梯度的话,需要在.backward()之前将各个变量的grad置为0,
                        # 否则会在grad中出现梯度叠加的副作用
    print "out_2.grad:", out_2.grad    # None  在这里,我曾经萌生了使用requires_grad的想法来查看中间变量的梯度值,
                                       # 但是这想法显然是有所保留的,因为这里仅仅是一遍图的反推,而且并不需要应用梯度结果,
                                       # 这种方法倒是可以临时查看一下中间量的梯度值,由于在真正的模型中,这些<Variable>
                                       # 都是会利用.grad属性值来进行值的更新的,而且在使用Sequential()的时候,中间的变量
                                       # 是得不到的,除非分开来写,这种方法,官方也没有提倡,可能甚至都没有人想过,使用下面的
                                       # demo_two测试以下吧,结论：不可行,具体原因查看demo_two
    print 'out_1.grad:', out_1.grad    # None
    print 'var_a.grad:', var_a.grad    # 32  与上面推导一致


def demo_two():
    """同样计算上式的梯度,此次使用requires_grad=True来查看中间变量的梯度值
    公式计算: (x**2)**2 ==> out_1 ** 2 ==> out_2
    d(out_2)/d(out_1) = 2out_1
    d(out_1)/d(x) = 2x
    d(out_2)/d(x) = d(out_2)/d(out_1)*d(out_1)/d(x) = 2out_1 * 2x = 2x**2 * 2x ,
    当x=2时,
        d(out_2)/d(out_1)结果为:2*4=8  <==> out_1.grad
        d(out_1)/d(x)结果为: 2*2=4     没有量来保存这个值
        d(out_2)/d(x)结果为: 32

    尝试之后的结论: 中间节点的requires_grad属性不可更改,只能更改叶子节点的requires_grad属性,故而该demo报错
    """
    var_a = Variable(th.Tensor([2]), requires_grad=True)
    out_1 = var_a.pow(2)
    out_1.requires_grad = True
    out_2 = out_1.pow(2)
    out_2.requires_grad = True

    out_2.backward()

    print 'out_2.grad:', out_2.grad
    print 'out_1.grad:', out_1.grad
    print 'var_a.grad:', var_a.grad


def demo_three():
    var_a = Variable(th.Tensor([2]), requires_grad=True)
    out_1 = var_a.pow(2)
    out_2 = out_1.pow(2)

    grads = th.autograd.grad(out_2, var_a)

    print 'grads:', grads  # 理论:32,已证实
    print 'var_a.grad:', var_a.grad   # 理论: None,已证实


def demo_four():
    var_a = Variable(th.Tensor([2]), requires_grad=True)
    out_1 = var_a.pow(2)
    out_2 = out_1.pow(2)

    out_3 = 2 * var_a
    out_4 = out_2 * 2   # out_4 = 2((var_a ** 2)**2),grad=2*32=64
    # 注意out_3与out_2,out_4没有公共的图路径
    # out_4与out_2有公共的图路径
    # out_2 关于var_a的梯度

    # grad_out_2 = th.autograd.grad(out_2, var_a)  # 这样写,有一个错误
                                                 # out_2的梯度计算之后图被释放,out_4的梯度计算必然出错
                                                 # 注意: torch.autograd.grad不会影响<Variable>.grad属性,
                                                 # 故而不存在梯度叠加的情况,权重利用梯度的更新需要手动实现
    # 正确写法
    grad_out_2 = th.autograd.grad(out_2, var_a, retain_graph=True)
    grad_out_3 = th.autograd.grad(out_3, var_a)
    grad_out_4 = th.autograd.grad(out_4, var_a)

    print 'd(out_2)/d(var_a):', grad_out_2  # 理论值32,已验证
    print 'd(out_3)/d(var_a):', grad_out_3  # 理论值2,已验证
    print 'd(out_4)/d(var_a):', grad_out_4  # 理论值64,已验证


def demo_five():
    """依旧是上式,计算var_a的二阶导数
    out_1 = var_a ** 2
    out_2 = out_1 ** 2
    d(out_2)/d(out_1) = 2out_1
    d(out_1)/d(var_a) = 2var_a
    d(out_2)/d(var_a) = 2out_1 * 2var_a = 2var_a**2 * 2var_a = 4var_a**3

    # 求out_2对var_a的二阶导
    d(out_2)/d(var_a^2) = d(4var_a**3) = 12var_a**2 ,当var_a=2时,结果为:48
    """
    var_a = Variable(th.Tensor([2]), requires_grad=True)
    out_1 = var_a.pow(2)
    out_2 = out_1.pow(2)

    # grad_out_2_1 = th.autograd.grad(out_2, var_a)      # 此处出错,因为没有grad_out_2_1的图
    # 正确的写法
    grad_out_2_1 = th.autograd.grad(out_2, var_a, create_graph=True)
    grad_out_2_2 = th.autograd.grad(grad_out_2_1[0], var_a)  # 理论48,已验证

    print 'd(out_2)/d(var_a^2):', grad_out_2_2


def demo_six():
    """这个是为了解惑文章Meta-Tracker: Fast and Robust Online Adaptation for Visual Object Trackers中
    在每一个循环中,明明都重新构图了,为何还要使用create_graph=True,或者,当设置了create_graph=True之后有何异同,
    公式依旧使用上式,d(out_2)/d(var_a) = 4var_a**3
    结论： 在其实现中,该参数无论为True还是为False都不影响结果,也就是说,该作者这个参数的设置根本没用
    """

    var_as = [Variable(th.Tensor([2]), requires_grad=True),
              Variable(th.Tensor([3]), requires_grad=True),
              Variable(th.Tensor([4]), requires_grad=True)]
    # 三次循环到话,梯度应该分别是: 32, 108, 256

    # 第一个试验: 不使用create_graph=True
    for idx, var_a in enumerate(var_as):
        out_1 = var_a.pow(2)
        out_2 = out_1.pow(2)
        grads = th.autograd.grad(out_2, var_a)
        print 'example_1_grads_%d:'%(idx+1), grads    # 已验证,32, 108, 256

    for idx, var_a in enumerate(var_as):
        out_1 = var_a.pow(2)
        out_2 = out_1.pow(2)
        grads = th.autograd.grad(out_2, var_a, create_graph=True)
        print 'example_2_grads_%d:'%(idx+1), grads   # 同样验证,32, 108, 256


if __name__ == '__main__':
    demo_one()
    # demo_two()   # 不可行,不必运行了,结论查看demo_two()
    # demo_three()
    # demo_four()
    # demo_five()
    # demo_six()