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
"""
def demoOne():
    indices = [(1, 1), (2, 2)]
    values = [4, 5]
    sparseTensor = tf.SparseTensor(indices=indices, values=values, dense_shape=[2, 3])

    with tf.Session() as sess:
        sparseTensorValue = sess.run(fetches=[sparseTensor])
        print 'sparseTensorValue:\n', sparseTensorValue


if __name__ == '__main__':
    demoOne()