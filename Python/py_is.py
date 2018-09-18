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
    2.is主要比较的是对象本身,而==比较的是对象内的值
        i.对于一个全是布尔值的矩阵array_a来说, array_a is None, 判断的是array_a这个标识符是否是引用的一个None对象,
          返回值要么为真,要么为假
        ii.array_a == None, 判断的是array_a中的每个元素是否是None值,返回值依旧是与array_a形状相同的array,只不过其
           内中的元素值取决于比较的结果
        iii: 将一个全是bool值的矩阵中的元素全部取反的话,只需要使用array_a = (array_a == False)
             因为,若array_a中元素为False的话,那么该位置的元素的返回值则为True
                 若array_a中元素为True的话,那么该位置的元素的返回值则为False,从而实现了array_a中所有元素的取反操作
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