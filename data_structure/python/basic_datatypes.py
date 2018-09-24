# coding=utf-8
# date: 2018-9-24,18:49:56
# name: smz


class Array(object):
    """实现一个可以保存任何类型的数组
        需要使用列表来实现,因为列表可以保存任何对象
    基本功能：
        1.在给定的位置访问或者替代数组的一个项 [] --> __getitem__(index) \__setitem__(index, newItem)
        2.查看数组的长度 len() --> __len__
        3.获取数组的字符串表示 str() --> __str__
        4.使用for循环 for -->  __iter__
    """
    def __init__(self, capacity, fillValue=None):
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        """len() capacity"""
        return len(self._items)

    def __str__(self):
        """str()"""
        return str(self._items)

    def __iter__(self):
        """for"""
        return iter(self._items)

    def __getitem__(self, idx):
        """[]"""
        return self._items[idx]

    def __setitem__(self, key, value):
        """选择运算符[]"""
        self._items[key] = value
