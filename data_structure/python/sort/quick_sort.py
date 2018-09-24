# coding=utf-8
# date: 2018-9-24,15:15:50
# name: smz

import sys
sys.path.insert(0, '/media/smz/SMZ_WORKING_SPACE/Github/Exercise/data_structure/python')
from basic_ops import swap


def partition(lyst, left, right):
    """用于分割列表,查找pivot的位置,pivot所在的位置索引称之为boundary
    升序情况下: pivot的前面的值都比pivot小,后面的值都比pivot大
    """
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot

    # 假设pivot是放在第一个位置
    boundary = left
    for idx in range(left, right): # 不包含right,right中的值是pivot
        if lyst[idx] < pivot:
            swap(lyst, boundary, idx)   # 重点: 在每一次分割的过程中将pivot的位置确定了,
            boundary += 1               # boundary上的值在下面的分割中是不会再被修改了

    # 将pivot放到boundary的位置上
    swap(lyst, boundary, right)
    return boundary


def quickSort(lyst, left, right):    # lyst是可变对象,在lyst上的操作都是直接有效的
    if left < right:
        boundary = partition(lyst, left, right)
        quickSort(lyst, left, boundary-1)
        quickSort(lyst, boundary+1, right)


if __name__ == '__main__':

    lyst = [2, 4, 7, 3, 9, 1]
    sorted_lyst = quickSort(lyst, 0, 5)
    print lyst



