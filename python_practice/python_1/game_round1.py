# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : game_round1.py
# @Author   : Pluto.
# @Time     : 2020/9/9 15:53
"""
一个回合制游戏，每个角色都有HP和POWER，HP代表血量，POWER代表攻击力
HP初始值1000，POWER初始值200
定义一个方法：
my_hp=hp-enemy_power
enemy_hp=enemy_hp-my_power
两个人血量对比，血量剩余多的获胜
"""
def fight():
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 200
    my_final_hp = my_hp - your_power
    your_final_hp = your_hp - my_power
    if my_final_hp > your_final_hp:
        print("我赢了")
    elif my_final_hp < your_final_hp:
        print(("你赢了"))
    else:
        raise Exception("no peace,不要平局,战斗到最后一刻")
        # print("平局")

fight()