# coding=utf-8
# date: 2018/7/26, 14:50
# name: smz

import logging
import tensorflow as tf

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s, %(message)s',
                    datefmt='%Y-%m-%d, %H:%M:%S',
                    filename='../Logs/tf_io.log',
                    filemode='a')

con = logging.StreamHandler()
con_for = logging.Formatter(fmt='%(asctime)s, %(message)s',
                            datefmt='%Y-%m-%d, %H:%M:%S')
con.setFormatter(con_for)
logging.getLogger().addHandler(con)


def write_tfrecords_file():
    """tf的专属数据格式"""
    # 根据协议写文件
    tfrd_writer = tf.python_io.TFRecordWriter('../Data/tf_io_stat.tfrecord')
    # 构造要写入对象
    for i in range(1, 3):
        example = tf.train.Example(   # 一个样例Example由一组特征构成
            features=tf.train.Features(   # 一组特征Features是 由多个特征向量构成的python字典
                feature={
                    'id': tf.train.Feature(int64_list=tf.train.Int64List(value=[i])),   # 一个特征向量Feature
                    'age': tf.train.Feature(int64_list=tf.train.Int64List(value=[i*24])),
                    'income': tf.train.Feature(float_list=tf.train.FloatList(value=[i*2048.0])),
                    'outgo': tf.train.Feature(float_list=tf.train.FloatList(value=[i*1024.0]))
                }
            )
        )

    tfrd_writer.write(example.SerializeToString())
    tfrd_writer.close()


def read_tfrd_file():
    """读取tfrecord"""
    files_queue = tf.train.string_input_producer(['../Data/tf_io_stat.tfrecord'])

    tfrd_reader = tf.TFRecordReader()
    _, serialized_example = tfrd_reader.read(files_queue)

    features = tf.parse_single_example(serialized_example,
                                       features={
                                           'id': tf.FixedLenFeature([], tf.int64),
                                           'age': tf.FixedLenFeature([], tf.int64),
                                           'income': tf.FixedLenFeature([], tf.float32),
                                           'outgo': tf.FixedLenFeature([], tf.float32)
                                       })
    with tf.Session() as sess:
        # id_ = sess.run(features['id'])   # 不可以这样写，否则又是停在Creating Tensorflow device 而没有任何动静

        logging.info(features)
        logging.info(features['id'])  # 可是该features['id']是一个张量，却不能通过sess.run()来获得值的大小？


if __name__ == '__main__':
    # write_tfrecords_file()
    read_tfrd_file()