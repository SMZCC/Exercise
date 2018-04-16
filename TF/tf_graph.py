# coding=utf-8
# date: 2018-4-13,14:55:26
# name: smz

import tensorflow as tf



def graph_use_one():
    g_1 = tf.Graph()
    g_2 = tf.Graph()

    g_1.as_default()
    tensor_a = tf.constant([1, 2])

    g_2.as_default()
    tensor_b = tf.constant([3, 4])

    print 'tensor_a graph:', tensor_a.graph   # 两个张量全在g_2上,g_2是default_graph
    print 'tensor_b graph:', tensor_b.graph
    print 'default graph:', tf.get_default_graph()
    print 'graph g_1:', g_1
    print 'graph g_2:', g_2   # g_2 和default_graph一样,两个张量全部在g_2上,也就是说,这种形式定义的张量是记录在default_graph
                              #当前的default_graph是哪个,那么这两个张量就在哪个图上
    # 验证： 将默认的graph改为g_1
    print '-' * 100
    g_1.as_default()
    print 'tensor_a graph:', tensor_a.graph  # 两个张量全在g_1上,g_1是default_graph
    print 'tensor_b graph:', tensor_b.graph
    print 'default graph:', tf.get_default_graph()
    print 'graph g_1:', g_1
    print 'graph g_2:', g_2

    # 推论错误,两个张量全在default_graph上,也就是说,算上default_graph的话,一共有三个图
    # g_1.as_default()并未作用到张量上

def graph_use_two():
    g_1 = tf.Graph()
    g_2 = tf.Graph()

    with g_1.as_default():
        tensor_a = tf.constant([1, 2])

    with g_2.as_default():
        tensor_b = tf.constant([3, 4])
    print '-' * 100
    print 'tensor_a graph:', tensor_a.graph  # a在图g_1
    print 'tensor_b graph:', tensor_b.graph  # b在图g_2
    print 'default graph:', tf.get_default_graph()  # 这是另外第三张图
    print 'graph g_1:', g_1
    print 'graph g_2:', g_2

    # 结论,要想让某个张量在某个具体的图上,必须使用 with some_graph.as_default():
    # 默认的图随便你定不定义新图,总会存在,在with之外定义的张量全部被认为是该默认图的张量

def graph_keys():

    g = tf.Graph()

    with g.as_default():
        v_b = tf.Variable(0.)
    print '-' * 100
    print tf.GraphKeys.TRAINABLE_VARIABLES  # ?
    print tf.GraphKeys.GLOBAL_VARIABLES     # ?


if __name__ == '__main__':
    graph_use_one()
    graph_use_two()
    graph_keys()
