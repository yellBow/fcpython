# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 21:29:29 2021

@author: user
"""

# 題1 請隨機取數1~49取6個,且整數不可重複,並放入串列中
while True:
    import random
    a = random.randint(1,49)
    b = random.randint(1,49)
    c = random.randint(1,49)
    d = random.randint(1,49)
    e = random.randint(1,49)
    f = random.randint(1,49)
    x=[a,b,c,d,e,f]
    a1=x.count(a)
    b1=x.count(b)
    c1=x.count(c)
    d1=x.count(d)
    e1=x.count(e)
    f1=x.count(f)
    if a1==1 and b1==1 and c1==1 and d1==1 and e1==1 and f1==1:                   
            y=[]
            y+=x
            print(y)
            break

