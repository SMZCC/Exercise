# coding=utf-8
# date: 2018-3-31,14:15:21
# name: smz


import tensorflow as tf


def get_tf_cond(sess):

    def true_result():
        return tf.convert_to_tensor(1)

    def false_result():
        return tf.convert_to_tensor(0)

    tf_cond = tf.cond(tf.cast(True, tf.bool), true_fn=true_result, false_fn=false_result)
    result = sess.run(tf_cond)        # pred 必须是tf.bool类型
                                      # true_fn, false_fn 不可少
                                      # true_fn, false_fn 必须要有返回值
                                      # true_fn, false_fn 必须要返回相同数目的同类型的值
    print result

if __name__ == '__main__':
    sess = tf.InteractiveSession()
    get_tf_cond(sess)