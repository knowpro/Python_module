# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 03:37:18 2022

@author: admin
"""

lnum = int(input("Enter how many numbers to calculate average."))
avg = 0
lst=[]

for i in range(0, lnum):
    no = int(input("no: "))
    lst.append(no)
    
    avg= avg + lst[i]
    
print(avg/lnum)