# coding=utf-8
# date: 2018-9-16,19:38:11
# name: smz

"""
same = a is b
返回标示符a和b是否是引用的同一个<obj>
1.若是,返回True
2.不是,返回False

注意：
    1.判断一个引用是否是None的话,要使用is,而不是使用==,虽然==也能实现功能,但是python推荐使用is,原因待机缘
"""


class Person(object):
    def __init__(self):
        self.age = 12
        self.gender = 'man'


def demo_one():
    personOne = Person()
    personTwo = Person()

    same = personTwo is personOne
    print 'personOne is personTwo:', same

    if not same:
        print 'id(personOne):', id(personOne)
        print 'id(personTwo):', id(personTwo)


def demo_two():
    personOne = Person()
    personTwo = personOne

    same = personOne is personTwo
    print 'personOne is personTwo:', same

    if same:
        print 'id(personOne):', id(personOne)
        print 'id(personTwo):', id(personTwo)


if __name__ == '__main__':
    # demo_one()
    demo_two()