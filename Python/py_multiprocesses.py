# coding=utf-8
# date: 2018-4-7,19:45:18
# name: smz


from multiprocessing.pool import ThreadPool  # 文件名的确定注意不要和包名相同,否则会引起"找不到"的麻烦


def hello():
    print 'hello, multiprocessing'
    return 1

def bye():
    print 'bye, multiprocessing'
    return 2

if __name__ == '__main__':
    pool = ThreadPool(processes=2)
    results = []
    results.append(pool.apply_async(hello))
    results.append(pool.apply_async(bye))  # 得到的是pool运行后的一个对象,并不是我自己定义的函数的返回值

    ans = [result.get() for result in results] # 使用get()方法获得函数真正的返回值
    print 'test'
