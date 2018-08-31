# coding=utf-8
# date: 2018-8-22,16:29:47
# name: smz

import torch as th
import numpy as np

"""
tensor是torch的基础类
tensor = torch.from_numpy()
tensor = torch.Tensor(3, 5)
基本方法有：
    .type()   返回值为设定的数据类型
    .float()  将当前<Tensor>转换成FloatTensor
    .mm(tensor_b) 与tensor_b进行正常的矩阵乘积,哈达玛积直接使用*即可,tensor_a * tensor_b
    .clamp(min, max) 将tensor的值限定在[min, max],可以只有一个参数[min, +inf)或(-inf, max]
    .t()  转置
    .clone() 拷贝
    .pow()  只有FloatTensor才有该方法,LongTensor没有该方法,而且,<LongTensor>也没有.square()方法
    .sum()
    .mean(dim=1)  当前tensor必须是FloatTensor类型,计算dim轴内元素的均值,计算时是一个元素依次取一个值计算一个均值,直至所有的元素取尽
                  如: [[1, 2], [3, 4]],dim=0, 0轴内有两个元素[1, 2], [3, 4], 依次取一个1+3=>2, 2+4=>3 ==>[2, 3]
    .zero_() 将当前tensor内的所有元素全部变为0,在反向传播计算梯度前,需要将各变量对应的梯度值变为0,防止梯度累加
    .vew()   相当于reshape,但是条件更苛刻一点:tensor在内存中必须是连续的一块,有时需要先执行.contiguous()
    .vew_as()相当于reshape,与上面的.view()的区别是.view()是直接传入shape,但是.view_as()是传入一个tensor,然后其自动获取shape,再reshape
    .cuda()  将返回值放到gpu中,而tensor本身还是在cpu
    .cpu()
    .size()  相当于ndarray.shape
    .permute(dim1, dim2, dim3, ...) 将当前<Tensor>的轴重新排序
    .transpose(input, dim1, dim2, out) 也是交换轴,然而只能交换两个轴,不如.permute可以随便几个轴
    .new()   返回新的tensor,类型同当前调用的tensor,若不传入数值的话,就没有维度,可以传入的类型有[1, 2], (1, 2), ndarray()以及单纯的数字
             前面三个类型传入是什么,返回就是什么,只有最后传入单纯的数字的时候,.new(2, 3)是返回shape为(2, 3)的随机矩阵
    .index_select(int dim, torch.LongTensor index)  在dim维度维度上进行取值,取值的索引为后面的参数,后面的参数必须是LongTensor类型的
    .long()  将当前的tensor数据类型改变为LongTensor类型
    .numpy() 转为ndarray()类型
    .repeat(a, b) 0轴内的所有元素作为一个整体复制为a个,1轴里的所有元素作为一个整体复制为b个
    .numel() 返回当前<Tensor>中的最小元素单位有几个,如tensor_a = [[1, 2], [3, 4]],最小的元素单位为1或者2或者3或者4,共4个
    .unsqueeze(tensor, dim)  在特定位置插入一个轴,使其成为当前tensor的dim轴,如:tensor_a = [[1, 2], [3, 4]],.unsqueeze(tensor_a, dim=1)
                             原tensor_a有0轴和1轴,插入的轴要称为1轴,必须将轴套在0轴的元素外面 => [[[1, 2]], [[3, 4]]]
    
    .contiguous()  返回一个当前tensor的整块内存副本,原本的tensor在没有进行transpose,permute等操作时,是占用的一整块内存,
                   但是经这些操作后,便会分散,导致该tensor不能再使用.view()方法
        说明：<Tensor>.view()只能用在contiguous的variable上.如果在view之前用了transpose, permute等,需要用contiguous()来返回一个contiguous copy.
            一种可能的解释是：
                有些tensor并不是占用一整块内存,而是由不同的数据块组成,而tensor的view()操作依赖于内存是整块的,这时只需要执行contiguous()这个函数,
                把tensor变成在内存中连续分布的形式,判断是否contiguous用torch.Tensor.is_contiguous()函数.
                import torch
                x = torch.ones(10, 10)
                x.is_contiguous()  # True
                x.transpose(0, 1).is_contiguous()  # False
                x.transpose(0, 1).contiguous().is_contiguous()  # True
            在pytorch的最新版本0.4版本中,增加了torch.reshape(), 这与 numpy.reshape的功能类似,它大致相当于 tensor.contiguous().view()
    .is_contiguous() 判断当前tensor在内存中是否是占用一片连续内存空间(整块内存空间)
基本数据类型有：
    torch.FloatTensor
    torch.IntTensor
    ...
    以上每种类型都有对应的cuda类型
    torch.cuda.FloatTensor
    ...
对于显示效果说明：
    在控制台上显示的时候,一行是一个最基本的元素
    
对于tensor的取值说明:
    记住: 1.在shape中,前面一个轴的长度就是以后面的轴作为元素的个数
            如: matrix_a = [0, 1, 2] shape=(3,),就是有3个没有轴的数
            matrix_b = [[1, 2], [3, 4]] shape=(2, 2),第一个轴长为2,即表示,在第一个轴内,以第二个轴为单位元素的个数是2个
            所以matrix_b[:, 1],表示,第一个轴内的元素全部取,此时已经有2个元素了,再在这两个元素内各自取索引为1的元素,由于一共有两个轴,
            所以第二个轴内的元素是那些没有轴的数,而且仅取1个,故而总共由2个最小单位元素(以没有轴的元素作为最小单位)
            maxtrix_c = [[[1, 2], [3, 4]], [[5, 6], [7, 8]] shape=(2, 2, 2)
            matrix_c[:, 1]表示第一个轴内的元素全选,第二轴内取索引为1的元素,由于一共有3个轴,故而第二个轴内的元素是以第三个轴为单位的
            由于第三个轴每个轴的长度为2,而第一个轴长度为2,所以总共取了4个最小单位元素,取了2x1个第三个轴单位的元素,
          2.这种取值情况,重点要考虑最后一个轴是什么,并将该轴作为一行,即一个单元进行考虑,比如:
            matrix_a = th.Tensor([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
            matrix_a[:, :, 2],由于一共由3个轴,故而,在最后一个轴上取值,最后一个轴内的元素都变成了最小单元,这些最小单元被前一个轴接收,成为了
            最后一个轴,即,一行,一个考虑单元,比如,若三个轴表示的意义分别是batch,num_bbox, score,那么一个考虑单元就是num_bbox个score构成的一行

        
          3.对那个轴应用索引进行取值,求和,求均值,相当于将该轴消去了,只留下一个数,若是取值的话,要看该轴后面是否还有轴,若有轴的话,该轴的元素就是后面的轴构成的,
            否则的话,就是一个数,常见的就是matrix_a = [0, 1, 2]  一共只有一个轴,matrix_a[1],在0轴上取索引为1的元素,由于0轴后面没有轴了,所以就
            只有一个数,没有了轴;matrix_b = [[1, 2], [3, 4]], 一共有两个轴,matrix_b[1],只在第一个轴上取了值,所以第一个轴的元素都是以第二个轴
            为单位的元素,每个单位的元素的长度是第二个轴的长度
    
"""

