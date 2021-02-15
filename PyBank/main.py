#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 19:09:08 2021

@author: robinmevans
"""
count=int()
date_set=set()
p_l_int=int()
max_profit=int()
max_month=str()
min_profit=int(99999999999999)
min_month=str()
fin_file = open("Resources/budget_data.csv")
for line  in fin_file.readlines()[1:]:
    count+=1
        
    # print(line.split(','))
    date_set.add(line.split(',')[0])
    
    #x=int(line.split(',')[1][:-2])
    x=line.split(",")
    x=x[1]
    x=x[:-1]
    x=int(x)
    p_l_int+=x

    if x > max_profit:
        max_profit=x
        max_month=line.split(",")[0]
        
    if x < min_profit:
        min_profit=x
        min_month=line.split(",")[0]
    
fin_file.close()    
    
    
    
# print(len(date_set))
# print(p_l_int)
# print(p_l_int/count)
# print( max_month, max_profit )
# print( min_month, min_profit )

output=f'''text
Financial Analysis
------------------------------------
Total Months: {len(date_set)}
Total: ${p_l_int}
Average Change: ${p_l_int/count}
Greatest Increase in Profits: {max_month} (${max_profit})
Greatest Decrease in Profits: {min_month} (${min_profit})'''

print(output)

output_file=open("analysis/PyBank_Final_PrintStmt.txt","w")
output_file.write(output)
output_file.close()