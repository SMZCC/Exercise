# coding=utf-8
# date: 2018-4-25,22:02:06
# name: smz

from __future__ import division

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def loss_one():
    tensor_a = tf.convert_to_tensor([[1, 2], [4, 5]], dtype=tf.float32)
    loss = tf.nn.l2_loss(tensor_a)     # 这玩意没有计算开方,直接是平方和除以2代替, 45.5
    tensor_a_square = tf.square(tensor_a)  # 这个是上式的两倍, 91
    loss_2 = tf.reduce_sum(tensor_a_square)
   
    with tf.Session() as sess:
        loss, loss_2 = sess.run(fetches=[loss, loss_2])

    print '-' * 50 + 'loss_one' + '-' * 50
    print 'loss:', loss
    print 'loss_2:', loss_2



if __name__ == '__main__':
    loss_one()
    # loss_two()