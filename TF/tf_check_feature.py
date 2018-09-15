# coding=utf-8
# date: 2018-3-29,13:26:20
# name: smz

import tensorflow as tf
from skimage import io
import matplotlib.pyplot as plt

import sys
sys.path.append('/media/smz/SMZ_WORKING_SPACE/Mine_Trakcers/smz_repository')



def conv3x3(input, n_outs, name):
    input_shape = input.shape
    n_ins = input_shape[-1]
    with tf.variable_scope(name):
        w = tf.get_variable(name='weight', shape=(3, 3, n_ins, n_outs),
                            initializer=tf.truncated_normal_initializer(mean=0,stddev=1),
                            dtype=tf.float32)
    return tf.nn.conv2d(input=input, filter=w, strides=(1, 5, 5, 1), padding='SAME', name='out')


if __name__ == '__main__':
    sess = tf.InteractiveSession()
    x = io.imread('/media/smz/SMZ_WORKING_SPACE/Mine_Trakcers/smz_repository/trial_images/img_common/0001.jpg')
    x = x[None, :, :, :]
    input = tf.placeholder(dtype=tf.float32, shape=(None, None, None, 3))

    feature = conv3x3(input, 1, name='conv3x3')

    init = tf.global_variables_initializer()
    sess.run(init)
    feat = sess.run(feature, feed_dict={input:x})

    fig = plt.figure()
    ax_ori = fig.add_subplot(1, 2, 1)
    ax_ori.axis('off')
    ax_ori.imshow(x[0])
    ax_ori.set_title('ori_image')

    ax_feat = fig.add_subplot(1, 2, 2)
    ax_feat.axis('off')
    ax_feat.imshow(feat[0, :, :, 0])
    ax_feat.set_title('feature')

    plt.show()
    print 'test'