# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 04:27:19 2022

@author: admin
"""

lnum = int(input("Enter the size of elements list."))
lst=[]

max_ev = 0
max_od = 0

for i in range(0, lnum):
    lst.append(int(input("no: ")))
        
    if lst[i]%2 != 0:
        if lst[i] > max_od:
            max_od = lst[i]
            
    elif lst[i]%2 == 0:
        if lst[i] > max_ev:
            max_ev = lst[i]
    
    
print(" Greatest odd no", max_od)
print("Greatest even no ", max_ev)