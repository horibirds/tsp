# -*- coding: utf-8 -*-
from src.tsp import tsp

__author__ = 'KazunoriHori'

if __name__ == '__main__':
    genes_num = 10

    cross_over_rate = 0.5
    inversion_rate = 0.2
    mutation_rate = 0.2

    meneki_num = 200

    # print "データ読み込み中..."
    # town_list = tsp.read_tsp_file("./ch130.tsp")
    town_list = tsp.read_tsp_file("./tsp225.tsp")
    # print "距離計算中..."
    dis_mat = tsp.get_distance_mat(town_list)

    genes = []
    for id in range(83):
        gene = tsp.read_tsp_opt_file("../meneki/"+str(id)+".tour")
        genes.append(gene)

    # print "GA中..."
    for count in range(10000000):

        # print "distance順にgenesをソート中..."
        genes, dis = tsp.sort_genes_by_distance(genes, dis_mat)
        # print dis
        if count % 100 == 0:
            print dis[0], count
        # print genes[0]
        # print genes[1]
        if count == 10000:
            break

        # print "突然変異,交叉,逆位 適応中..."

        genes = tsp.cross_over_all(genes, cross_over_rate, dis_mat)
        genes = tsp.inversion_all(genes, inversion_rate, dis_mat)
        genes = tsp.mutation_all(genes, mutation_rate, dis_mat)

    print dis[0]
    print genes[0]
    print genes[1]
    print genes[2]
    print "パラメータ"
    print genes_num, count, mutation_rate, inversion_rate, cross_over_rate
    save_path = "genes_num-%d-count-%d-mutation_rate-%.2f-inversion_rate-%.2f-cross_over_rate-%.2f" % (genes_num, count, mutation_rate, inversion_rate, cross_over_rate)
    tsp.save_town_by_path(genes[0], town_list, './ga_image/'+save_path+'.png')
    # tsp.show_town_by_path(genes[0], town_list)
