# coding=utf-8
# date: 2018-9-10,12:37:13
# name: smz

import cv2
"""
img = cv2.imread(path)
注意：
    1.返回的对象为np.ndarray类型
    2.shape属性返回值为:(h, w, c)
    3.path使用绝对路径,不要使用相对路径,因为我发现了一个贼他妈奇葩的bug,该cv2_imread.py文件和cv2_imshow.py文件同时
      使用相对目录: './imgs/0001.jpg'的话,cv2_imshow.py中的读取结果为None,真是奇葩至极,原因不明
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
    demo_two()