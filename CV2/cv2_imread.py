# coding=utf-8
# date: 2018-9-10,12:37:13
# name: smz

import cv2
"""
img = cv2.imread(path)
注意：
    1.返回的对象为np.ndarray类型
    2.shape属性返回值为:(h, w, c)
"""


def demo_one():
    """
    :return:
    """
    img = cv2.imread('./imgs/otb2015_results.png')
    print 'img:', img
    print 'img.__class__:', img.__class__   # np.ndarray
    print 'img.shape:', img.shape

def demo_two():
    """
    :return:
    """
    img = cv2.imread('./imgs/0001.jpg')
    print 'img:', img
    print 'img.shape:', img.shape


if __name__ == '__main__':
    demo_one()