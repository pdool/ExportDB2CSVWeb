#!/usr/bin/python3
# -*- coding: utf-8 -*-
def dealStr(str):
    d = str.replace(' ', '')
    d = d.replace('（', '')
    d = d.replace('(', '')
    d = d.replace(')', '')
    d = d.replace('）', '')
    d = d.replace('%', '')
    return d


#     {db} == = 游戏库
#     {logdb} == 日志库
#     {date} == 日期
def replaceSql(str):

    # if str.find("{db}") != -1:
    str = str.replace("{db}","unity3dm")
    print(str)
if __name__ == '__main__':
    replaceSql("select * from unity3dm.player_roles")