# coding=utf-8
# date: 2018-4-12,16:02:44
# name: smz

import tensorflow as tf

if __name__ == '__main__':
    g = tf.Graph()
    g.as_default()

    mean, mean_op = tf.metrics.mean(values=tf.convert_to_tensor([1, 2, 3, 4, 5], dtype=tf.float32))

    init_global = tf.global_variables_initializer()
    init_local = tf.local_variables_initializer()

    sess = tf.InteractiveSession()
    sess.run([init_global, init_local])

    # sess.run()内的执行顺序是没有固定的顺序的,不是像你想象的那样如同你输入的顺序
    i = 0
    while True:
        mean_1, mean_2 = sess.run([mean, mean_op])  # 当先执行mean时,结果：0., 3.,当先执行mean_op,结果: 3., 3.
        i += 1
        if mean_1 == mean_2:
            print 'i:', i, 'means:', mean_1, mean_2
            break
    #print sess.run([mean_op, mean])  # 3., 0.,因为即使这样写,也不一定是先执行mean_op


    # sess.run()两个参数,一个是fetches,另一个是feed_dict