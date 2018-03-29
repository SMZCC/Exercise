# coding=utf-8
# date: 2018-3-29,18:34:50
# name: smz

from collections import OrderedDict

dict = OrderedDict()
dict['one'] = 1
dict['two'] = 2


if __name__ == '__main__':
    dict.update({'one':3} )
    print dict