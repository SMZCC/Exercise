# coding=utf-8
# date: 2018-8-30,13:46:45
# name: smz
import torch as th
"""
index_array = torch.nonzero(input)
返回input中非0元素的索引
说明：
    index_array: zxN的array,其中,z表示input中非0元素的个数,N表示input的维度总数
                 => 一行是一个非0元素的索引,因为对于一个N维的array来说,每一个元素的索引均是N维的(索引每个最小单元都需要N个坐标)
"""
def demo_nonzero():
    tensor_a = th.Tensor([[1, 2], [0, 3]])
    print 'th.nonezero(tensor_a):', th.nonzero(tensor_a)

  # 0, 0 这是1的索引
  # 0, 1 这是2的索引
  # 1, 1 这是3的索引


if __name__ == '__main__':
    demo_nonzero()

