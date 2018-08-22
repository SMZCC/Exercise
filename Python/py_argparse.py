# coding=utf-8
# date: 2018-8-22,13:46:18
# name: smz

import argparse
"""
主要使用argparse下的Argumentparser()类进行命令行解析
    parser = argparse.Argumentparser()
类的主要方法： 
  parser.add_argument('-命令行中变量名称的简写', '--变量名称', defaut=默认值, help='一些对变量的说明')
  args = parser.parse_args() # 无参数, 将所有的命令行参数解析出来,保存在args中,通过args.xxx调用
  
"""

def print_hello_someone(args):
    print 'Hello ' + args.name

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', default='SMZ', help="someone's name")
    args = parser.parse_args()
    print_hello_someone(args)