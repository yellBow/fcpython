# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 17:33:02 2021

@author: HeroPC
"""

'''
題2 列出
   *
  ***
 *****
*******
 *****
  ***
   *
'''
a=1
b=5
for i in range(4,0,-1):
    for x in range(1,i):
        print(' ',end='')
    for u in range(0,a,2):   
        print('*',end='')
    print()
    a+=4
for o in range(1,4):
    for j in range(0,o):
        print(' ',end='')  
    for u in range(b,0,-1):   
        print('*',end='')    
    print()
    b-=2