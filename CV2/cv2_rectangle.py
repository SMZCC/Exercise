# coding=utf-8
# date: 2018-9-19,21:09:37
# name: smz

import cv2
"""
cv2.rectangle(image, (x1, y1), (x2, y2), color=1, thickness=None)
在图片image上根据对角点绘制一个矩形
注意:
    1.这个奇葩的参数color的候选值是标量数字, 1 是代表黑色
    2.x1, y1, x2, y2都必须是整型
    3.老规矩,cv2画的东西要想一起显示的话,就需要调用cv2.imshow()以及cv2.waitkey()
"""

def demo_one():
    image = cv2.imread('/media/smz/SMZ_WORKING_SPACE/Github/Exercise/CV2/imgs/0001.jpg')
    cv2.rectangle(image, (10, 10), (50, 50), 1)
    cv2.imshow('image', image)
    cv2.waitKey()

if __name__ == '__main__':
    demo_one()

