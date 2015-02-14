# -*- coding: utf-8 -*-
from Town import Town

__author__ = 'KazunoriHori'

#tspファイル読み込み - cities作成
def read_tsp_file(filename):
    fin = open(filename)
    town_list = []
    id = 0
    for row in fin:
        list = row[:-1].split(' ')
        name = list[0]
        x = float(list[1])
        y = float(list[2])
        town1 = Town(id, name, x, y)
        town_list.append(town1)
        id += 1
    fin.close()
    return town_list

# optファイル読み込み
def read_tsp_opt_file(filename):
    fin = open(filename)
    town_id_list = []
    for row in fin:
        town_id_list.append(int(row[:-1])-1)
    fin.close()
    return town_id_list

# geneファイル書き込み
def write_gene_file(filename, gene):
    fout = open(filename,"w")
    for id in gene:
        fout.write(str(id+1)+"\n")
    fout.close()

#ファイル出力
def write_tour_file(self, filename, dict = None):
    fout = open(filename,"w")
    if dict != None:
        for k, v in dict.items():
            fout.write(k + " : " + str(v) +"\n")

    for id in self.tourList:
        town = self.townList[id]
        fout.write("%04d" % (id) + " : " + str(town.name)+"\n")
    fout.close()