def demo_tensor():
    tensor_a = th.from_numpy(np.array([[1, 2], [3, 4]]))
    tensor_b = th.from_numpy(np.array([[5, 6], [7, 8]]))
    tensor_c = tensor_a.mm(tensor_b)
    tensor_d = tensor_a * tensor_b   # 哈达玛积
    tensor_e = tensor_a.view((1, 4))
    tensor_f = tensor_a.cuda()
    tensor_g = tensor_a.new()
    tensor_h = tensor_a.new([[1, 2]])
    tensor_i = th.Tensor([[[1], [2], [3]], [[4], [5], [6]]])  # (2, 3, 1),th.Tensor中的Tensor是torch.FloatTensor的别名

    print 'tensor_a.mm(tensor_b):\n', tensor_c
    print 'tensor_a * tensor_b:\n', tensor_d
    print 'tensor_a.view((1, 4)):\n', tensor_e
    print 'tensor_a.cuda():', tensor_f  # gpu
    print 'tensor_a:', tensor_a        # cpu
    print 'tensor_a.size:', tensor_a.size()
    print 'tensor_a.new:', tensor_g
    print 'tensor_a.new([[1, 2]]):', tensor_h
    print 'tensor_a.new(1):', tensor_a.new(1)              # 随机一个数,范围不清楚
    print 'tensor_a.new((2, 3)):', tensor_a.new((2, 3))    # 就是[2, 3]
    print 'tensor_a.new(np.array([1, 2])):', tensor_a.new(np.array([1, 2])) # 就是[1, 2]
    print 'tensor_a.new(2, 3):', tensor_a.new(2, 3)        # 随机(2, 3)的数,范围不清楚
    print 'tensor_a.index_select(0, th.from_numpy(np.array([1])).long()):', tensor_a.index_select(0, th.from_numpy(np.array([1])).long())
    print 'tensor_a.numpy():\n', tensor_a.numpy()
    print 'tensor_a:', tensor_a
    print 'tensor_a.float().mean():', tensor_a.float().mean()
    print 'tensor_a.float().mean(dim=1):', tensor_a.float().mean(dim=1)
    print 'tensor_a.float().mean(dim=0):', tensor_a.float().mean(dim=0)

    print 'tensor = th.Tensor(3, 5):', th.Tensor(3, 5)   # 随机shape=(3, 5)的值

    tensor_float = th.FloatTensor(2)  # 两个随机值
    print 'torch.FloatTensor(2):', tensor_float
    print 'tensor_a.repeat(1, 2):', tensor_a.repeat(1, 2)
    print 'tensor_a.repeat(2, 2):', tensor_a.repeat(2, 2)
    print 'tensor_a.numel():', tensor_a.numel()
    print 'tensor_a.unsqueeze(2)', tensor_a.unsqueeze(2)
    print 'tensor_a.unsuqeeze(1)', tensor_a.unsqueeze(1)
    print 'tensor_a.permute(1, 0):', tensor_a.permute(1, 0)
    print 'tensor_i.permute(1, 0, 2):', tensor_i.permute(1, 0, 2)
    print 'tensor_a.pow(2):', tensor_a.float().pow(2)


def tensor_add_elments():
    """
    给张量添加元素,该方法比较蛮力
    :return:
    """
    tensor_a = th.from_numpy(np.array([[1, 2], [3, 4]]))
    tensor_a_shape = tensor_a.shape
    tensor_b = tensor_a.new(3, tensor_a_shape[1])
    tensor_b[:2] = tensor_a[:2]
    tensor_b[2] = tensor_a[1]
    print 'check ...'


if __name__ == '__main__':
    demo_tensor()
    # tensor_add_elments()


