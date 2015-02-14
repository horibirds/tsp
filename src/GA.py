# -*- coding: utf-8 -*-
from tsp import file, calc, image, ga
from tsp.Town import Town


__author__ = 'KazunoriHori'
import math

if __name__ == '__main__':
    genes_num = 10

    cross_over_rate = 0.5
    inversion_rate = 0.2
    mutation_rate = 0.2

    meneki_num = 200

    # print "データ読み込み中..."
    # town_list = tsp.read_tsp_file("./ch130.tsp")
    town_list = file.read_tsp_file("../data/tsp225.tsp")
    # print "距離計算中..."
    dis_mat = calc.get_distance_mat(town_list)

    # print "genes作成中..."
    for meneki in range(100, meneki_num):
        print meneki
        genes = ga.create_genes_rand(genes_num ,town_list)
        for count in range(10000000):

            # print "distance順にgenesをソート中..."
            genes, dis = ga.sort_genes_by_distance(genes, dis_mat)
            if count % 100 == 0:
                print dis[0], count
            # print genes[0]
            # print genes[1]
            if count == 5:
                break

            # # print "免疫アルゴリズム"
            # genes = tsp.men_eki(genes)


            # print "select中..."
            # select_list = [10]*1 + [8]*1 + [7]*1 + [6]*2 + [5]*1 + [4]*2
            select_list = []
            last_dis = dis[len(dis)-1]
            for i in range(len(genes)):
                num = int(math.ceil((last_dis - dis[i])/1000))
                if num == 0:
                    num = 1
                if sum(select_list) + num > genes_num:
                    select_list.append(genes_num - sum(select_list))
                else:
                    if num == 0:
                        break
                    else:
                        select_list.append(num)
                if sum(select_list) == genes_num:
                    break
            # print select_list
            # print sum(select_list)
            # print dis

            genes = ga.select_genes(genes, select_list)

            # selectで足りなかった文をランダムで補完
            genes.extend(ga.create_genes_rand(genes_num - sum(select_list), town_list))

            # print "突然変異,交叉,逆位 適応中..."

            genes = ga.cross_over_all(genes, cross_over_rate, dis_mat)
            genes = ga.inversion_all(genes, inversion_rate, dis_mat)
            genes = ga.mutation_all(genes, mutation_rate, dis_mat)
        file.write_gene_file("../meneki/"+str(meneki)+".tour", genes[0])
        image.save_town_by_path(genes[0], town_list, '../meneki/images/'+str(meneki)+'.png')


    print dis[0]
    print genes[0]
    print genes[1]
    print genes[2]
    print "パラメータ"
    print genes_num, count, mutation_rate, inversion_rate, cross_over_rate
    save_path = "genes_num-%d-count-%d-mutation_rate-%.2f-inversion_rate-%.2f-cross_over_rate-%.2f" % (genes_num, count, mutation_rate, inversion_rate, cross_over_rate)
    # image.save_town_by_path(genes[0], town_list, '../images/ga_image/'+save_path+'.png')
    # tsp.show_town_by_path(genes[0], town_list)
