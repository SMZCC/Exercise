# coding=utf-8
# date: 2018-5-19,20:49:20
# name: smz

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import cv2
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    detector = cv2
    logging.info('opencv version:%s'%(cv2.__version__))