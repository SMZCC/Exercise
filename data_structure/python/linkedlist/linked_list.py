# coding=utf-8
# date: 2018-9-25,09:30:25
# name: smz

import sys
sys.path.insert(0, '/media/smz/SMZ_WORKING_SPACE/Github/Exercise/data_structure/python')

from basic_datatypes import Node


def genLinkedList(num):
    """从链尾开始依次生成单链表的各个节点"""
    head = None
    for i in range(1, num+1):
        head = Node(i, head)
    return head


def printLinkedList(head):
    """从链头开始依次打印各个节点数据"""
    while head is not None:
        print head.data
        head = head.next_


def traverseLinkedList(head):
    """使用另外一个指针来遍历链表"""
    p = head  # 从链头开始
    while p is not None:
        print p.data
        p = p.next_

    print 'head.data:', head.data   # 10,head依旧是链头


if __name__ == '__main__':
    head = genLinkedList(10)
    traverseLinkedList(head)
