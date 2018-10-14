# coding=utf-8
# date: 2018-10-13,13:25:28
# name: smz

import tensorflow as tf

"""
sparseTensor = tf.SparseTensor(indices, values, dense_shape)
args: 
    indices: 对应的dense tensor中非0值的索引,索引需要是满索引
    values: 对应的dense tensor 中前面索引所对应的值,可以是标量,也可以是字符
    dense_shape: 完整tensor的形状
结果的使用方法：
    使用sparseTensorValue = sess.run(fetches=[sparseTensor])之后,得到的sparseTensorValue是个
    <list>, 只有一个元素,该元素是个<SparseTensorValue>,有三个元素,且实现了__getitem__,该三个元素分别对应了
    我们所输入的三个参数：
    sparseTensorValue[0][0]  对应  indices
    sparseTensorValue[0][1]  对应  values
    sparseTensorValue[0][2]  对应  dense_shape
注意： 
    1.<SparseTensor> 不支持__getitem__, 支持__getitem__的是经过sess.run之后得到的<SparseTensorValue>(这个对象的名字同你自己定义的变量)
    2.在python2和python3中,sess.run(<SparseTensor>)的结果还不一样,python2返回的是一个<list>,只有一个元素<SparseTensorValue>
      而python3中是直接返回<SparseTensorValue>而非一个<List>
    3.tf.sparse_placeholder()在使用feed_dict进行赋值的时候,传入的是(indices, values, shape)这三个参数,而不是一个
      <SparseTensor>
"""


def demoOne():
    indices = [(1, 1), (2, 2)]
    values = [4, 5]
    sparseTensor = tf.SparseTensor(indices=indices, values=values, dense_shape=[2, 3])

    sparsePlaceholder = tf.sparse_placeholder(dtype=tf.int32, name='sparseTensor')
    result = sparsePlaceholder

    with tf.Session() as sess:
        sparseTensorValue = sess.run(fetches=[sparseTensor])
        print 'sparseTensorValue:\n', sparseTensorValue
        print 'sparseTensorValue[0][0]:\n', sparseTensorValue[0][0]   # [[1, 1], [2, 2]]
        print 'sparseTensorValue[0][1]:\n', sparseTensorValue[0][1]   # [4, 5]
        print 'sparseTensorValue[0][2]:\n', sparseTensorValue[0][2]   # [2, 3]

        result_ = sess.run(fetches=[result], feed_dict={sparsePlaceholder:([[1,1], [2, 2]], [4, 5], [2, 3])})
        print 'result:\n', result_


if __name__ == '__main__':
    demoOne()