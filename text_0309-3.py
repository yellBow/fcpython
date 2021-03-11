# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 23:12:45 2021

@author: HeroPC
"""

'''
題3 
import random
ans=random.randint(1,100)
guess=0
while ans != guess:
    guess=int(input('請輸入1~100的整數:'))
'''
import random
ans=random.randint(1,100)
guess=0
a=1
b=100
while ans != guess:
    guess=int(input('請輸入1~100的整數:'))        
    if guess<ans:
        a=guess
        print('介於',a,'~',b,'之間')        
    if guess>ans:
        b=guess      
        print('介於',a,'~',b,'之間')
else:   
        print('恭喜中獎')