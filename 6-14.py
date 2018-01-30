#coding:utf-8

import random

def guess():
    dic = {1:'剪刀', 2:'石头', 3:'布',}
    win = {'剪刀' : '布', '布' : '石头', '石头' : '剪刀'}
    lose = {'剪刀' : '石头', '石头' : '布', '布' : '剪刀'}

    com = random.randint(1,3)

    while True:
        usr = int(raw_input('Enter you choice: 1-剪刀  2 - 石头  3 - 布  4-退出'))
        while usr not in [1, 2, 3, 4]:
            print '请输入正确手势'
            usr = int(raw_input('Enter you choice: 1-剪刀  2 - 石头  3 - 布  4-退出'))

        if usr == 4:
            print '游戏结束'
            break
        elif win[dic[usr]] == dic[com]:
            print '恭喜你获得胜利'
        elif lose[dic[usr]] == dic[com]:
            print '很遗憾，你失败了'
        else:
            print '平局'

guess()