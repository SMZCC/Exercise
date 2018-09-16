# coding=utf-8
# date: 2018-9-16,19:10:18
# name: smz

import py_compile
"""
1..pyc文件是.py被编译后的字节码(byte code)文件
2..pyc经过python解释器最终会生成机器码执行
3..pyc是可以跨平台部署的,类似于java的.class
文件生成方法:
    i.  使用命令: python -m fool.py
    ii. 使用py_compile库文件:
          import py_compile
          py_compile.compile('./fool.py')
    iii.使用py_compileall将一个目录下的全部.py文件都编译,这个在py2.7中没有发现
执行方法：
    在控制台使用python xxx.pyc
"""


def compilePyFile():
    filePath = './compile_files/helloWord.py'
    py_compile.compile(filePath)


if __name__ == '__main__':
    compilePyFile()