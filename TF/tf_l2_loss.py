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
    I = tf.eye(2)
    loss_3 = tf.nn.sigmoid_cross_entropy_with_logits()
    tf.nn.cross
    with tf.Session() as sess:
        loss, loss_2 = sess.run(fetches=[loss, loss_2])

    print '-' * 50 + 'loss_one' + '-' * 50
    print 'loss:', loss
    print 'loss_2:', loss_2

def loss_two():
    x = np.linspace(start=-100, stop=100, num=200)
    y = x ** 2 / (x ** 2 + 1)

    fig = plt.figure()
    # ax = plt.Axes(fig, rect=(0., 0., 1., 1.))   # 这样召唤出来的ax是没有spine的
    # ax.set_axis_off()
    ax = fig.add_subplot(111)     # 这样召唤出来的ax是有spine的
    # fig.add_axes(ax)
    line, = ax.plot(x, y)
    plt.show()



if __name__ == '__main__':
    # loss_one()
    loss_two()