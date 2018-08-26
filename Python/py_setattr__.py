# coding=utf-8
# date: 2018-8-26,16:26:34
# name: smz

"""
__setattr__()若被实现的话,类的属性在被赋值时便会调用该方法
注意:
    1.由于存在属性赋值的时候就会调用__setattr__()方法,所以在__setattr__()方法的下面不能存在属性赋值,否则会无限递归
        如下是错误示范：
            def __setattr__(self, key, value):
                self.name = 'he'   # 这里通过调用__setattr__才能实现该赋值语句,由于调用赋值语句又转到调用__setattr__()方法,故而又重复前面的调用关系=>无限循环
    2.具体的使用方法暂时没有清楚
"""

class Person(object):
    def __init__(self):
        self.age = 12    # 这里给类的属性赋值了,实际上是调用了__setattr__()方法

    def __setattr__(self, age, value):
        print 'hello'

if __name__ == '__main__':
    person_one = Person()     # person_one 没有任何属性值,因为给属性赋值的语句被替换为了print 'hello'
    print person_one.__dict__  # 属性值字典中是空的
    print 'check ...'
