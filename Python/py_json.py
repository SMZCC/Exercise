# coding=utf-8
# date: 2018-9-10,14:42:38
# naem: smz

import json
"""
json.dump(<obj>, fp, intent=None)
注:
    1.intent表示缩进等级,用于pretty-print,
        若为None, 保存的json文件中是most compact 模式;
        若为0,仅会插入新行
        
"""


def demo_one():
    data = [1, 2, 3]
    with open('./saved_files/json_one.json', 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    demo_one()