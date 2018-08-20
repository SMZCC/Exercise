# coding=utf-8
# date: 2018-3-13,14:59:07
# name: smz

import os
from options import *

file = open(SAVE_DIR, 'w')
cats = sorted(os.listdir(INPUT_DIR))
for idx, cat in enumerate(cats):
    img_dir = os.path.join(INPUT_DIR, cat)
    imgs = os.listdir(img_dir)
    for img in imgs:
        file.write('%s %d\r\n'%(img, idx+1))

file.close()





