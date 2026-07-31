# Count Lines in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts how many lines are present in the file.
# Input:
# Demo.txt
# Expected Output:
# Total number of lines in Demo.txt.

import sys
import os

def CountLines(FileName):

    Ret = False
    Ret = os.path.exists(FileName)

    if(Ret == False):
        print("File Does not exists")
        return

    fobj = open(FileName,"r")
    Count = 0

    for line in fobj:
        Count = Count + 1

    fobj.close()

    print("Number of line from file is : ",Count)

def main():

    if(len(sys.argv) == 2):
        CountLines(sys.argv[1])
    else:
        print("Invalid Number of Arguments")

if __name__ == "__main__":
    main()