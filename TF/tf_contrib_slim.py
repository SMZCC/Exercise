# coding=utf-8
# date: 2018-3-31,15:49:09
# name: smz


import tensorflow as tf


if __name__ == '__main__':
    slim = tf.contrib.slim
    weights_regularizer = slim.l2_regularizer(0.005)

    print 'test'