# coding=utf-8
# date: 2018-8-30,16:50:12
# name: smz
"""
map(function, sequence[, sequence, ...]) -> list
    将function作用于sequence的元素上,并将所有的结果收集到列表中,最后返回该列表
    注意：
        1.如果提供了多个sequence的话,function在被调用的时候的argument就是每个sequence
          的元素构成的列表,即,function的argument的个数和sequence的个数一致=>将各个sequence取一个元素同时处理
          如果这些列表都不一样长的话,那么,缺少的元素就会使用None来替代.
        2.如果function是None的话,返回一个包含sequence的列表,如果有多个sequence的话,就返回一个元组,该元祖的结果类似与zip([], [])
        3.更细节的东西取python文件夹下查看
简单总结：
    1. function是要执行的函数,该函数由多个参数,如arg1,arg2,arg3
    2. 但是arg1,arg2,arg3都可以有多种取值,如：
        arg1: 1, 2, 3
        arg2: 4, 5, 6
        arg3: 6, 7, 8
    3.为了避免一遍又一遍地调用function(1, 4, 6), function(2, 5, 7), function(3, 6, 8)
      可以直接将arg1的可能取值放到一个列表1中,将arg2的可能取值放到列表2中,将arg3可能取值放到列表3中,并利用map函数来执行function
      即map(function, [1, 4, 6], [2, 5, 7], [3, 6, 8]) <=> function(1, 4, 6), function(2, 5, 7), function(3, 6, 8)
      即第一个sequence是函数function第一个位置参数的集合,第二个sequence是函数第二个位置参数的集合,同理第三个sequence
    4.在结果中,一个元素就是函数function执行一次的结果
    5.从上面的理解可以知道,若是补充的sequence中的元素为None的话,必须要调用的函数function在对应的位置参数上的参数可以为None才行,否则必然会
      发生函数function参数错误的异常
    6.默认的函数function应该就是一个接收任意个位置参数,并返回原值的函数
"""
def demo_map():
    print 'map(None, [1, 2, 3], [4, 5, 6]):\n', map(None, [1, 2, 3], [4, 5, 6])  # [(1, 4), (2, 5), (3, 6)]
    print 'map(lambda x: x+1, [1, 2, 3], [4, 5, 6]):\n', map(lambda x,y:x+1, [1, 2, 3], [4, 5, 6])  # 前面function的argument必须是两个


if __name__ == '__main__':
    demo_map()