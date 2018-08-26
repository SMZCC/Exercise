# coding=utf-8
# date: 2018-8-25,21:19:17
# name: smz

import tensorflow as tf
"""
tensorflow中最基本的类
tensor = tf.convert_to_tensor(value, dtype, name)  
tensor = tf.constant(value, dtype, name)
参数:
  value  可以是ndarray,也可以不是
  dtype  tf.int32, tf.float32 ...
  name   实际上是与该tensor相关联的操作的名称,而且,名字中不可含有空格
基本属性:
    .graph   返回当前张量tensor所在的图对象 <tensorflow.python.framework.ops.Graph object at 0x7fc52caa8850>
基本方法:
    $.eval()  获取tensor的值
     
   
注:
    1.凡是需要在环境tf.Session()中执行的方法,前面都有标记$
    2.tensor类实际上都是与某个操作相关联的,作为某个操作的输出而存在,其构造函数中有三个参数：op, value_index, dtype
        def __init__(self, op, value_index, dtype):
            op指的是某个操作
    3.上面tf.convert_to_tensor() 实际是调用的tf.constant()
    4.诸如tf.constant()这种操作不需要输入tensor却能向其他的操作提供tensor的操作被称作 源op
    
"""
def demo_tensor():

    tensor_a = tf.convert_to_tensor(12)

    with tf.Session() as sess:
    # 每生成一个Session()都会对GPU进行一次部署:I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: GeForce GTX 1050


        print 'tensor_a:', tensor_a    # Tensor("Const:0", shape=(), dtype=int32) Const为操作类的实例名,0为Const的输出的第一个值
        print 'tensor_a.eval():', tensor_a.eval()

        tensor_b = tf.constant(13,dtype=tf.float32)
        print 'tensor_b:', tensor_b    # Tensor("Const_1:0", shape=(), dtype=float32)
        print 'tensor_b.eval():', tensor_b.eval()

        tensor_c = tf.constant(34, dtype=tf.float32, name='my_constant')
        print 'tensor_c:', tensor_c    # Tensor("my_constant:0", shape=(), dtype=float32) 操作类实例更名为:my_constant
        print 'tensor_c.eval():', tensor_c.eval()

        tensor_a = tensor_a + 1
        print 'new tensor_a:', tensor_a   # Tensor("add:0", shape=(), dtype=int32) 这次这个tensor变为了操作add的输出,与上面的tensor_a不同
                                          # 上面的tensor_a 是Const操作类的输出
        print 'new tensor_a.eval():', tensor_a.eval()
        print 'tensor_a.graph:', tensor_a.graph


if __name__ == '__main__':
    demo_tensor()