# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : houyi.py
# @Author   : Pluto.
# @Time     : 2020/9/9 20:26
from python_practice.python_1.game.python_game import Game


class HouYi(Game):
    def __init__(self,houyi_hp,your_hp,defense):
        super().__init__(my_hp=houyi_hp,your_hp=your_hp)
        self.defense = defense

    def fight(self):
        while True:
            self.my_hp = self.my_hp +self.defense - self.your_power
            self.your_hp = self.your_hp - self.my_power
            if self.my_hp <= 0:
                print("houyi剩余血量为:",self.my_hp)
                print("你的剩余血量为:",self.your_hp)
                print("houyi输了")
                break
            elif self.your_hp <= 0:
                print("houyi剩余血量为:",self.my_hp)
                print("你的剩余血量为:",self.your_hp)
                print(("你输了"))
                break

houyi = HouYi(1000,1000,100)
houyi.fight()