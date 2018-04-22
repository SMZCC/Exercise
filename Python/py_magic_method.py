# coding=utf-8
# date:2018-3-27,12:55:44
# name: smz

__metaclass__ =type


class Sequence:  # 序列魔法
    def __init__(self, list=None):
        self.list= list

    # 实现取值
    def __getitem__(self, item):
        return self.list[item]

    # 实现取长度
    def __len__(self):
        return len(self.list)
        #return 'long'

    # 实现赋值操作
    def __setitem__(self, key, value):
        self.list[key] = value

    def __delitem__(self, key):
        del(self.list[key])

if __name__ == '__main__':
    seq = Sequence([1, 2, 3, 4])
    print seq[2]
    print len(seq)  # 失败,没有实现那个对应到魔法方法
    seq[0] = 5      # 失败,没有实现__setitem__魔法方法
    print seq[0]
    del(seq[0])    # 失败,没有实现__delitem__魔法方法
    print seq[:]