# coding=utf-8
# date: 2018-3-29,18:34:50
# name: smz

from collections import OrderedDict
"""
dict_ = dict()
dict_ = OrderedDict()
Dict是最常用的基本对象之一:{key1:value1, key2:value2, ...}
基本方法:
    .[key]                  返回当前<Dict>键为key的值
    .keys()                 返回当前<Dict>所有的键,是个<List>, [key1, key2, ...]
    .values()               返回当前<Dict>所有的值,是个<List>, [value1, value2, ...]
    .items()                返回当前<Dict>所有的键值对,是个<List>, [(key1, value1), (key1, value2), ...]
    .update(<Dict1>)        按照<Dict1>中的键值对修改当前<Dict>键值对
                                1.该方法没有返回值,直接修改原对象
                                2.若是当前<Dict>中没有对应的键,那么就添加该键值对到当前的<Dict>中
    
注意:
    1.内置类 dict(), 同名,自定义变量的时候注意不要重名
    2.直接使用in <Dict>的形式会直接遍历键
"""


def demo_one():
    dict_ = OrderedDict()
    dict_['one'] = 1
    dict_['two'] = 2

    print 'dict_.keys():', dict_.keys()
    print 'dict_.values():', dict_.values()
    print 'dict_.items():', dict_.items()
    print "dict_.update({'two':12}):", dict_.update({'two':12}), dict_
    print "dict_.update({'three':3})", dict_.update({'three':3}), dict_

    for key in dict_:
        print key


if __name__ == '__main__':
    demo_one()