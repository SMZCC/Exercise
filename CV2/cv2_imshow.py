# coding=utf-8
# date: 2018-9-19,21:13:02
# name: smz

import cv2
"""
cv2.imshow(<str>, image_data)
显示图片
注意:
    1.<str>参数为显示的框体的名字,该参数为位置参数,不可省略
    2.image_data需要是cv2.imread()读取的数据,如果是其他图形接口读取出来的数据,显示可能会类似于一个单通道图片的样子
    3.在python中,在调试的时候,使用cv2.imshow()的窗体会莫名奇妙没有响应,而matplotlib则不会,非必要还是使用matplotlib
    4.cv2.waitKey(delay=None),在使用cv2.imshow()之后,如果需要显示出来的话,还需要使用waitKey函数
"""


def demo_one():
    img = cv2.imread('/media/smz/SMZ_WORKING_SPACE/Github/Exercise/CV2/imgs/0001.jpg')
    cv2.imshow('image', img)
    cv2.waitKey()


if __name__ == '__main__':
    demo_one()