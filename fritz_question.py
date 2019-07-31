# Creator: Zakary ElSeht
# Created: 7/30/2019
# Last edited: 7/30/2019
# Name: Fritz email questions
# Description: 
# (3 parts) A string reverse method, html filter, 
# and garage/space management pseudocode

# Question 1 - reverse a string
def reverse_str(old_str):
    return old_str[::-1]

#Question 2 - webpages
from bs4 import BeautifulSoup
import glob, os

def files_matched(use_dir, phone_num):
    files = []
    os.chdir(use_dir)

    for file in glob.glob('*.html'):
        with open(file) as fp:
            soup = BeautifulSoup(fp, features="lxml")
        
        if(soup.find_all(string=phone_num)):
            files.append(str(file))
    
    return files

#Question 3 - Pseudocode
'''
class car():
    width: int()
    length: int()

    def area(self):
        ...
    
class location():
    level: int()
    section: int()
    spot_num: int()


class garage():
    spaces: [(filled_bool, spot)]
    open_space: [spot]
    filled_space: [(spot, car())]
    
    def fill_space():
        # find_space()
        # update lists
    def open_space():
        # update lists
    def find_space():
        # check open spots
        # can prioritze a spot based on:
        # location (level), neighboring vehicles (and their size),
        # and or density of filled spaces
        # return a location
'''
def test_q1():
    # Test for question 1
    basic_str = "Hello World"
    print(reverse_str(basic_str))    
    return


def test_q2():
    # Test for question 2
    num = '908-967-7118' # example num
    use_dir = os.getcwd() # use current dir
    print(files_matched(use_dir, num))
    return

if __name__ == "__main__":
    test_q1()
    #test_q2()