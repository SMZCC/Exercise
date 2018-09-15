# coding=utf-8
# date: 2018-3-31,19:17:57
# name: smz


from collections import OrderedDict
def parse_keyword(one=None, two=None, three=None):
    dict_a = OrderedDict()
    dict_a['one'] = one
    dict_a['two'] = two
    dict_a['three'] = three
    return dict_a

if __name__ == '__main__':
    dict_params_1 = {
        'one': 1,
        'two': 2,
        'three': 3,
    }
    dict_a_1 =  parse_keyword(**dict_params_1)
    print '以关键字作为字符键:', dict_a_1

    dict_params_2 = {
        'three': 3,
        'two': 2,
        'one': 1
    }
    print '调换字符键的顺序:', parse_keyword(**dict_params_2)

    dict_params_3 = {
        'three': 3,
        'two': 2,
        'one': 1,
        # 'four': 4    # 关键字字典集合中的参数必须是函数所要接受的参数,多了会报错
    }
    print '多于函数的关键字个数:', parse_keyword(**dict_params_3)

    dict_params_4 = {
        'three': 5,
        'two': 2,
        'one': 10,
        # 'four': 4
    }
    print '修改键所对应的值:', parse_keyword(**dict_params_4)

    dict_params_5 = {
        'three': 5,
        'two': 2,
    }
    print '减少键的个数:', parse_keyword(**dict_params_5)

    dict_params_6 = {
        'three': 3,
        'two': 2,
        # 'four': 1  # 报错,提示没有该键
    }
    print '以非关键字作为字符键:', parse_keyword(**dict_params_6)