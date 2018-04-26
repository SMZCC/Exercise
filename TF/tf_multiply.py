# coding=utf-8
# date: 2018-4-25,17:41:10
# name: smz


import tensorflow as tf


def multi_one():
    g = tf.Graph()
    with g.as_default():
        tensor_a = tf.convert_to_tensor([[1, 2], [3, 4]])
        tensor_b = tf.convert_to_tensor([[1, 1], [1, 1]])
        result_multiply = tf.multiply(tensor_a, tensor_b)
        result_matmul = tf.matmul(tensor_a, tensor_b)
    with tf.Session(graph=g) as sess:
        out_matmul, out_multiply = sess.run(fetches=[result_matmul, result_multiply])

    print '-' * 50 + 'multi_one' + '-' * 50
    print 'out_matmul:\n', out_matmul
    print 'out_multiply:', out_multiply

if __name__ == '__main__':
    multi_one()
