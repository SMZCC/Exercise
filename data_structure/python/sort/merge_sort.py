# coding=utf-8
# date: 2018-9-24,16:02:42
# name: smz

import sys
sys.path.insert(0, '/media/smz/SMZ_WORKING_SPACE/Github/Exercise/data_structure/python')
from basic_datatypes import Array


def merge(lyst, lystBuffer, low, middle, high):
    """合并索引为low与high之间的数,不同的子序列的low与high是不同的"""
    p1 = low  # 第一个子序列的开始索引
    p2 = middle + 1  # 第二个子序列的开始索引

    for i in range(low, high+1):
        # 如果两个子序列中某个被比较完了的话,那么就把另外一个序列直接赋值过去
        if p1 > middle:
            lystBuffer[i] = lyst[p2]
            p2 += 1
        elif p2 > high:
            lystBuffer[i] = lyst[p1]
            p1 += 1
        elif lyst[p1] < lyst[p2]:  # 比较两个子序列的元素的大小,升序时,按小的优先将数据合并
            lystBuffer[i] = lyst[p1]
            p1 += 1
        else:
            lystBuffer[i] = lyst[p2]
            p2 += 1

    for i in range(low, high+1):   # 索引从low到high部分lyst的数值顺序已经合并好了
        lyst[i] = lystBuffer[i]


def mergeSortHelper(lyst, lystBuffer, low, high):
    """将原数列分割, 并合并到lystBuffer中
       为了避免在递归的过程中多次生成lystBuffer,所以这里将lystBuffer放到函数外面
    """
    if low < high:
        middle = (low + high) // 2
        mergeSortHelper(lyst, lystBuffer, low, middle)   # 注意这里与快排不同,这里在分割的时候没有确定中点的位置,所以这里合并的时候必须要包含middle
        mergeSortHelper(lyst, lystBuffer, middle+1, high)
        merge(lyst, lystBuffer, low, middle, high)  # 将当前层的low, middel, high进行合并


def mergeSort(lyst):
    capacity = len(lyst)
    lystBuffer = Array(capacity)
    mergeSortHelper(lyst, lystBuffer, 0, capacity-1)

    return lyst


if __name__ == '__main__':
    lyst = [4, 3, 2, 7, 6]
    mergeSort(lyst)
    print lyst