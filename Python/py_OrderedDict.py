# coding=utf-8
# date: 2018-8-26,21:29:33
# name: smz

from collections import OrderedDict
"""
有序字典,初始化为一个空字典,没有任何键值对
"""
def demo_ordereddict():
    ord = OrderedDict()
    for name, value in ord:
        print name, value


if __name__ == '__main__':
    demo_ordereddict()