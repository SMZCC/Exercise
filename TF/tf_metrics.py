# coding=utf-8
# date: 2018-4-11,22:19:14
# name: smz

import tensorflow as tf

from tensorflow.python import debug as tfdbg


def metrics_mean_one():
    """
    accuracy is recomputed everytime it is evaluated.

    How tf.metrics.accuracy works in general is that it maintains two variables, total and count, each which starts at 0.
    Whenever accuracy is evaluated, it returns total / count (or 0 if count is 0), and does not modify total or count.
    accuracy also does not look labels or predictions. It just does a division.

    When update_op is evaluated, it uses labels and predictions to increase total and count.
    It increases total by the number of predictions that match the labels,
    and increases count by the total number of predictions.
    The idea is that you run update_op for every new batch of labels and predictions you get.
    Then, whenever you want to check to accuracy of all the batches you've seen so far,
    you evaluate accuracy, which will have the current accuracy of the batches seen so far.
    accuracy will change only when you run update_op, since only running update_op modifies total and count.

    In your Estimators case, update_op is never run during training, only during evaluation.
    The Estimator will automatically call the update_op every batch when
    you return the EstimatorSpec with eval_metric_ops during evaluation, but it does not during training.
    :param values:
    :return:
    """



    def get_mean(values):
        with tf.name_scope('get_mean'):
            mean, update_op = tf.metrics.mean(values)  # values = [1, 2, 3, 4, 5]
            with tf.control_dependencies([update_op]):
                mean = tf.identity(mean)   # 通过调试发现,依赖其实建立了,那么为什么值不符合预期呢？
            return mean


    values = tf.convert_to_tensor([1, 2, 3, 4, 5], dtype=tf.float32, name='values')
    mean= get_mean(values)
    init_global_variables = tf.global_variables_initializer()
    init_local_variables = tf.local_variables_initializer()

    sess = tf.InteractiveSession()
    sess.run(init_global_variables)
    sess.run(init_local_variables)
    print sess.run(values)
    # sess = tfdbg.LocalCLIDebugWrapperSession(sess)
    print '-' * 50 + 'one' + '-' * 50
    for i in range(5):
        print 'mean:', sess.run(mean)


def metrics_mean_two():



    def get_mean(values):
        with tf.name_scope('get_mean'):
            mean, update_op = tf.metrics.mean(values)  # values = [1, 2, 3, 4, 5]
            with tf.control_dependencies([update_op]):
                mean = tf.identity(mean)

            return mean  # 如果其是自带了上下文的话, 从头流到mean的话,会执行依赖,结果应当为3


    values = tf.convert_to_tensor([1, 2, 3, 4, 5], dtype=tf.float32)
    mean_1 = get_mean(values)
    mean_2 = get_mean(values)
    init_global_variables = tf.global_variables_initializer()
    init_local_variables = tf.local_variables_initializer()   # metrics的计算会用到local variables

    sess = tf.InteractiveSession()
    sess.run(init_global_variables)         # 总是出错,讲没有进行初始化mean/total,添加local_variables_initializer()解决
    sess.run(init_local_variables)          # 结果与预期不符合
    print sess.run(values)
    # print sess.run(update_op)
    print '-' * 50 + 'two' + '-' * 50
    print 'mean_1:', sess.run(mean_1)  # 0.0,应当为3  # TODO: 依赖不被执行？
    print 'mean_2:', sess.run(mean_2)  # 0.0,应当为6


def matrics_mean_three():
    values = tf.convert_to_tensor([1., 2., 3., 4., 5])
    with tf.name_scope('get_mean'):
        mean, update_op = tf.metrics.mean(values)  # values = [1, 2, 3, 4, 5]
        with tf.control_dependencies([update_op]):
            # mean = tf.identity(mean)
            sess = tf.InteractiveSession()
            init_global_variables = tf.global_variables_initializer()
            init_local_variables = tf.local_variables_initializer()
            sess.run([init_local_variables, init_global_variables])
            print '-' * 50 + 'three' + '-' * 50
            print sess.run(mean)  #TODO： 结果为 3  若使用mean = tf.identity(mean), 结果为6 ？


def metrics_mean_four():
    values = tf.convert_to_tensor([1., 2., 3., 4., 5])
    with tf.name_scope('get_mean'):
        mean, update_op = tf.metrics.mean(values)  # values = [1, 2, 3, 4, 5]
        with tf.control_dependencies([update_op]):
            # mean = tf.identity(mean)
            sess = tf.InteractiveSession()
            init_global_variables = tf.global_variables_initializer()
            init_local_variables = tf.local_variables_initializer()
            sess.run([init_local_variables, init_global_variables])
            print '-' * 50 + 'four' + '-' * 50
            for i in xrange(5):
                print sess.run(mean)    # 这里5次都是3.0是因为update_op只执行了一次,total以及count的值没有得到更新



def metrics_mean_five():
    values = tf.convert_to_tensor([1, 2, 3, 4, 5], dtype=tf.float32, name='values')

    mean, update_op = tf.metrics.mean(values)

    sess = tf.InteractiveSession()
    init_global = tf.global_variables_initializer()
    init_local = tf.local_variables_initializer()
    sess.run([init_local, init_global])

    sess.run(update_op)
    print '-' * 50 + 'five' + '-' * 50
    print sess.run(mean)


def metrics_mean_six():

    def get_mean(values):
        with tf.name_scope('get_mean'):
            mean, update_op = tf.metrics.mean(values, name='metrics_mean')

            with tf.control_dependencies([update_op]):
                mean_ = tf.identity(mean, name='identity_mean')   # 这里的这个identity 应该建立了依赖关系
                                                                  # 到了这里的这个张量的名字叫它 identity_mean
            return mean_

    values = tf.convert_to_tensor([1, 2, 3, 4, 5])

    mean_result = get_mean(values)

    init_global = tf.global_variables_initializer()
    init_local = tf.local_variables_initializer()

    sess = tf.InteractiveSession()
    sess.run([init_global, init_local])

    print '-' * 50 + 'six' + '-' * 50
    for i in range(5):
        print sess.run(mean_result)    # 这个他妈的有毒： 居然出现了不同的值：
                                       # 第一次运行： 0.0, 3.0, 3.0, 3.0, 3.0
                                       # 第二次运行： 0.0, 3.0, 3.0, 4.0, 3.0
                                       # 第三次运行： 3.0, 3.0, 3.0, 3.0, 3.0
                                       # 第四次运行： Nan 3.0, 3.0, 3.0, 3.75





if __name__ == '__main__':
   # metrics_mean_one()
   # metrics_mean_two()
   # matrics_mean_three()
   # metrics_mean_four()
   # metrics_mean_five()
   metrics_mean_six()

