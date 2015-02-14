# -*- coding: utf-8 -*-
__author__ = 'KazunoriHori'
import math

import numpy as np


#距離を返す
def distance(x1, y1, x2, y2):
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
def distance(town1, town2):
    return math.sqrt(pow(town1.x - town2.x, 2) + pow(town1.y - town2.y, 2))

#都市間の距離を計算したMatrix生成
def get_distance_mat(town_list):
    disMat = np.zeros([len(town_list), len(town_list)])
    for row in range(len(town_list)):
        for col in range(row+1, len(town_list)):
            dis = distance(town_list[row], town_list[col])
            disMat[row][col] = dis
            disMat[col][row] = dis
    return disMat