# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 07:16:24 2020

 2020 Advent of Code, Day 2
 Analyze validity of passwords from input file.
 Each line item is a new password and rule.

@author: willg
"""
import os
import csv
os.chdir(r"C:\Users\willg\Dropbox\Projects\2020 Advent of Code") #set to the correct directory for the data
Raw_Data = open("Day2_Data.txt","r") #opens the data file to be interpreted.
list_data = Raw_Data.readlines() #creates a list with each line in the file as a separate element in the list.
good_pw = 0
occurrence = 0 #set global variable value to start the loop
final_list = [] #create empty list to be populated
for row in list_data: #start the iteration through the data file.  will iterate the number of times necessary to analyze all rows of the file.
    split_data = row.split() #creates a list of the words in the string, effectively making a global list of final_list[(split_data[0], split_data[1], split_data[2])]
    print(split_data) #just to check the output format
    char_count = len(split_data[0]) #determine how long the first list item is to create the range section
    Range = split_data[0] #defines the local variable for the range based on the local list 
         
    if char_count == 3: 
        Range_Start = int(Range[0])
        Range_End = int(Range[2])
        print("Range Start = ",Range_Start, "Range End = ", Range_End)
        
    elif char_count == 5:
        Range_Start = int(Range[0] + Range[1])
        Range_End = int(Range[3] + Range[4])
        print("Range Start = ",Range_Start, "Range End = ", Range_End)
    elif char_count == 4:
        Char2 = Range[1]
        if type(Char2) == int:
            Range_Start = int(Range[0] + Range[1])
            Range_End = int(Range[3])
            print("Range Start = ",Range_Start, "Range End = ", Range_End)
        elif type(Char2) == str:
            Range_Start = int(Range[0])
            Range_End = int(Range[2] + Range[3])
            print("Range Start = ",Range_Start, "Range End = ", Range_End)
        else:
            pass
    else:
        pass
    Check_char = split_data[1][0] #parse out the character to check for
    print("The character to check in the password is: ", Check_char)
    
    occurence = split_data[2].count(Check_char) #count how many times the check character occurs
    print("The # of occurences for check character is: ", occurence)
    
    if Range_Start <= occurence <= Range_End:
        good_pw += 1
    
    else:
        pass
    print("# of good passwords: ", good_pw)
            
    
    final_list.append(split_data)


Raw_Data.close()
