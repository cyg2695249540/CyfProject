# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : python_game.py
# @Author   : Pluto.
# @Time     : 2020/9/9 19:52

class Game():
    def __init__(self,my_hp,your_hp):
        self.my_hp = my_hp
        self.my_power = 100
        self.your_hp = your_hp
        self.your_power = 100

    def fight(self):
        while True:
            self.my_hp = self.my_hp - self.your_power
            self.your_hp = self.your_hp - self.my_power
            if self.my_hp <= 0:
                print("我的剩余血量为:",self.my_hp)
                print("你的剩余血量为:",self.your_hp)
                print("我输了")
                break
            elif self.your_hp <= 0:
                print("我的剩余血量为:",self.my_hp)
                print("你的剩余血量为:",self.your_hp)
                print(("你输了"))
                break

