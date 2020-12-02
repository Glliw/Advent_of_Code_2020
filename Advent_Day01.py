# -*- coding: utf-8 -*-
"""
Advent of Code - Day 01 2020

Created on Tue Dec  1 20:28:47 2020

@author: willg
"""

expense_report = list(open("Day1_data.txt", "r"))
#stripped = expense_report.remove(())
#print("Here is the input data as a list:")
#print(expense_report)
#stripped_line = [s.rstrip() for s in expense_report]
expense_data = []

for num in expense_report:
    noslashN= int(num.rstrip())
    #print(noslashN)
    expense_data.append(noslashN)
    
#print(expense_data)
print("length of the list:")    
print(len(expense_data))

length = len(expense_data)

for i in range(length):
     num1 = expense_data[i]
     while i < length:
         result = num1 + expense_data[i]
         if result == 2020:
             print(num1, expense_data[i])
             multiplied = num1 * expense_data[i]
             print("Advent of Code, Day 1 answer:")
             print(multiplied)
             break
         else:
             #print("no number pair found to equal 2020")
             i += 1
             
             

    