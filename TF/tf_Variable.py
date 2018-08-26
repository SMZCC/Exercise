# coding=utf-8
# date: 2018-3-31,20:43:06
# name: smz


import tensorflow as tf

def main():
    sess = tf.InteractiveSession()
    with tf.variable_scope('scope_1', 'defaut_scope') as sc:
        print 'scope_1:', sc.name   #

    with tf.variable_scope('default_scope') as sc:
        print 'default_scope:', sc.name

    # with tf.variable_scope(default_name='test_default_name') as sc:
    #     print 'test_default_name:', sc.name  # 这里位置参数不可省,故而这种跳过位置参数来给关键字
    #                                          # 赋值的方式是不行的,那么既然第一个位置参数不可省略,那么那个设置默认名字的关键字参数
                                               # 又有什么意义呢？

if __name__ == '__main__':
    main()
