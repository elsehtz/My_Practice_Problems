import sys
import datetime
import numpy as np
import os

# file1 = open("<file_name.type>","w") 'w' writes over file
# file1 = open("<file_name.type>","a") 'a' appends and write() data onto the current contents

def main():
    # Case 1: txt
    file_type = input("What kind of file are you writing to? (txt, json, csv)\n").lower()
    if(file_type == 'txt'):a
        file1 = open("write_to_file_practice.txt","w")# w for write mode, a for append mode
        file1.write(input("Type something to put into example txt file\n"))
        print("Check write_to_file_practice.txt in the directory to see!")
    # Case 2: csv
    elif(file_type == 'csv'):
        file1 = open("write_to_file_practice.csv","w")# w for write mode, a for append mode
        file1.write('it worked')
        print("String placed in example csv file, try real data next!")

    # Case 3: JSON
    elif(file_type == 'json'):
        file1 = open("write_to_file_practice.json","w")# w for write mode, a for append mode
        file1.write("Placed holder for example write to json")
    
    else:
        print("Sorry, file specificed not recognized. Approved types are txt, json, and csv")
    
    return

if __name__ == '__main__':
    
    main()