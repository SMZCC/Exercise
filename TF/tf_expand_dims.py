# coding=utf-8
# date: 2018-4-15,20:41:58
# name: smz


import tensorflow as tf


if __name__ == '__main__':

    input = tf.placeholder(dtype=tf.float32, shape=(None, 14, 14, 3), name='input')
    out = tf.map_fn(lambda x: tf.expand_dims(x, 0), input)  # 使用tf.map_fn()保证了输出的维度各轴是表示的正确的意义
    print 'test'