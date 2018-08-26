# coding=utf-8
# date: 2018-8-26,16:39:43
# name: smz

"""
__dict__属性是在类生成实例的时候,用于保存实例的各个属性值的,默认是个空字典,而且其中的属性可以通过<obj>.name来调用
"""
class Person_one(object):
    def __init__(self):
        self.name = 'smz'

class Person_two(object):
    def __init__(self):
        self.__dict__['name'] = 'smz_2'

class Person_three(object):
    pass

if __name__ == '__main__':
    person_one = Person_one()
    print person_one.__dict__   # {'name': 'smz'}

    person_two = Person_two()   # {'name': 'smz_2'}
    print person_two.__dict__
    print person_two.name       # smz_2

    person_three = Person_three()
    print person_three.__dict__   # {}