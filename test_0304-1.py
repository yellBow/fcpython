# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 21:35:50 2021

@author: user
"""
#第一題 請利用 for range 計算1~50之間的偶數和&奇數和
a=0
b=0
for i in range(1,51):  
        if i%2 !=0:
            print(i,"奇數",end=' ')
            a+=i
        else:
            print(i,"偶數")
            b+=i
print('奇數和',a)            
print('偶數和',b)       