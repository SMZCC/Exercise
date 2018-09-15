# coding=utf-8
# date: 2018-4-22,10:04:59
# name: smz


def function_a():
    print 'hello'
    function_a.stride = 3   # function_a是个对象,该对象可以被赋予属性,也可以被返回
    return function_a

if __name__ == '__main__':
    func= function_a()
    print 'check end'