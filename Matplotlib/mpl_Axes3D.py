# coding=utf-8
# date: 2018-4-26,18:46:04
# name: smz


from __future__ import absolute_import

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d.art3d import PolyCollection

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


def show_3D_three():

    def randrange(n, vmin, vmax):
        return np.random.randint(vmin, vmax, n)

    def fun(ax, ben, color, n):

        x5 = randrange(n, 0, 100)
        y5 = randrange(n, 0, 100)
        z5 = randrange(n, 5, 6)
        ax.scatter(x5, y5, z5, s=50, c=color, marker='o')
        poly3d = [[(0, 0, ben), (0, 100, ben), (100, 100, ben), (100, 0, ben)]]
        ax.add_collection3d(Poly3DCollection(poly3d, facecolors=color, linewidths=1, alpha=0.2))

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    fun(ax, 5, "red", 10)
    fun(ax, 50, "green", 15)
    fun(ax, 90, "blue", 10)

    n = 50
    color = "yellow"
    zl, zh = (0, 100)
    xa = randrange(n, 0, 100)
    ya = randrange(n, 0, 100)
    za = randrange(n, zl, zh)
    ax.scatter(xa, ya, za, s=50, c=color, marker='o')

    ax.set_xlabel('$x^{(1)}$', size=20)  # $x^{(1)}$是Latex表达式
    ax.set_xlim3d(0, 100)
    ax.set_ylabel('$x^{(2)}$', size=20)
    ax.set_ylim3d(0, 100)
    ax.set_zlabel('$z$', size=20)
    ax.set_zlim3d(0, 100)
    plt.show()

def show_3D_four():
    fig = plt.figure()
    # 创建3d图形的两种方式
    # ax = Axes3D(fig)
    ax = fig.add_subplot(111, projection='3d')
    # X, Y value
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)  # x-y 平面的网格
    R = np.sqrt(X ** 2 + Y ** 2)
    # height value
    Z = np.sin(R)
    # rstride:行之间的跨度  cstride:列之间的跨度
    # rcount:设置间隔个数，默认50个，ccount:列的间隔个数  不能与上面两个参数同时出现
    # vmax和vmin  颜色的最大值和最小值
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
    # zdir : 'z' | 'x' | 'y' 表示把等高线图投射到哪个面
    # offset : 表示等高线图投射到指定页面的某个刻度
    ax.contourf(X, Y, Z, zdir='z', offset=-2)
    # 设置图像z轴的显示范围，x、y轴设置方式相同
    ax.set_zlim(-2, 2)
    plt.show()

def show_3D_five():
    def anim_set_data(artist, data, fixed_limits=True):
        """
        """
        # of course mpl has to be difficult and not allow set_data
        # on polycollections...
        ax = artist.axes
        if isinstance(artist, PolyCollection) or isinstance(artist, Poly3DCollection):
            ax.collections.remove(artist)

            if data is not None:
                pckwargs = {k: v for k, v in data.items() if k != 'data'}
                data = data['data']
            else:
                data = []
                pckwargs = {}

            if len(data):
                xarray = np.array(data[:, :, 0])
                yarray = np.array(data[:, :, 1])
            else:
                xarray = []
                yarray = []

            if isinstance(artist, Poly3DCollection):
                if len(data):
                    zarray = np.array(data[:, :, 2])
                else:
                    zarray = []
                artist = Poly3DCollection(data, **pckwargs)
            else:
                zarray = None
                artist = PolyCollection(data, **pckwargs)

            ax.add_collection(artist)

            created = True
        else:
            if data is None:
                # TODO: may need to be smart here to send the right shape,
                # especially for 3d axes
                data = ([], [])
            artist.set_data(*data)

            created = False
            xarray = np.array(data[0])
            yarray = np.array(data[1])
            zarray = None  # TODO: add support for 3d

        # TODO: need to be smarter about this - the user may have provided limits
        # in one of the plot_argss
        if not fixed_limits:
            ax = handle_limits(ax, xarray, yarray, zarray, apply=True)

        return artist, created

if __name__ == '__main__':
    # show_3D_one()
    # show_3D_two()
    # show_3D_three()
    show_3D_four()