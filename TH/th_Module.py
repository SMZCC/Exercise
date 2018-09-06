# coding=utf-8
# date: 2018-8-26,15:36:54
# name: smz

import torch as th
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
    .name_children()    返回当前<Module>的 名字,孩子 对, 所有, 名字的连接都是用的.,如:layers.conv1.0.weight
    .modules()          返回当前<Module>的所有<Module>, 包含当前<Module>,当前<Module>的名字为变量名,实际是调用.named_module()
    .named_modules()    返回当前<Module>的所有 name, <Module> 对
                          若网络结构为:
                            self.layers = th.nn.Sequential(
                            # layers 这个Sequential的_modules中包含两个<Module> 一个是'conv1',另一个是'conv2'
                            OrderedDict([
                              ('conv1', th.nn.Sequential(th.nn.Conv2d(3, 96, 2), th.nn.Dropout())),
                                # conv1 这个<Modules>的_modules中包含Conv2d和Dropout两个<Module>,名字分别为索引'0'和'1'
                              ('conv2', th.nn.Sequential(th.nn.Conv2d(96, 128, 2), th.nn.Dropout()))
                            ]))  # 结构: layers->两个Sequential->各自两个网络层
                            
                            layers--|'' Sequential  # 这里这个''是赋值给layers的Sequential的名字
                                     --|'conv1'  Sequential
                                        --|'conv1.0' Conv2d
                                        --|'conv1.1' Dropout
                                     --|'conv2'  Sequential
                                        --|'conv2.0' Conv2d
                                        --|'conv2.1' Dropout
                            => layers.named_modules的结果为:
                            ''      Sequential  # 这是layers对应的最外层的Sequential
                            'conv1' Sequential
                            'conv1.0' Conv2d
                            'conv1.1' Dropout
                            'conv2' Sequential
                            'conv2.0' Conv2d
                            'conv2.1' Dropout
    .add_module()       将当前<Module>的<Module>都保存到_modules中(如出现在torch.nn.Sequential的构造函数中的<Module>),
                        或者将某个<Module>添加到当前的<Module>中,
                            如：<Module> = nn.Sequential()是个空的<Module>,另外实现了<Module>_new = torch.nn.ReLU(),
                               可以使用<Module>.add_module(name, <Module>_new)来将<Module>_new添加到<Module>中 
    .state_dict()       返回当前<Module>的各种参数设置,以字典的形式返回,可用torch.save()保存
    .load_state_dict()  给当前<Module>加载已经训练的参数,可先用torch.load()加载保存的字典,然后再使用<Module>.load_state_dict(loaded_dict)
    .train()            将当前<Module>设置为训练模式,当有Dropout or BatchNorm层时,是必须的
    .eval()             将当前<Module>设置为测试模式,当有Dropout or BatchNorm层时,是必须的
    .zero_grad()        将当前<Module>的所有变量的梯度全部设置为0,在进行梯度计算前需要执行,当前优化器也有类似的功能
    .cuda()             将当前<Module>放到gpu中
    .cpu()              将当前<Module>放到cpu中,在保存模型的时候会用到,因为我们在加载已经训练的模型的时候,往往多是在cpu中加载的
    
    
    # 以下方法基本是框架本身调用,用户调用频率不高
    .register_parameters() 将当前<Module>的变量都保存到_parameters中
    .register_buffers()    将当前<Module>的常量都保存到_buffers中
    
注:
    1.没能搞明白.modules()中是如何添加当前<Module>的名字的
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
# 以下是调试中时model_one对象中所包含的对象,括号中是其对应的名字,之所以有layers那是因为该model_one中有个属性名为layers的属性,这个暂时为搞明白为何会有layers这个名字
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

def show_methods(model):
    print 'model_one.children():', model.children()
    print 'model_one.named_children():', model.named_children()
    print 'model_one.parameters():', model.parameters()
    print 'model_one.named_parameters():', model.named_parameters()

    print 'model_one.children():'
    for module in model.children():
        print module
    print 'model_one.named_children():'
    for name, module in model.named_children():
        print name, module
    print 'model_one.parameters():'
    for param in model.parameters():
        print param
    print 'model_one.named_parameters():'
    for name, param in model.named_parameters():
        print name, param

    print 'model_one._parameters:', model._parameters
    print 'model_one._modules:', model._modules


def check_parameters(model_one):
    for module_name, module in model_one.layers.named_modules():
        if module_name.startswith('conv1'):
            print module_name, module.named_parameters()

    print '*' * 50

    print model_one.layers[0].named_parameters()


if __name__ == '__main__':
    model_one = model()
    for name, module in model_one.named_modules():
        print name, module
        print '*' * 100
    # check_parameters(model_one)
    # show_methods(model_one)

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
# ****************************************************************************************************
# layers Sequential (
#   (conv1): Sequential (
#     (0): Conv2d(3, 96, kernel_size=(2, 2), stride=(1, 1))
#     (1): Dropout (p = 0.5)
#   )
#   (conv2): Sequential (
#     (0): Conv2d(96, 128, kernel_size=(2, 2), stride=(1, 1))
#     (1): Dropout (p = 0.5)
#   )
# )
# ****************************************************************************************************
# layers.conv1 Sequential (
#   (0): Conv2d(3, 96, kernel_size=(2, 2), stride=(1, 1))
#   (1): Dropout (p = 0.5)
# )
# ****************************************************************************************************
# layers.conv1.0 Conv2d(3, 96, kernel_size=(2, 2), stride=(1, 1))
# ****************************************************************************************************
# layers.conv1.1 Dropout (p = 0.5)
# ****************************************************************************************************
# layers.conv2 Sequential (
#   (0): Conv2d(96, 128, kernel_size=(2, 2), stride=(1, 1))
#   (1): Dropout (p = 0.5)
# )
# ****************************************************************************************************
# layers.conv2.0 Conv2d(96, 128, kernel_size=(2, 2), stride=(1, 1))
# ****************************************************************************************************
# layers.conv2.1 Dropout (p = 0.5)
# ****************************************************************************************************
#     for name, module in model_one.named_children():    # 只有一个module,即,最外层的那个Sequence
#         print name, module
#         print '*' * 100
#
# layers Sequential (
#   (conv1): Sequential (
#     (0): Conv2d(3, 96, kernel_size=(2, 2), stride=(1, 1))
#     (1): Dropout (p = 0.5)
#   )
#   (conv2): Sequential (
#     (0): Conv2d(96, 128, kernel_size=(2, 2), stride=(1, 1))
#     (1): Dropout (p = 0.5)
#   )
# )
# ****************************************************************************************************

# 将源码中以下部分注释掉,以下语句没有任何输出
# if self not in memo:
#     memo.add(self)
#     yield prefix, self

# for name, module in model_one.named_modules():   无任何输出
#     print name, module
#     print '*' * 100