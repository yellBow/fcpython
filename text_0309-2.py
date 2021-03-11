# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 23:12:34 2021

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
'''
for c in range(1,8,2):
    for d in range(0,c):        
            print(d,end='')    
    print() 
for c in range(5,0,-2):   
    for d in range(0,c):        
            print(d,end='') 
    print()     
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