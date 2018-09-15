# coding=utf-8
# date: 2018-9-10,10:26:57
# name: smz

import tensorflow as tf
"""
tf中的随机种子分为图随机种子和操作随机种子,如果是单纯的指定操作的随机种子,那么只有该操作的结果是可重复的,如果指定的是图随机种子,
那么该图中的所有随机操作都是可重复的
tf.set_random_seed()
"""


def demo_random_seed():
    tf.set_random_seed(10)   # 使该图上所有的随机操作结果能够重复,这里是默认图
    tensor_uniform_a = tf.random_uniform([1])
    tensor_nomal_b = tf.random_normal([1])
    with tf.Session() as sess:
        print 'tf.random_uniform:', tensor_uniform_a    # 返回的是<Tensor>
        print 'tf.random_uniform((1)):', sess.run(tensor_uniform_a)   # [0.21322536]

        print 'tf.random_normal:', tensor_nomal_b
        print 'tf.random'


if __name__ == '__main__':
    demo_random_seed()