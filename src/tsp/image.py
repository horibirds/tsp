# -*- coding: utf-8 -*-
__author__ = 'KazunoriHori'
from Town import Town
import matplotlib.animation as animation
from pylab import *
import matplotlib.pyplot as plt
#図を作成
# def show_town_by_movie(town_list_list, interval):
#     fig = plt.figure()
#
#     ims = []
#     for town_list in town_list_list:
#         X = []
#         Y = []
#         for town in town_list:
#             X.append(town.x)
#             Y.append(town.y)
#         color = ['r'] * len(town_list)
#         # plt.clf()
#         im = plt.scatter(X, Y, c=color, s=50)
#         ims.append([im])
#
#     # アニメーション作成
#     ani = animation.ArtistAnimation(fig, ims, interval=interval, repeat_delay=1000)
#     # 表示
#     plt.show()


def show_town_by_movie(town_list_list, con_town_list, interval, hakka_list):
    # plt.figure()
    line, = plt.plot([], [], 'k-', lw=2)
    town_point, = plt.plot([], [], 'wo', ms=7)
    som_point, = plt.plot([], [], 'bo', ms=7)
    hakka_point, = plt.plot(0, 0, 'ro', ms=7)
    plt.xlim(0,700)
    plt.ylim(0,700)
    # plt.grid()
    fig=plt.gcf()
    # ax=plt.gca()
    # ax.set_aspect('equal')

    def animate(nframe):
        print nframe
        X = []
        Y = []
        for town in con_town_list:
            X.append(town.x)
            Y.append(town.y)
        town_point.set_data(X, Y)
        X = []
        Y = []
        for town in town_list_list[nframe]:
            X.append(town.x)
            Y.append(town.y)
        som_point.set_data(X, Y)
        line.set_data(X, Y)
        town = con_town_list[hakka_list[nframe]]
        hakka_point.set_data(town.x,town.y)

    anim = animation.FuncAnimation(fig,
        animate, len(town_list_list), blit=False, interval=interval, repeat=False)
    # anim.save("anim.mp4")
    plt.show()

def show_town_by_path(gene, town_list):
    im = get_plot(gene, town_list)
    plt.show()


def show_som_by_path(town_list, som_list):
    im1 = get_plot_path(range(len(som_list)), som_list)
    im2 = get_plot(range(len(town_list)), town_list)
    plt.show()

def save_town_by_path(gene, town_list, save_path):
    im = get_plot(gene, town_list)
    plt.savefig(save_path)

def get_plot(gene, town_list):
    point_table = []
    for i in gene:
        town = town_list[i]
        point_table.append((town.x, town.y))
    # 最大値取得
    max_x = max(map(lambda x: x[0], point_table)) + 20
    max_y = max(map(lambda x: x[1], point_table)) + 20
    xlim([-20, max_x])
    ylim([-20, max_y])
    im = plt.plot(map(lambda x: x[0], point_table), map(lambda x: x[1], point_table), "o")
    return im

def get_plot_path(gene, town_list):
    point_table = []
    for i in gene:
        town = town_list[i]
        point_table.append((town.x, town.y))
    # 最大値取得
    max_x = max(map(lambda x: x[0], point_table)) + 20
    max_y = max(map(lambda x: x[1], point_table)) + 20
    xlim([-20, max_x])
    ylim([-20, max_y])
    im1 = plt.plot(map(lambda x: x[0], point_table), map(lambda x: x[1], point_table), "o")

    x0, y0 = point_table[0]
    for x1, y1 in point_table:
        im2 = plt.plot([x0, x1], [y0, y1], 'k-')
        x0, y0 = x1, y1
    return im1, im2