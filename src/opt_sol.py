# -*- coding: utf-8 -*-
__author__ = 'KazunoriHori'
from src.tsp.tsp import tm
if __name__ == "__main__":
    print "データ読み込み中..."
    tm_1 = tm("./ch130.tsp")
    print "距離計算中..."
    tm_1.get_distance_mat()
    print "最短経路検索中..."
    f = open("./ch130.opt.tour")
    list = []
    for row in f:
        list.append(int(row[:-1])-1)
    tm_1.tourList = list
    print len(list)
    f.close()
    print "最短経路出力中..."
    tm_1.save_town_by_path("opt.png")
    print tm_1.length
    print "終了"