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



def log(func, text):  # 这个是错误的,因为无法传入被装饰的函数

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


def show_func_name(func):  # 装饰器函数
    print 'func_name:', func.__name__
    return func

@show_func_name
def say_hi():    # 被装饰函数
    print 'say_hi'


# 返回函数的函数,当一个函数不要求被立刻执行的时候,可以将其作为一个函数对象返回
def sum_(*args):  # 表示原函数,看看
    sum = 0
    for arg in args:
        sum += arg
    return sum


@show_func_name
def lazy_sum_1(*args): # 检查参数在不同位置时,不同的情况
    def sum():
        sum = 0
        for arg in args:
            sum += arg
        return sum
    return sum

@show_func_name
def lazy_sum_2():
    def sum(*args):
        sum = 0
        for arg in args:
            sum += arg
        return sum
    return sum

def lazy_sum_3(*args):
    @show_func_name
    def sum_3():
        sum = 0
        for arg in args:
            sum += arg
        return sum
    return sum_3





if __name__ == '__main__':
    # list_a = MyList([1, 2, 3])
    # print list_a
    #
    # h = hi()
    # print h

    # for f in outer():
    #     print f()
    #say_hello()
    # objTestProperty = TestProperty()
    # objTestProperty.name = 'me'
    # print objTestProperty.name
    say_hi() # 这里发现了一个奇怪的现象：我say_hi(), sum_1, sum_2
             # 都使用了show_func_name 函数,但是他们没有按照我调用的顺序进行
             # 使用显示函数名字,而是一次将所有的函数名都显示了
             # 通过在装饰器中打断点我发现,装饰器在函数调用之前,好像
             # 在语法检查阶段就直接运行了,那么如果我想直接让装饰器和
             # 函数同时运行,我恐怕要使用个闭包
    sum_1 = lazy_sum_1(1, 2, 3, 4, 5)
    print sum_1()

    sum_2 = lazy_sum_2()
    print sum_2(6, 7, 8, 9, 10)

    sum_3 = lazy_sum_3(1,2, 3, 4, 5, 6)  # 在将装饰器放入闭包中后,装饰器便和
    print sum_3()                        # 函数的执行变成对了,没有在一开始
                                         # 的检查阶段直接运行出来