# -*- coding: utf-8 -*-
"""
Advent of Code - Day 01 2020, part 2

find 3 numbers in the data set that add to 2020 and determine their product

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
    for j in range(length):     
        for k in range(length):
            if i < length:
                num1 = expense_data[i]
            if j < length:
                if j == length:
                    j = 0
                
                num2 = expense_data[j]
                if k < length:
                    if k == length:
                        k = 0
                    num3 = expense_data[k]
                    result = num1 + num2 + num3
                    if result == 2020:
                        print(num1, num2, num3)
                        multiplied = num1 * num2 * num3
                        print("Advent of Code, Day 1, part 2 answer:")
                        print(multiplied)
                        break
                    else:
                             #print("no number pair found to equal 2020")
                        #j += 1
                        continue
            if k == length:
                j += 1
                    #j = 0
            if j == length:
                i += 1
            else: 
                continue
