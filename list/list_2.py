# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 03:51:39 2022

@author: admin
"""

lnum = int(input("Enter the size of elements list."))
lst=[]
sumn = 0
sumnev = 0
sumpod = 0

for i in range(0, lnum):
    lst.append(int(input("no: ")))
    
    if lst[i] < 0 :
        sumn = sumn + lst[i]
        
    if lst[i] > 0 and lst[i]%2 != 0:
        sumpod = sumpod + lst[i]
        
    if lst[i] < 0 and lst[i]%2 == 0:
        sumnev = sumnev + lst[i]
    
    
print("Sum of negative nos : ", sumn)
print("Sum of positive odd nos : ", sumpod)
print("Sum of negative even nos : ", sumnev)