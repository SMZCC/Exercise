# coding=utf-8
# date:2018-9-24,14:51:55
# name: smz


def swap(lyst, i, j):
    """
    交换lyst[i]与lyst[j]的值
    """
    if i == j:
        return lyst
    else:
        temp = lyst[i]
        lyst[i] = lyst[j]
        lyst[j] = temp
        return lyst