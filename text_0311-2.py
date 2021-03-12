# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 23:59:25 2021

@author: HeroPC
"""

# 題2 [100,80,1,3,10,7] 請排序小~大 (氣泡排序)
p=[]
a=[100,80,1,3,10,7]
for i in range(6):    
    mi=min(a)
    x=[mi]
    a.remove(mi)
    p+=x
print(p) 