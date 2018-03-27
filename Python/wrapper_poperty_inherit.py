# coding=utf-8
# date:2018-3-27,16:36:57
# name: smz


__metaclass__ = type


class MyList(list):   # 这里这个有个UserList不知道怎么用
    def __init__(self, *arg):
        super(MyList, self).__init__(*arg)  # *arg是上面到参数


def hi():
    print 'hi'

def outer():
    fs = []
    for j in range(1, 4):
        def inner(k=j):
            return k*k
        fs.append(inner)
    return fs



def log(func, text):

    def wrapper(*args, **kw):
        print '%s, call %s'%(text, func.__name__)
        return func()
    return wrapper



def say_hello():
    print 'hello'


class TestProperty:

    @property   # 属性,属性就应该可以被获得,可以被赋值
    def name(self):
        return self.__name  # 私有,因为反正可以通过@name.setter来获得

    @name.setter   # 赋值属性
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError



if __name__ == '__main__':
    # list_a = MyList([1, 2, 3])
    # print list_a
    #
    # h = hi()
    # print h

    # for f in outer():
    #     print f()
    #say_hello()
    objTestProperty = TestProperty()
    objTestProperty.name = 'me'
    print objTestProperty.name