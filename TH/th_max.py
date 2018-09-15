# coding=utf-8
# date: 2018-8-30,14:03:18
# name: smz

import torch as th
"""
value, index = torch.max(tensor_a, dim)
返回tensor的dim轴内的最大值以及其对应的索引
说明：
    1. 不提供dim参数的话,就是返回tensor_a中所有元素的最大值,也不会返回该值的索引
    2. 提供dim参数的话,就是返回该dim内,元素的最大值,注意是该dim内元素的最大值,返回的索引,也是在该dim内,元素的索引
       有两种情况(下面那个最外面的中括号为该dim)：
         1.该dim内的元素都是最小单元元素,如[1, 2, 3, 4],这种情况,好理解,返回4,索引为3
         2.该dim内的元素是带轴的元素,如[[2, 3], [1, 4]],该dim内的元素为[2, 3]和[1, 4],此时比较大小就是每个元素依次取出一个最小单元元素进行比较,
           然后返回该元素在dim内元素(该元素是轴包裹元素)的索引,这个例子的结果就是 最大值是2和4,索引分别是0和1
         3.最后一单轴包裹元素中最小单元元素的个数就是考虑单元中元素的个数
"""

def demo_max():
    tensor_a = th.Tensor([[2, 3, 5], [1, 4, 6]])
    tensor_b = th.Tensor([[[1, 2, 4], [3, 6, 5]], [[9, 8, 7], [10, 11, 12]], [[13, 15, 16], [14, 17, 18]]]) # (3, 2, 3)
    tensor_c = th.Tensor([[1, 2], [3, 4]])
    print 'torch.max(tensor_a):', th.max(tensor_a)
    print 'torch.max(tensor_a, 1):', th.max(tensor_a, 1)
    print 'torch.max(tensor_a, 0):', th.max(tensor_a, 0)
    print 'torch.max(tensor_b, 0):', th.max(tensor_b, 0)
    print 'torch.max(tensor_c, 0):', th.max(tensor_c, 0)


if __name__ == '__main__':
    demo_max()