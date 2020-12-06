# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 07:16:24 2020
https://adventofcode.com/2020/day/2

while it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?.

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
        First_Pos = int(Range[0]) - 1
        Second_Pos = int(Range[2]) - 1
        print("First Position to Check = ",First_Pos + 1, "Second Position to Check = ", Second_Pos + 1)
        
    elif char_count == 5:
        First_Pos = int(Range[0] + Range[1]) - 1
        Second_Pos = int(Range[3] + Range[4]) - 1
        print("First Position to Check = ",First_Pos + 1, "Second Position to Check = ", Second_Pos + 1)
    elif char_count == 4:
        Char2 = Range[1]
        if type(Char2) == int:
            First_Pos = (int(Range[0] + Range[1]) - 1)
            Second_Pos = int(Range[3]) - 1
            print("First Position to Check = ",First_Pos + 1, "Second Position to Check = ", Second_Pos + 1)
        elif type(Char2) == str:
            First_Pos= int(Range[0]) - 1
            Second_Pos = int(Range[2] + Range[3]) - 1
            print("First Position to Check = ",First_Pos + 1, "Second Position to Check = ", Second_Pos + 1)
        else:
            pass
    else:
        pass
    Check_char = split_data[1][0] #parse out the character to check for
    print("The character to check in the password is: ", Check_char)
    print("the first position to check is = ", First_Pos + 1)
    print("the first character checked is = ", split_data[2][First_Pos])
    print('the second position to check is =', Second_Pos + 1)
    print('The second character checked is = ', split_data[2][Second_Pos])
    if split_data[2][First_Pos] == Check_char and split_data[2][Second_Pos] != Check_char: 
        good_pw += 1
    elif split_data[2][Second_Pos] == Check_char and split_data[2][First_Pos] != Check_char:
        good_pw += 1
    else:
        pass
    print("# of good passwords = ", good_pw)
            
    
    final_list.append(split_data)


Raw_Data.close()
