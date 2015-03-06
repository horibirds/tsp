# -*- coding: utf-8 -*-
__author__ = 'KazunoriHori'
from Town import Town
import random
import calc
import math
def get_rect_somlist_from_townlist(town_list, num):
    point_table = []
    for town in town_list:
        point_table.append((town.x, town.y))
    # 最大値取得
    max_x = max(map(lambda x: x[0], point_table))
    max_y = max(map(lambda x: x[1], point_table))
    min_x = min(map(lambda x: x[0], point_table))
    min_y = min(map(lambda x: x[1], point_table))

    min_x += 20
    min_y += 20
    max_x -= 20
    max_y -= 20

    length_x = max_x - min_x
    length_y = max_y - min_y
    neu_list = []

    for id in range(num):
        # ランダム
        if random.random() > 0.5:
            x = random.randint(int(min_x)+1,int(max_x))
            if random.random() < 0.5:
                y = min_y
            else:
                y = max_y
        else:
            y = random.randint(int(min_y)+1,int(max_y))
            if random.random() < 0.5:
                x = min_x
            else:
                x = max_x

        name = ''
        town1 = Town(id, name, x, y)
        neu_list.append(town1)

    neu_list_max_x = [neu for neu in neu_list if neu.x == max_x]
    neu_list_min_x = [neu for neu in neu_list if neu.x == min_x]
    neu_list_max_y = [neu for neu in neu_list if neu.y == max_y]
    neu_list_min_y = [neu for neu in neu_list if neu.y == min_y]
    neu_list_max_y = sorted(neu_list_max_y, key=lambda n: n.x)
    neu_list_max_x = sorted(neu_list_max_x, key=lambda n: n.y)[::-1]
    neu_list_min_y = sorted(neu_list_min_y, key=lambda n: n.x)[::-1]
    neu_list_min_x = sorted(neu_list_min_x, key=lambda n: n.y)
    neu_list = []
    neu_list.extend(neu_list_max_y)
    neu_list.extend(neu_list_max_x)
    neu_list.extend(neu_list_min_y)
    neu_list.extend(neu_list_min_x)

    return neu_list


def get_circle_somlist(num, r, center):
    som_list = []
    for id in range(num):
        rad = 2.0 * math.pi * id / num
        x = r * math.cos(rad) + center[0]
        y = r * math.sin(rad) + center[1]
        name = ''
        town = Town(id, name, x, y)
        som_list.append(town)
    return som_list

def update(som_list, town_list):
    #入力を発火させてsom_listを動かす
    pass

def hakka_all(town_list, som_list, r, num, move):
    rand_list = range(len(town_list))
    random.shuffle(rand_list)
    for rand in rand_list:
        town = town_list[rand]
        if town.fix == 1:
            continue
        som_list = hakka(town, som_list, r, num, move)
    return som_list

def hakka(town, som_list, r, num, move):
    # 入力と一致したら次から発火しない
    neu_dis_list = []
    for neu in som_list:
        dis = calc.distance(town, neu)
        neu_dis_list.append((neu, dis))
    neu_dis_list = sorted(neu_dis_list, key=lambda l: l[1])
    cnt = 0
    for neu, dis in neu_dis_list:
        if cnt == num:
            break
        if neu.fix == 1:
            continue
        if dis < r:
            x = town.x - neu.x
            y = town.y - neu.y
            sin = y/dis
            cos = x/dis
            neu.x += move*x
            neu.y += move*y
            cnt += 1

            dis = calc.distance(town, neu)
            if dis < 10:
                town.fix = 1
                neu.fix = 1
                break
    return som_list

def fit_somlist_to_townlist(som_list, town_list):
    # somがtownに対するneuronのidを取得する
    som_id_list = []
    for town in town_list:
        id = 0
        min = 100000
        for neu in som_list:
            if id in som_id_list:
                id += 1
                continue
            dis = calc.distance(neu, town)
            if dis < min:
                min = dis
                min_id = id
            id += 1
        som_list[min_id].x = town.x
        som_list[min_id].y = town.y
        som_id_list.append(min_id)

    # idに該当しないneuronを消していく
    id_list = range(len(som_id_list))
    id_list.sort()
    id_list.reverse()

    for id in id_list:
        if id in som_id_list:
            continue
        del som_list[id]
    return som_list