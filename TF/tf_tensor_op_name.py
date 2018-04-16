# coding=utf-8
# date: 2018-4-16,08:47:35
# name: smz

import tensorflow as tf


def example_one():
    g = tf.Graph()
    with g.as_default():

        tensor_a = tf.convert_to_tensor([1, 2, 3], name='tensor_a')
        # The name 'tensor_a' refers to an Operation, not a Tensor. Tensor names must be of the form "<op_name>:<output_index>"
        tensor_b = tf.convert_to_tensor([4, 5, 6], name='tensor_b')
        result = tf.add(tensor_a, tensor_b, name='add_a_b')

    # 'tensor_a', 'tensor_b', 'add_a_b'其实都是操作的名字,准确的来说应该说是该行所代表的一系列的操作的前缀,当前最上层(我们自己写的操作)的操作
    # 名字就是我们自己所定义的,若该操作还调用了其他操作,那么那些其他操作的名字将都通过tensor_a/打头的形式给出
    # [<tf.Operation 'tensor_a' type=Const>, <tf.Operation 'tensor_b' type=Const>, <tf.Operation 'add_a_b' type=Add>]
    # 操作结果的名字 由操作的名字加上索引构成,如: tensor_a:0, tensor_a代表操作, 0代表该操作输出值的索引
    # Tensor("tensor_a:0", shape=(3,), dtype=int32) Tensor("tensor_b:0", shape=(3,), dtype=int32) Tensor("add_a_b:0", shape=(3,), dtype=int32)
    operations = g.get_operations()
    print '-' * 50 + 'example_one' + '-' * 50
    print operations
    print tensor_a, tensor_b, result

def example_two():
    g = tf.Graph()
    with g.as_default():
        variable_a = tf.get_variable(name='var_a', dtype=tf.float32, shape=(), initializer=tf.constant_initializer(5))
    operations = g.get_operations()

    # variable_a = tf.get_variable(name='var_a', dtype=tf.float32, shape=(), initializer=tf.constant_initializer(5))
    # 该行所涉及的一系列的操作的名字均以var_a打头,我自己写的该行是一个VariableV2操作,其名字为：var_a
    # 由于还调用了其他的操作,那么那些操作也都以'var_a/'打头
    # 一共有4个操作
    # <tf.Operation 'var_a' type=VariableV2>
    # <tf.Operation 'var_a/Initializer/Const' type=Const>
    # <tf.Operation 'var_a/Assign' type=Assign>
    # <tf.Operation 'var_a/read' type=Identity>

    # 变量名也同张量名一样,是由操作名+输出索引构成
    # <tf.Variable 'var_a:0' shape=() dtype=float32_ref>

    print '-' * 50 + 'example_two' + '-' * 50
    print operations
    print variable_a

if __name__ == '__main__':
    example_one()
    example_two()