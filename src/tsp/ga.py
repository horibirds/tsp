# -*- coding: utf-8 -*-
__author__ = 'KazunoriHori'
import random
from random import Random
# GA実装
def create_genes_rand(num, town_list):
    genes = []
    for i in range(num):
        gene = create_gene_rand(town_list)
        genes.append(gene)
    return genes

def create_gene_rand(town_list):
    gene = [town.id for town in town_list]
    r = Random()
    r.shuffle(gene)
    return gene

def get_distance_from_gene(gene, dis_mat):
    dis = 0
    id1 = int(gene[0])
    id2 = int(gene[0])
    for tmp_id in range(len(gene)):
        id1 = int(gene[tmp_id])
        dis += float(dis_mat[id1][id2])
        id2 = id1
    return dis

def sort_genes_by_distance(genes, dis_mat):
    gene_dis_list = []
    for gene in genes:
        dis = get_distance_from_gene(gene, dis_mat)
        gene_dis_list.append((gene ,dis))
    sorted_gene_dis_list = sorted(gene_dis_list, key=lambda l: l[1])
    sorted_gene_list = [gene_dis[0] for gene_dis in sorted_gene_dis_list]
    dis_list = [gene_dis[1] for gene_dis in sorted_gene_dis_list]
    # print sorted_gene_dis_list
    return sorted_gene_list, dis_list

def select_genes(genes, select_list):
    out_genes = []

    for i in range(len(select_list)):
        for j in range(select_list[i]):
            out_genes.append(list(genes[i]))
    return out_genes

def mutation_all(genes, ratio, dis_mat):
    if len(genes) <= 1:
        print "mutation : genesのサイズが1以下です！！"
        return genes
    for cnt in range(len(genes)):
        if random.random() < ratio:
            genes[cnt] = mutation(list(genes[cnt]), dis_mat)
    return genes

def mutation(gene, dis_mat):
    tmp_gene = list(gene)
    i = random.randint(0,len(gene)-1)
    j = random.randint(0,len(gene)-1)
    while i == j:
        j = random.randint(0,len(gene)-1)
    tmp_gene[i], tmp_gene[j] = int(gene[j]), int(gene[i])
    dis = get_distance_from_gene(gene, dis_mat)
    tmp_dis = get_distance_from_gene(tmp_gene, dis_mat)
    if tmp_dis < dis:
        return tmp_gene
    else:
        return gene

def inversion_all(genes, ratio, dis_mat):
    if len(genes) <= 1:
        print "inversion : genesのサイズが1以下です！！"
        return genes
    for cnt in range(len(genes)):
        if random.random() < ratio:
            genes[cnt] = inversion(list(genes[cnt]), dis_mat)
    return genes

def inversion(gene, dis_mat):
    tmp_gene = list(gene)
    i = random.randint(0,len(gene)-1)
    j = random.randint(0,len(gene)-1)
    while i == j:
        j = random.randint(0,len(gene)-1)
    if i > j:
        tmp_gene[j:i] = gene[j:i][::-1]
    else:
        tmp_gene[i:j] = gene[i:j][::-1]
    dis = get_distance_from_gene(gene, dis_mat)
    tmp_dis = get_distance_from_gene(tmp_gene, dis_mat)
    if tmp_dis < dis:
        return tmp_gene
    else:
        return gene

def cross_over_all(genes, ratio, dis_mat):
    out_genes = []
    if len(genes) <= 1:
        print "cross_over : genesのサイズが1以下です！！"
        return genes
    for cnt in range(len(genes)):
        if random.random() < ratio:
            rand = random.randint(0, len(genes)-1)
            while rand == cnt:
                rand = random.randint(0, len(genes)-1)
            cross_gene = genes[rand]
            gene = cross_over(genes[cnt], cross_gene, dis_mat)
            out_genes.append(gene)
        else:
            out_genes.append(genes[cnt])
    return out_genes
# geneにcross_geneを交差させる(geneが変更)
def cross_over(gene, cross_gene, dis_mat):
    tmp_gene = list(gene)
    i = random.randint(0, len(gene)-1)
    j = random.randint(0, len(gene)-1)
    while i == j:
        j = random.randint(0, len(gene)-1)
    if i > j:
        tmp = i
        i = j
        j = tmp
    for k in range(i, j+1):
        tmp_value = tmp_gene[k]
        cross_value = cross_gene[k]
        tmp_gene[tmp_gene.index(cross_value)] = tmp_value
        tmp_gene[k] = cross_value
    dis = get_distance_from_gene(gene, dis_mat)
    tmp_dis = get_distance_from_gene(tmp_gene, dis_mat)
    if tmp_dis < dis:
        return tmp_gene
    else:
        return gene

def men_eki(genes):
    onaji_list = []
    genes_len = len(genes)
    gene_len = len(genes[0])
    genes1 = list(genes)
    genes2 = list(genes)
    for i in range(genes_len):
        gene1 = genes1[i]
        for j in range(i+1, genes_len):
            # print i,j
            gene2 = genes2[j]
            count = 0
            for k in range(gene_len):
                if gene1[k] == gene2[k]:
                    count += 1
            if count > 80:
                onaji_list.append(j)
    # 消す
    onaji_list = list(set(onaji_list))
    onaji_list.sort()
    onaji_list.reverse()
    # print onaji_list
    for id in onaji_list:
        # print id
        del genes1[id]
    # print len(genes1)
    return genes1