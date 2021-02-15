#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 19:09:08 2021

@author: robinmevans
"""
count=int()
date_set=set()
p_l_int=int()
fin_file = open("Resources/budget_data.csv")
for line  in fin_file.readlines()[1:]:
    count+=1
    
    print(line.split(','))
    date_set.add(line.split(',')[0])
    
    #x=int(line.split(',')[1][:-2])
    x=line.split(",")
    x=x[1]
    x=x[:-2]
    x=int(x)
    p_l_int+=x

    
    
    
print(len(date_set))
print(p_l_int)
print(p_l_int/count)