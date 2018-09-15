# coding=utf-8
# date: 2018-4-24,11:21:06
# name: smz

import numpy as np

def save_data(dir, data):
    np.save(dir, data)      # 两个参数,一个是dir, 另一个是要保存的值


if __name__ == '__main__':

    matrix_a = np.array([[1, 2], [3, 4]])
    save_dir = './matrix_a.npy'
    save_data(save_dir, matrix_a)

    matrix = np.load('matrix_a.npy')
    print matrix

