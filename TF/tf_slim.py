# coding=utf-8
# date: 2018-4-11,18:49:05
# name: smz


import tensorflow as tf
import tensorflow.contrib.slim as slim


def main(input):
    layer_1 = slim.conv2d(input, 10, [5, 5], 2, scope='layer_1')  # 默认是nn.relu激活
    layer_1_bn = slim.batch_norm()
    tf.metrics.mean()
    tf.identity()