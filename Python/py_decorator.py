# coding=utf-8
# date: 2018-8-13,20:15:35
# name: smz

class Person:
    def __init__(self):
        self.__age__ = 10

    @property     # 属性装饰器
    def age(self):      # 将函数age转换成实例的名称为age的属性,可通过instance.age访问,此时该属性只能是可读的
        return self.__age__   # 访问设置

    # 补上写入方法
    @age.setter
    def age(self, value):
        self.__age__ = value

if __name__ == '__main__':
    p_one = Person()
    # p_one.age = 20   错误,无法这样设置,因为此时这里的这个age属性缺乏实现与@property同时生成的@age_setter所对应的方法
                    # 另,若设置了@age_setter所对应的方法的话,p_one = 20实际上是调用了一个访问器方法,而不仅仅是单纯的赋值操作
    p_one.age = 30
    print  p_one.age