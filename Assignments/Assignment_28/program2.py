# Count Words in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts the total number of words in that file.
# Input:
# Demo.txt
# Expected Output:
# Total number of words in Demo.txt.

import sys
import os

def CountWords(FileName):

    Ret = False
    Ret = os.path.exists(FileName)

    if(Ret == False):
        print("File Does not exists")
        return

    fobj = open(FileName,"r")
    Count = 0

    for line in fobj:
        words = line.split()
        Count = Count + len(words)

    fobj.close()

    print("Number of words from file is : ",Count)

def main():

    if(len(sys.argv) == 2):
        CountWords(sys.argv[1])
    else:
        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()