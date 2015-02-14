# -*- coding: utf-8 -*-
__author__ = 'KazunoriHori'

class Town():
    def __init__(self, id, name, x, y):
        self.id = id #town_listの何番目か
        self.name = name
        self.x = x
        self.y = y

        #som用
        self.fix = 0