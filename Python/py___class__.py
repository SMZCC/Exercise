# coding=utf-8
# date: 2018-8-20,18:28:31
# name: smz

"""
在没有生成实例的时候,__class__以及__name__均是默认值,__class__为type类,类名__name__为:type
当生成实例的时候
    __class__为生成实例的类
    __name__为生成该实例的类的名字

"""

class Person(object):
    def __init__(self):
        self.name = 'Iris'
        self.age = 12
        self.class_ = self.__class__
        self.name_ = self.__class__.__name__



if __name__ == '__main__':
    print '#############未实例化之前######################'
    print '__class__:', Person.__class__
    print '__class__.__name__:', Person.__class__.__name__
    print '###############实例化之后######################'

    p = Person()
    print 'self.class_:', p.class_
    print 'self.name_:', p.name_


