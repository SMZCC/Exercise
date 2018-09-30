# coding=utf-8
# date: 2018-9-25,13:59:43
# name: smz

"""
当要在对象中实现原对象的副本的话,需要在构造函数中分解参数并赋值才可,
因为一旦调用class(param),param只能是__init__中self之外的参数
"""


class PersonOne(object):
    def __init__(self, age=None, name=None):
        self.name = name
        self.age = age

    def new(self):
        """self作为类调用参数时的现象"""
        p = PersonOne(self)   # 将原对象的引用传递给了age
        return p


class PersonTwo(object):
    def __init__(self, arg):
        self.age = arg.age
        self.name = arg.name

    def new(self):
        p = PersonTwo(self)
        return p    # 原对象的一个副本,因为arg得到的值是self,代表原对象


if __name__ == '__main__':
    p1 = PersonOne(10, 'smz')
    p2 = p1.new()
    print 'p1:', p1     # p1: <__main__.PersonOne object at 0x7f4ec1883390>
    print 'p1.name:', p1.name  # smz
    print 'p1.age:', p1.age    # 10
    print 'p2.name:', p2.name   # None
    print 'p2.age:', p2.age     # 这个是对象的引用 p1  <__main__.PersonOne object at 0x7f4ec1883390>

    p3 = PersonTwo(p1)
    p4 = p3.new()
    print 'p3:', p3        # <__main__.PersonTwo object at 0x7f20e2a94590>
    print 'p3.name:', p3.name   # smz
    print 'p3.age:', p3.age     # 10
    print 'p4.name:', p4.name   # smz
    print 'p4.age:', p4.age     # 10

