# coding=utf-8
# date: 2018-9-10,12:33:08
# name: smz

import numpy as np
from PIL import Image as im

"""
img = PIL.Image.open().convert('RGB')  # <Image>
img = np.asarray(img)  # ndarray
img = np.array(img)    # ndarray
注意：
    1.open()返回的是<Image>
    2.Image对象没有shape属性,只有size属性,且size只有宽高的大小,返回的元组是(w, h)
    3.使用np.asarray()之后,变为ndarray对象,具有shape属性,且shape为一般格式(h, w, c)
"""


def demo_one():
    img_path = './imgs/otb2015_results.png'
    img = im.open(img_path)
    print 'img.__class__:', img.__class__    # <class 'PIL.PngImagePlugin.PngImageFile'>
    print 'img.size:', img.size  # width, height

    img_asarray = np.asarray(img)
    print 'img_asarray.__class__:', img_asarray.__class__  # <type 'numpy.ndarray'>
    print 'img_asarray.shape:', img_asarray.shape    # (h, w, c)

    img_array = np.array(img)
    print 'img_array.__class__:', img_array.__class__
    print 'img_array.shape:', img_array.shape


def demo_two():
    img_path = './imgs/0001.jpg'
    img = im.open(img_path)
    print 'Image.open():', img
    print 'img.size:', img.size  # (640, 360)


if __name__ == '__main__':
    demo_one()