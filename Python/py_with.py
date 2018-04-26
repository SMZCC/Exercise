# coding=utf-8
<<<<<<< HEAD
# date: 2018-4-1,16:16:24
# name: smz


import numpy as np


def get_file(file_dir):

    with open(file_path, 'r') as f:
        file = f
        return file  # 即使在这里返回也没有用
    #return file  # 到这里时,上下文管理器已经执行__exit__了, 所以return出去的东西到底能不能用,要看__exit__里是怎么实现的了


if __name__ == '__main__':

    with open('/media/smz/SMZ_WORKING_SPACE/Github/Exercise/labels/test_labels.txt') as f:
        data = f.read()

    print 'hello with'
    print data   # 变量值依旧存在,没有被释放
    print f  # 仅仅是上下文管理器发生了变化

    file_path = '/media/smz/SMZ_WORKING_SPACE/Github/Exercise/Python/files/train_labels.txt'
    f = get_file(file_path)
    print f.readline()

