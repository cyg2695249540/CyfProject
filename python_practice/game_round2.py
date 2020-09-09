# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : game_round2.py
# @Author   : Pluto.
# @Time     : 2020/9/9 16:06
"""
一个回合制游戏，每个角色都有HP和POWER，HP代表血量，POWER代表攻击力
HP初始值1000，POWER初始值200
定义一个方法：
my_hp=hp-enemy_power
enemy_hp=enemy_hp-my_power
打斗多个方法，谁的HP先为0，那么谁就输了
"""

def fight():
    my_hp = 1100
    my_power = 100
    your_hp = 1000
    your_power = 100

    while True:
        my_hp = my_hp - your_power
        your_hp = your_hp - my_power
        if my_hp <= 0:
            print("我输了")
            print("我的剩余血量为:",my_hp)
            print("你的剩余血量为:",your_hp)
            break
        elif your_hp <= 0:
            print(("你输了"))
            print("我的剩余血量为:",my_hp)
            print("你的剩余血量为:",your_hp)
            break

fight()