# -*- coding: utf-8 -*-
__author__ = 'KazunoriHori'
from tsp import file, calc, image, som
from tsp.Town import Town
import copy
if __name__ == '__main__':
    # print "データ読み込み中..."
    town_list = file.read_tsp_file("../data/ch130.tsp")
    # town_list = file.read_tsp_file("../data/tsp225.tsp")
    # print "距離計算中..."
    dis_mat = calc.get_distance_mat(town_list)
    som_list = som.get_somlist_from_townlist(town_list, 132)

    r = 400.1
    alpha = 0
    num = 13
    move = 10.0
    a = []
    for count in range(300):
        #入力を発火させてsom_listを動かす
        som_list = som.hakka_all(town_list, som_list, r, num, move)
        i = copy.deepcopy(som_list)
        a.append(i)
        # if count % 100 ==0:
        #     image.show_som_by_path(town_list, som_list)
        r -= alpha
        if r < 5:
            r = 5
        if count in (10, 30, 50, 70):
            num -= 2
            if num < 1:
                num = 1
            move -= 4
            if move < 5.0:
                move = 5.0
    # som_list = som.fit_somlist_to_townlist(som_list, town_list)
    print "表示"
    # image.show_som_by_path(town_list, som_list)
    image.show_town_by_movie(a, town_list, 1)