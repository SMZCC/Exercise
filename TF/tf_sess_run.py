# coding=utf-8
# date: 2018-4-12,16:02:44
# name: smz

import tensorflow as tf


def example_one():
    g = tf.Graph()
    g.as_default()  # 这样写其实是错误的

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
            print '-' * 50 + 'example_one' + '-' * 50
            print 'i:', i, 'means:', mean_1, mean_2
            break
    #print sess.run([mean_op, mean])  # 3., 0.,因为即使这样写,也不一定是先执行mean_op


    # sess.run()两个参数,一个是fetches,另一个是feed_dict

    ############## 以上没有固定顺序的情况是使用的tf.InteractiveSession(),但是使用tf.Session()是会按我们所期望的顺序执行的 ########

def example_two():
    g = tf.Graph()

    with g.as_default():     # 正确用法
        mean, op_update = tf.metrics.mean(tf.convert_to_tensor([1, 2, 3, 4, 5, 6], dtype=tf.float32))

        init_global = tf.global_variables_initializer()
        init_local = tf.local_variables_initializer()

        with tf.Session() as sess:   # 使用该tf.Session()其执行的顺序就不是随机的,而是会根据我们的需要进行执行
            sess.run([init_global, init_local])

            i = 0
            while True:
                i += 1
                mean_1, mean_2 =  sess.run(fetches=[mean, op_update])

                if mean_1 != mean_2:
                    print '-' * 50 + 'example_two' + '-' * 50
                    print 'i:', i , 'mean_1:', mean_1, 'mean_2:', mean_2
                    break
                elif i == 10000:
                    print '-' * 50 + 'example_two' + '-' * 50
                    print 'up to 10000 iters, ', 'mean_1:', mean_1, 'mean_2:', mean_2
                    break



if __name__ == '__main__':
    example_one()
    example_two()