# coding=utf-8
# date: 2018-4-13,16:42:23
# name: smz



def get_file(file_dir):

    with open(file_path, 'r') as f:
        file = f
        return file  # 即使在这里返回也没有用
    #return file  # 到这里时,上下文管理器已经执行__exit__了, 所以return出去的东西到底能不能用,要看__exit__里是怎么实现的了






if __name__ == '__main__':
    file_path = '/media/smz/SMZ_WORKING_SPACE/Github/Exercise/Python/files/train_labels.txt'
    f = get_file(file_path)
    print f.readline()
