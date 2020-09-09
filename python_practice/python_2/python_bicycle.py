# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : python_bicycle.py
# @Author   : Pluto.
# @Time     : 2020/9/9 18:30
"""
写一个Bicycle(自行车)类,有run(骑行)方法, 调用时显示骑行里程km(骑行里程为传入的数字):
再写一个电动自行车类EBicycle继承自Bicycle,添加电池电量valume属性通过，参数传入,
同时有两个方法：
1. fill_charge(vol) 用来充电, vol 为电量
2. run(km) 方法用于骑行,每骑行10km消耗电量1度,
当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，显示骑行结果
"""
class Bicycle():
    def run(self,km):
        print(f"用脚一共骑行了{km}km")

class EBicycle(Bicycle):
    def __init__(self,valum):
        self.valum = valum
    def fill_charge(self,vol):
        print(f"电动车已充电{vol}度")
        print(f"充完电之后还有{vol+self.valum}度")
    def run(self,km):
        e_km = self.valum*10
        print("电动车最大骑行公里数",e_km,"km")
        if km <= e_km:
            print(f"用电一共骑行了{e_km}km")
        else:
            print(f"一共骑行了{e_km}km")
            super().run(km - e_km)

ebike = EBicycle(10)
ebike.run(200)