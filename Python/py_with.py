# coding=utf-8
# date: 2018-4-1,16:16:24
# name: smz


import numpy as np


if __name__ == '__main__':

    with open('/media/smz/SMZ_WORKING_SPACE/Github/Exercise/labels/test_labels.txt') as f:
        data = f.read()

    print 'hello with'
    print data   # 变量值依旧存在,没有被释放
    print f  # 仅仅是上下文管理器发生了变化
