# coding=utf-8
# date: 2018-5-29,15:48:26
# name: smz

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def sin_gif():
    """
    练习gif生成
    :return:
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)

    x = np.linspace(0, 2*np.pi, 200)
    y = np.sin(x)
    line_sin, = ax.plot(x, y, label='sin(x)')
    dot, = ax.plot([], [], 'ro')

    def init(ax=ax, line_sin=line_sin):
        ax.set_xlim(0, 2*np.pi)
        ax.set_ylim(-1, 1)
        return line_sin


    def gen_dot():  # 返回用于每帧更新的数值
        for i in np.linspace(0, 2*np.pi, 200):
            new_dot = [i, np.sin(i)]
            yield new_dot  # 这里返回要跟新的数据

    def update_dot(new_dot, dot=dot):  # 使用数值更新artist,并且返回artist
        dot.set_data(new_dot[0], new_dot[1])
        return dot

    ani = animation.FuncAnimation(fig=fig, func=update_dot,
                                  frames=gen_dot, interval=10,
                                  init_func=init, save_count=200)
                                                   # 这句有点疑问,原本frames是接受一个
                                                   # int类型的属性值,但是如果接受一个
                                                   # int类型的话,那么update_dot就
                                                   # 就无法使用索引了,因为传入的参数不对

    ani.save('./saves/sin_dot.gif', writer='imagemagick', fps=100)
    plt.show()


if __name__ == '__main__':
    sin_gif()


