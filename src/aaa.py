# -*- coding: utf-8 -*-
__author__ = 'KazunoriHori'
# import numpy as np
# import matplotlib.pyplot as plt

#
# np.random.seed(5)
# x = np.arange(1, 101)
# y = 20 + 3 * x + np.random.normal(0, 60, 100)
# plt.plot(x, y, "o")
#
#
# # draw vertical line from (70,100) to (70, 250)
# plt.plot([70, 70], [100, 250], 'k-', lw=2)
#
# # draw diagonal line from (70, 90) to (90, 200)
# plt.plot([70, 90], [90, 200], 'k-')
#
# plt.show()
import tsp
from tsp import file, calc, image, ga
from tsp.Town import Town

i = 3
j = 5

# print range(i,j)
# print range(100)[i:j]
# print range(10)[1:9]
town_list = tsp.file.read_tsp_file("../data/tsp225.tsp")
dis_mat = tsp.calc.get_distance_mat(town_list)
print dis_mat
# list1 = [0,1,2,3,4]
# list2 = [1,3,2,4,0]
# tsp.cross_over(list1,list2,dis_mat)