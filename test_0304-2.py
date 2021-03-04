# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 21:38:50 2021

@author: user
"""
#第二題 利用 for range印出 [2,4,6,8]
for i in range(2,10,2):  
        if i%2 ==0:
            print(i,end="")
            if i<8:
                 print(',',end='')