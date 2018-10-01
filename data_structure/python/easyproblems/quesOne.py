# coding=utf-8
# date: 2018-9-28, 14:48:05
# name: smz


def quesOne(n):
    height = 100.
    sum = 100.
    for i in range(1, n):
        height = height / 2.
        sum = sum + height * 2
    return height, sum


if __name__ == '__main__':
    height, sum = quesOne(10)
    print 'height:%f, sum:%f'%(height, sum)