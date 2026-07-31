# Search a Word in File
# Problem Statement:
# Write a program which accepts a file name and a word from the user and checks whether that word is present in
# the file or not.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Display whether the word Marvellous is found in Demo.txt or not.

import sys
import os

def SearchWord(FileName,Word):

    Ret = False
    Ret = os.path.exists(FileName)

    if(Ret == False):
        print("File Does not exists")
        return

    fobj = open(FileName,"r")
    bfound = False

    for line in fobj:
        word = line.split()
        if Word in word:
            bfound = True
            break
    fobj.close()

    if(bfound == True):
        print("Word Exist in FIle")
    else:
        print("WOrd Does not Exist")

def main():

    if(len(sys.argv) == 3):
        SearchWord(sys.argv[1],sys.argv[2])
    else:
        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()