# coding=utf-8
# date: 2018-5-24,10:17:23
# name: smz


from __future__ import division
from __future__ import absolute_import

import numpy as np
import matplotlib.pyplot as plt


def exercise():
    loss = []
    alpha = [0.000002, 0.000002]
    # samples && labels
    X = np.array([[143, 1],[145, 1],[146,1],[147,1],[149,1],[150,1],
                  [153,1],[154,1],[155,1],[156,1],[157,1],[158,1],
                  [160,1],[162,1],[164,1],[165,1]], dtype=np.float32)
    y = np.array([88, 85, 88, 91, 92, 93, 93, 95, 96, 98, 97, 96, 98, 99, 100, 102], dtype=np.float32)

    N = len(X)
    # weights
    theta1 = 0.
    theta2 = 0.
    theta = np.array([theta1, theta2])

    # loss
    loss_init = np.sum(np.square(np.matmul(X, theta) - y) / N)
    loss.append(loss_init)

    for i in range(1000):
        # gradient
        X_T =  np.transpose(X, (1, 0))
        X_T_mul_X = np.matmul(X_T, X)

        differ = np.matmul(X_T_mul_X, theta) - np.matmul(X_T, y)

        gradient = 2 / N * differ
        # apply gradient
        theta = theta - alpha * gradient

        loss_update = np.sum(np.square(np.matmul(X, theta) - y) / N)
        loss.append(loss_update)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(left=0, right=1000)
    max = np.max(loss)
    ax.set_ylim(bottom=0, top=max)
    x_data = [data for data in range(1001)]
    line, = ax.plot(x_data, loss)

    plt.show()


    print 'test'

if __name__ == '__main__':
    exercise()