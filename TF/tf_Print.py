# coding=utf-8
# date: 2018-10-16,12:36:38
# name: smz

import tensorflow as tf
"""
tf.Print(inputTensor, [要查看的值], '输出结果的前缀'),如：
tensor_a = tf.convert_to_tensor([1, 2, 3])
tensor_a_message = tf.Print(tensor_a, [tensor_a.shape, tensor_a, tensor_a.name], 'tensor_a')
这里查看了tensor_a的三个信息:形状,值,名字,输出的格式如下: 
tensor_a[形状][值][名字]

注意：
    1.对于静态图来说,打印信息是调试的最好方法了
"""


def demo():
    tensor_a = tf.convert_to_tensor([1, 2, 3])
    tensor_a_message = tf.Print(tensor_a, [tensor_a.shape, tensor_a.name, tensor_a], 'tensor_a:')

    with tf.Session() as sess:
        sess.run([tensor_a_message])    # tensor_a:[3][Const:0][1 2 3]   shape是(3, ), 名字是Const操作下输出中索引为0的值,值为[1, 2, 3]


if __name__ == '__main__':
    demo()