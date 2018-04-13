# coding=utf-8
# date: 2018-4-12,10:25:52
# name: smz


import numpy as np
import tensorflow as tf
from tensorflow.python import debug as tfdbg
# 妹的,感觉很不习惯,以run为单位,每次列出所有的tensor的取值情况

if __name__ == '__main__':

    H = 128    # 滤波器长度
    L = 10240  # 输入信号长度
    miu = 1    # 学习速率

    # 载入滤波器权值
    filter = np.random.randn(H)
    # 载入信号值
    sig_in = np.random.randn(L)

    weights = tf.Variable(tf.zeros([H], dtype=tf.float32), name='weights')  # 训练权值
    input_vec = tf.placeholder(tf.float32, shape=(H), name='input')       # 输入信号窗口
    prod = tf.reduce_sum(tf.multiply(input_vec, weights), name='prod')   # 输出信号
    desired = tf.reduce_sum(tf.multiply(input_vec, filter), name='desired') # 期望信号
    err = tf.nn.l2_loss(desired - prod, name='err')                     # 误差信号
    opt = tf.train.GradientDescentOptimizer(miu).minimize(err) # 梯度下降优化器
    mse = tf.nn.l2_loss(weights - filter, name='mse')                   # 训练权值与预期权值的 MSE

    with tf.Session() as sess:
      sess = tfdbg.LocalCLIDebugWrapperSession(sess)                      # 被调试器封装的会话
      sess.add_tensor_filter("has_inf_or_nan", tfdbg.has_inf_or_nan)      # 调试器添加过滤规则
      tf.global_variables_initializer().run()                             # 变量初始化
      print 'Initialized!'
      for step in xrange(L - H):
        sess.run(opt, feed_dict={input_vec:sig_in[step:(step+H)]})        # 输入信号窗口每次滑动一个单位
        print sess.run(mse)                                               # 打印输出，观察训练权值是否收敛到与预期权值一致

