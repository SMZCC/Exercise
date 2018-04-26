# coding=utf-8
# date: 2018-4-26,18:46:04
# name: smz


from __future__ import absolute_import

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import sys
sys.path.append('/media/smz/SMZ_WORKING_SPACE/Mine_Trakcers/smz_repository')
from SMZ_Tools import SMZ_Tools
from SMZ_Utils import SMZ_Utils

smz_tools = SMZ_Tools()
smz_utils = SMZ_Utils()

def show_3D_one():

    fig = plt.figure()
    ax = Axes3D(fig)
    X = np.arange(0, 4, 0.25)
    Y = np.arange(0, 4, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    #Z = np.sin(R)
    Z = R

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)
    ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)  # 这是等高图
    ax.set_zlim(0, 10)

    # savefig('../figures/plot3d_ex.png',dpi=48)
    plt.show()


def show_3D_two():
    y, cs, rs = smz_utils.generate_label((10, 50), (101, 101))

    ### start
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(cs, rs, y, rstride=1, cstride=1, cmap='rainbow')
    ### end

    smz_tools.imshow_grid(y[None, :, :], shape=(1, 1), name='label', isgray=True)
    plt.show()

if __name__ == '__main__':
    show_3D_one()
    show_3D_two()
