# coding=utf-8
# date: 2018-8-25,21:19:17
# name: smz

import tensorflow as tf
"""
tf中最基本的类
tensor = tf.convert_to_tensor(value, dtype, name)
基本方法:
   $tensor.eval()  获取tensor的值
   
注:
   凡是需要在环境tf.Session()中执行的方法,前面都有标记$
    
"""
def demo_tensor():

    tensor_a = tf.convert_to_tensor(12)
    print 'tensor_a:', tensor_a
    with tf.Session() as sess:
        print 'tensor_a.eval():', tensor_a.eval()



if __name__ == '__main__':
    demo_tensor()