# -*- coding: utf-8 -*-
from src.tsp import tsp

__author__ = 'KazunoriHori'

if __name__ == '__main__':
    town_list = tsp.read_tsp_file("./tsp225.tsp")
    # opt_id_list = tsp.read_tsp_opt_file("./tsp225.opt.tour")
    id = 9
    opt_id_list = tsp.read_tsp_opt_file("./meneki/"+str(id)+".tour")
    dis_mat = tsp.get_distance_mat(town_list)
    gene = opt_id_list
    print tsp.get_distance_from_gene(gene, dis_mat)
    # tsp.show_town_by_path(gene, town_list)
    tsp.save_town_by_path(gene, town_list, './meneki/images/'+str(id)+'.png')