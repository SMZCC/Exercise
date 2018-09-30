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


class Grid(object):
    """数组的数组"""
    def __init__(self, rows, columns, fillValue=None):
        self._data = Array(rows)
        for row in range(rows):
            self._data[row] = Array(columns, fillValue)

    def getHeight(self):  # num of rows
        return len(self._data)

    def getWidth(self):  # length of one row
        return len(self._data[0])

    def __getitem__(self, idx):
        return self._data[idx]

    def __str__(self):
        result = ''
        for row in range(self.getHeight()):
            for column in range(self.getWidth()):
                result = result + str(self._data[row][column]) + ' '
            result = result + '\n'

        return result


class Node(object):
    """单链表节点:数据项+一个节点引用"""
    def __init__(self, data, next_=None):
        self.data = data
        self.next_ = next_



class TwoWayNode(Node):
    """双链表节点:数据域+两个节点引用域, 另外在生成链表的时候,会额外使用一个指针域保存尾节点"""
    def __init__(self, data, previous=None, next_=None):
        super(TwoWayNode, self).__init__(data, next_)
        self.previous = previous


class BSTNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right