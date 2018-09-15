# coding=utf-8
# date: 2018-4-6,18:43:38
# name: smz


import xml.etree.ElementTree as ET


def parse_xml(file_path):
    xml_file = ET.parse(file_path)  # 这是个ElementTree对象,至于对象是怎么封装的就不要管了,因为如果全是私有属性的话,什么都看不到
    root = xml_file.getroot()  # 从对象中获得其根节点对象

    for children in root._children:  # _children下是所有的子节点
        print children

    size = root.find('size')       # 要取某个节点要使用find('')方法

    height = size.find('height').text  # 获取叶子节点中的内容,都是字符串类型的
    width = size.find('width').text

    for object in root.iter('object'):  # 如果有多个同名的子节点,可以使用iter方法来遍历每个子节点
        bbox = object.find('bndbox')

    print 'test'


if __name__ == '__main__':
    file_path = '/media/smz/SMZ_WORKING_SPACE/Github/Exercise/Python/files/000000.xml'
    parse_xml(file_path)
