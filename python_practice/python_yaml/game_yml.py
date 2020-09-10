# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : game_yml.py
# @Author   : Pluto.
# @Time     : 2020/9/10 15:41
import yaml


class Game():
    def __init__(self):
        data = yaml.safe_load(open("game.yml"))
        self.my_hp = data["me"]["hp"]
        self.my_power = data["me"]["power"]
        self.your_hp = data["you"]["hp"]
        self.your_power = data["you"]["power"]

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

game = Game()
game.fight()