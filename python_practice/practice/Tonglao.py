# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : Tonglao.py
# @Author   : Pluto.
# @Time     : 2020/9/9 20:44
"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，
血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
加入模块化改造
"""

class TongLao():
        def __init__(self,hp,power,defense):
            self.hp = hp
            self.power = power
            self.defense = defense
        def see_people(self,name):
            if name == "WYZ":
                print("师弟！！！")
            elif name == "李秋水":
                print("呸，贱人")
            elif name == "丁春秋":
                print("叛徒！我杀了你")
        def fight_zms(self,enemy_hp,enemy_power,enemy_defense):
            self.power = self.power*10
            self.hp = self.hp / 2
            self.hp = self.hp + self.defense - enemy_power
            enemy_hp = enemy_hp + enemy_defense - self.power
            if self.hp > enemy_hp:
                print("天山童姥获胜")
                print("天山童姥剩余血量",self.hp)
                print("敌人血量",enemy_hp)
            elif self.hp < enemy_hp:
                print("天山童姥也不过如此")
                print("天山童姥剩余血量", self.hp)
                print("敌人血量", enemy_hp)
            else:
                raise Exception("no peace,不要平局,战斗力到最后一刻")

fight = TongLao(2000,200,100)
fight.see_people("丁春秋")
fight.fight_zms(2001,200,100)