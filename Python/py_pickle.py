# coding=utf-8
# date: 2018-9-10,11:17:34
# name: smz

import pickle
"""
pickle.dump(obj, fp, protocol)
 obj: 要写入的数据对象
 fp: 用于保存的数据文件,需要使用open()来打开
 protocol: 写入协议,若想py2和py3能同时打开同一个pkl文件,可令protocol=2
 
注：
    1.只有指定了protocol的dump才会保存成未知的pkl文件,否则都像是文本文件的样子
    2.pickle序列化的什么对象,读取出来的就是什么对象
    3.如果某个对象无法序列化,尝试使用二进制的方式打开文件来保存
"""


def demo_one():
    data = [1, 2, 3, 4]
    with open('./saved_files/pickle_one.pkl', 'w') as f:
        pickle.dump(data, f)

def demo_two():
    data = {'one':1, 'two':2}
    with open('./saved_files/pickle_two.pkl', 'w') as f:
        pickle.dump(data, f)

def demo_three():
    data = [1, 2, 3, 4]
    with open('./saved_files/pickle_three.pkl', 'wb') as f:
        pickle.dump(data, f)

# 以下保存出来的是白色文件
def demo_four():
    data = [1, 2, 3, 4]
    with open('./saved_files/pickle_four.pkl', 'w') as f:
        pickle.dump(data, f, -1)

def demo_five():
    data = [1, 2, 3, 4]
    with open('./saved_files/pickle_five.pkl', 'w') as f:
        pickle.dump(data, f, 2)

if __name__ == '__main__':
    # demo_one()
    # demo_two()
    # demo_three()
    # demo_four()
    demo_five()