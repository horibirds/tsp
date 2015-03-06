# -*- coding: utf-8 -*-
__author__ = 'KazunoriHori'
from tsp import file, calc, image, som
from tsp.Town import Town
import copy
import math
import random
if __name__ == '__main__':
    # print "データ読み込み中..."
    town_list = file.read_tsp_file("../data/ch150.tsp")
    # town_list = file.read_tsp_file("../data/tsp225.tsp")
    # print "距離計算中..."
    dis_mat = calc.get_distance_mat(town_list)
    neu_num = 450
    circle_r = 300
    circle_center = (350, 350)

    som_list = som.get_circle_somlist(neu_num, circle_r, circle_center)

    b = 100
    r = 300.1
    num = int(len(town_list)*0.15)
    # num = 13
    som_list_list = []
    hakka_list = []
    for t in range(300):
        #学習率係数
        a = 1/math.log(t+2)
        move = a
        #入力を発火させてsom_listを動かす
        # som_list = som.hakka_all(town_list, som_list, r, num, move)

        rand = random.randrange(len(town_list))
        town = town_list[rand]
        if town.fix == 1:
            continue
        som_list = som.hakka(town, som_list, r, num, move)
        hakka_list.append(rand)
        som_list_list.append(copy.deepcopy(som_list))


        if t % b == 0:
            num -= 1
            if num < 1:
                num = 1
            r -= 0.1
            if r < 1:
                r = 1
        # if count % 100 ==0:
        #     image.show_som_by_path(town_list, som_list)
    print len(som_list)
    som_list = som.fit_somlist_to_townlist(som_list, town_list)
    print "表示"
    print len(som_list)
    image.show_som_by_path(town_list, som_list)
    image.show_town_by_movie(som_list_list, town_list, 1, hakka_list)